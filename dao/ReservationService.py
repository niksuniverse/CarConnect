from util.DBConnUtil import get_connection
from dao.IReservationService import IReservationService
from entity.Reservation import Reservation
from datetime import datetime

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

        cursor.execute("SELECT DailyRate FROM Vehicle WHERE VehicleID = %s", (reservation.get_vehicle_id(),))
        result = cursor.fetchone()
        if not result:
            conn.close()
            raise ValueError("❌ Vehicle not found.")

        daily_rate = result[0]

        start = datetime.strptime(reservation.get_start_date(), "%Y-%m-%d")
        end = datetime.strptime(reservation.get_end_date(), "%Y-%m-%d")
        if end < start:
            conn.close()
            raise ValueError("❌ End date must be after start date.")

        days = (end - start).days + 1
        total_cost = days * daily_rate

        cursor.execute("""
            INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            reservation.get_customer_id(),
            reservation.get_vehicle_id(),
            reservation.get_start_date(),
            reservation.get_end_date(),
            total_cost,
            reservation.get_status()
        ))

        # Fetch the auto-generated ReservationID
        cursor.execute("SELECT LAST_INSERT_ID()")
        new_id = cursor.fetchone()[0]
        reservation.set_reservation_id(new_id)

        conn.commit()
        cursor.close()
        conn.close()

        print(f"\n✅ Reservation created successfully.")
        print(f"📌 Duration: {days} day(s)")
        print(f"💰 Total Cost: ₹{total_cost:.2f}")

    def update_reservation(self, reservation):
        conn = get_connection(self.config)
        cursor = conn.cursor()

        cursor.execute("SELECT DailyRate FROM Vehicle WHERE VehicleID = %s", (reservation.get_vehicle_id(),))
        result = cursor.fetchone()
        if not result:
            conn.close()
            raise ValueError("❌ Vehicle not found.")

        daily_rate = result[0]

        start = datetime.strptime(reservation.get_start_date(), "%Y-%m-%d")
        end = datetime.strptime(reservation.get_end_date(), "%Y-%m-%d")
        if end < start:
            conn.close()
            raise ValueError("❌ End date must be after start date.")

        days = (end - start).days + 1
        total_cost = days * daily_rate

        cursor.execute("""
            UPDATE Reservation
            SET CustomerID=%s, VehicleID=%s, StartDate=%s, EndDate=%s,
                TotalCost=%s, Status=%s
            WHERE ReservationID=%s
        """, (
            reservation.get_customer_id(), reservation.get_vehicle_id(),
            reservation.get_start_date(), reservation.get_end_date(),
            total_cost, reservation.get_status(), reservation.get_reservation_id()
        ))

        conn.commit()
        conn.close()

        print(f"\n Reservation updated successfully.")
        print(f" New Duration: {days} day(s)")
        print(f" New Total Cost: ₹{total_cost:.2f}")

    def cancel_reservation(self, reservation_id):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Reservation WHERE ReservationID = %s", (reservation_id,))
        conn.commit()
        conn.close()
        print("❌ Reservation cancelled successfully.")

