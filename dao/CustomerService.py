
import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='Nikitha@2003')
c=db.cursor()
from util.DBConnUtil import get_connection
from dao.ICustomerService import ICustomerService
from entity.Customer import Customer
from exception.InvalidInputException import InvalidInputException
from exception.DatabaseConnectionException import DatabaseConnectionException

class CustomerService(ICustomerService):

    def __init__(self, config):
        self.config = config

    def get_customer_by_id(self, customerID):
        try:
            conn = get_connection(self.config)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customer WHERE CustomerID = %s", (customerID,))
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            return Customer(*row) if row else None
        except Exception as e:
            raise DatabaseConnectionException(f"Error fetching customer by ID: {str(e)}")

    def get_customer_by_username(self, username):
        try:
            conn = get_connection(self.config)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customer WHERE Username = %s", (username,))
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            return Customer(*row) if row else None
        except Exception as e:
            raise DatabaseConnectionException(f"Error fetching customer by username: {str(e)}")

    def register_customer(self, customer):
        try:
            conn = get_connection(self.config)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Customer ( CustomerID, FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                 customer.customer_id, customer.first_name, customer.last_name, customer.email,
                customer.phone_number, customer.address, customer.username,
                customer.password, customer.registration_date
            ))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            raise DatabaseConnectionException(f"Error registering customer: {str(e)}")

    def update_customer(self, customer):
        try:
            conn = get_connection(self.config)
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Customer SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s, Address=%s,
                Username=%s, Password=%s, RegistrationDate=%s WHERE CustomerID=%s
            """, (
                customer.first_name, customer.last_name, customer.email, customer.phone_number,
                customer.address, customer.username, customer.password,
                customer.registration_date, customer.customer_id
            ))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            raise DatabaseConnectionException(f"Error updating customer: {str(e)}")

    def delete_customer(self, customerid):
        try:
            conn = get_connection(self.config)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Customer WHERE CustomerID = %s", (customerid,))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            raise DatabaseConnectionException(f"Error deleting customer: {str(e)}")
