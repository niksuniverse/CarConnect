from util.DBConnUtil import get_connection
from dao.IVehicleService import IVehicleService
from entity.Vehicle import Vehicle

class VehicleService(IVehicleService):

    def __init__(self, config):
        self.config = config

    def get_vehicle_by_id(self, vehicle_id):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Vehicle WHERE VehicleID = %s", (vehicle_id,))
        row = cursor.fetchone()
        conn.close()
        return Vehicle(*row) if row else None

    def get_available_vehicles(self):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Vehicle WHERE Availability = TRUE")
        rows = cursor.fetchall()
        conn.close()
        return [Vehicle(*row) for row in rows]

    def add_vehicle(self, vehicle):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (vehicle.model, vehicle.make, vehicle.year, vehicle.color,
              vehicle.registration_number, vehicle.availability, vehicle.daily_rate))

        conn.commit()

        # Get the auto-generated VehicleID from the database
        vehicle.vehicle_id = cursor.lastrowid

        cursor.close()
        conn.close()

    def update_vehicle(self, vehicle):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Vehicle SET Model=%s, Make=%s, Year=%s, Color=%s,
            RegistrationNumber=%s, Availability=%s, DailyRate=%s WHERE VehicleID=%s
        """, (vehicle.model, vehicle.make, vehicle.year, vehicle.color, vehicle.registration_number,
              vehicle.availability, vehicle.daily_rate, vehicle.vehicle_id))
        conn.commit()
        conn.close()

    def remove_vehicle(self, vehicle_id):
        conn = get_connection(self.config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Vehicle WHERE VehicleID = %s", (vehicle_id,))
        conn.commit()
        conn.close()