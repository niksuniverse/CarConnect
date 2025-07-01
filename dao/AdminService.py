from exception.DatabaseConnectionException import DatabaseConnectionException
from util.DBConnUtil import get_connection
from dao.IAdminService import IAdminService
from entity.Admin import Admin

class AdminService(IAdminService):

    def __init__(self, config):
        self.config = config

    def get_admin_by_id(self, admin_id):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Admin WHERE AdminID = %s", (admin_id,))
        row = cursor.fetchone()
        conn.close()
        return Admin(*row) if row else None

    def get_admin_by_username(self, username):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Admin WHERE Username = %s", (username,))
        row = cursor.fetchone()
        conn.close()
        return Admin(*row) if row else None

    def register_admin(self, admin):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Admin (AdminID, FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (admin.admin_id, admin.first_name, admin.last_name, admin.email, admin.phone_number,
              admin.username, admin.password, admin.role, admin.join_date))
        admin.admin_id = cursor.lastrowid  # <-- THIS IS IMPORTANT

        conn.commit()
        conn.close()

    def update_admin(self, admin):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Admin SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s,
            Username=%s, Password=%s, Role=%s, JoinDate=%s WHERE AdminID=%s
        """, (admin.first_name, admin.last_name, admin.email, admin.phone_number,
              admin.username, admin.password, admin.role, admin.join_date, admin.admin_id))
        conn.commit()
        conn.close()

    def delete_admin(self, admin_id):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Admin WHERE AdminID = %s", (admin_id,))
        conn.commit()
        conn.close()

    def authenticate(self, username, password):
        try:
            conn = get_connection(self.config)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Admin WHERE Username = %s AND Password = %s", (username, password))
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            return Admin(*row) if row else None
        except Exception as e:
            raise DatabaseConnectionException(f"Error authenticating admin: {str(e)}")

    def get_reservation_history(self):
        conn = get_connection(self.config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Reservation")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_vehicle_utilization(self):
        conn = get_connection(self.config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT v.VehicleID, v.Make, v.Model,
                   SUM(DATEDIFF(r.EndDate, r.StartDate) + 1) AS DaysBooked,
                   ROUND(SUM(DATEDIFF(r.EndDate, r.StartDate) + 1) /
                   (DATEDIFF(CURDATE(), MIN(r.StartDate)) + 1) * 100, 2) AS UtilizationPercent
            FROM Vehicle v
            JOIN Reservation r ON v.VehicleID = r.VehicleID
            WHERE r.Status = 'Confirmed'
            GROUP BY v.VehicleID
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_revenue_summary(self):
        conn = get_connection(self.config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT DATE(StartDate) AS Date,
                   SUM(TotalCost) AS Revenue,
                   COUNT(*) AS BookingCount
            FROM Reservation
            WHERE Status IN ('Confirmed', 'Completed')
            GROUP BY DATE(StartDate)
            ORDER BY Date DESC
            LIMIT 30
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_top_vehicles_by_revenue(self):
        conn = get_connection(self.config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT v.VehicleID, v.Make, v.Model, SUM(r.TotalCost) AS TotalRevenue
            FROM Vehicle v
            JOIN Reservation r ON v.VehicleID = r.VehicleID
            WHERE r.Status IN ('Confirmed', 'Completed')
            GROUP BY v.VehicleID
            ORDER BY TotalRevenue DESC
            LIMIT 5
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_most_active_customers(self):
        conn = get_connection(self.config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT c.CustomerID, c.FirstName, c.LastName, COUNT(r.ReservationID) AS TotalBookings
            FROM Customer c
            JOIN Reservation r ON c.CustomerID = r.CustomerID
            GROUP BY c.CustomerID
            ORDER BY TotalBookings DESC
            LIMIT 5
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_least_utilized_vehicles(self):
        conn = get_connection(self.config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT v.VehicleID, v.Make, v.Model,
                   COALESCE(SUM(DATEDIFF(r.EndDate, r.StartDate) + 1), 0) AS DaysBooked
            FROM Vehicle v
            LEFT JOIN Reservation r ON v.VehicleID = r.VehicleID AND r.Status = 'Confirmed'
            GROUP BY v.VehicleID
            ORDER BY DaysBooked ASC
            LIMIT 5
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_monthly_revenue_trend(self):
        conn = get_connection(self.config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT DATE_FORMAT(StartDate, '%Y-%m') AS Month, 
                   SUM(TotalCost) AS MonthlyRevenue,
                   COUNT(*) AS TotalBookings
            FROM Reservation
            WHERE Status IN ('Confirmed', 'Completed')
            GROUP BY Month
            ORDER BY Month DESC
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_reservation_status_summary(self):
        conn = get_connection(self.config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT Status, COUNT(*) AS Count
            FROM Reservation
            GROUP BY Status
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_booking_by_weekday(self):
        conn = get_connection(self.config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT DAYNAME(StartDate) AS DayOfWeek, COUNT(*) AS TotalReservations
            FROM Reservation
            GROUP BY DayOfWeek
            ORDER BY TotalReservations DESC
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_inactive_customers(self):
        conn = get_connection(self.config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT c.CustomerID, c.FirstName, c.LastName, MAX(r.StartDate) AS LastBooking
            FROM Customer c
            LEFT JOIN Reservation r ON c.CustomerID = r.CustomerID
            GROUP BY c.CustomerID
            HAVING LastBooking IS NULL OR LastBooking < DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

