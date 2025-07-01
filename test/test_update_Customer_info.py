import unittest
from datetime import datetime
from entity.Customer import Customer
from dao.CustomerService import CustomerService

class TestUpdateCustomer(unittest.TestCase):

    def setUp(self):
        self.config = {
            "host": "localhost",
            "port": 3306,
            "database": "casestudy_db",
            "user": "root",
            "password": "Nikitha@2003"
        }
        self.customer_service = CustomerService(self.config)

    def test_update_customer_information(self):
        # Step 1: Fetch existing customer
        original_customer = self.customer_service.get_customer_by_id(13)
        self.assertIsNotNone(original_customer)

        # Step 2: Modify details (simulate user update)
        updated_customer = Customer(
            customer_id=original_customer.customer_id,
            first_name=original_customer.first_name,
            last_name=original_customer.last_name,
            email="varun_updated@gmail.com",  # updated email
            phone_number="9876543210",         # updated phone
            address=original_customer.address,
            username=original_customer.username,
            password=original_customer.password,
            registration_date=original_customer.registration_date
        )

        # Step 3: Perform update
        self.customer_service.update_customer(updated_customer)

        # Step 4: Fetch again and verify
        fetched_customer = self.customer_service.get_customer_by_id(13)
        self.assertEqual(fetched_customer.email, "varun_updated@gmail.com")
        self.assertEqual(fetched_customer.phone_number, "9876543210")

    def tearDown(self):
        pass
    def test_update_customer_tina(self):
        updated_customer = Customer(
            customer_id=16,
            first_name="Tina",
            last_name="Bose",
            email="tina.updated@example.com",          # updated email
            phone_number="+91-9999999916",              # updated phone number
            address="Kolkata",
            username="tina1",
            password="pass16",
            registration_date=datetime(2024, 6, 16)
        )

        self.customer_service.update_customer(updated_customer)

        fetched_customer = self.customer_service.get_customer_by_id(16)

        self.assertEqual(fetched_customer.email, "tina.updated@example.com")
        self.assertEqual(fetched_customer.phone_number, "+91-9999999916")

    def tearDown(self):
        # Optional: Reset to original values if needed
        original_customer = Customer(
            customer_id=16,
            first_name="Tina",
            last_name="Bose",
            email="tina@example.com",
            phone_number="+91-9000000016",
            address="Kolkata",
            username="tina1",
            password="pass16",
            registration_date=datetime(2024, 6, 16)
        )
        self.customer_service.update_customer(original_customer)

if __name__ == '__main__':
    unittest.main()
