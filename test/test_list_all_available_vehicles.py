import unittest
from dao.VehicleService import VehicleService


class TestCarConnect(unittest.TestCase):

    def setUp(self):
        self.config = {
            "host": "localhost",
            "port": 3306,
            "database": "casestudy_db",
            "user": "root",
            "password": "Nikitha@2003"
        }
        self.vehicle_service = VehicleService(self.config)

    def test_get_all_vehicles(self):
        all_vehicles = self.vehicle_service.get_available_vehicles()
        self.assertIsInstance(all_vehicles, list)
        self.assertGreaterEqual(len(all_vehicles), 0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
