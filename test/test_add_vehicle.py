import unittest
from dao.VehicleService import VehicleService
from entity.Vehicle import Vehicle


class TestAddVehicle(unittest.TestCase):

    def setUp(self):
        self.config = {
            "host": "localhost",
            "port": 3306,
            "database": "casestudy_db",
            "user": "root",
            "password": "Nikitha@2003"
        }
        self.vehicle_service = VehicleService(self.config)

    def test_add_new_vehicle(self):
        test_vehicle_id = 9999
        test_registration_number = "TEST9999_UNIQUE"

        new_vehicle = Vehicle(
            vehicle_id=test_vehicle_id,
            model="Sedan",
            make="Hyundai",
            year=2023,
            color="Red",
            registration_number=test_registration_number,
            availability=True,
            daily_rate=2000.00
        )

        self.vehicle_service.add_vehicle(new_vehicle)

        added_vehicle = self.vehicle_service.get_vehicle_by_id(test_vehicle_id)

        self.assertIsNotNone(added_vehicle)
        self.assertEqual(added_vehicle.model, "Sedan")
        self.assertEqual(added_vehicle.make, "Hyundai")
        self.assertEqual(added_vehicle.year, 2023)
        self.assertEqual(added_vehicle.color, "Red")
        self.assertEqual(added_vehicle.registration_number, test_registration_number)
        self.assertEqual(added_vehicle.availability, True)
        self.assertEqual(added_vehicle.daily_rate, 2000.00)

    def tearDown(self):
        try:
            self.vehicle_service.remove_vehicle(9999)
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()
