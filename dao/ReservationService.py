from util.DBConnUtil import get_connection
from dao.IReservationService import IReservationService
from entity.Reservation import Reservation

class ReservationService(IReservationService):

    def __init__(self, config):
        self.config = config

    def get_reservation_by_id(self, reservation_id):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Reservation WHERE ReservationID = %s", (reservation_id,))
        row = cursor.fetchone()
        conn.close()
        return Reservation(*row) if row else None

    def get_reservations_by_customer_id(self, customer_id):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Reservation WHERE CustomerID = %s", (customer_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Reservation(*row) for row in rows]

    def create_reservation(self, reservation):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Reservation (ReservationID, CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (reservation.reservation_id, reservation.customer_id, reservation.vehicle_id,
              reservation.start_date, reservation.end_date, reservation.total_cost, reservation.status))
        conn.commit()
        conn.close()

    def update_reservation(self, reservation):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Reservation SET CustomerID=%s, VehicleID=%s, StartDate=%s, EndDate=%s,
            TotalCost=%s, Status=%s WHERE ReservationID=%s
        """, (reservation.customer_id, reservation.vehicle_id, reservation.start_date,
              reservation.end_date, reservation.total_cost, reservation.status,
              reservation.reservation_id))
        conn.commit()
        conn.close()

    def cancel_reservation(self, reservation_id):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Reservation WHERE ReservationID = %s", (reservation_id,))
        conn.commit()
        conn.close()
