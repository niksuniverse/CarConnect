import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from dao.CustomerService import CustomerService
from dao.VehicleService import VehicleService
from dao.ReservationService import ReservationService
from dao.AdminService import AdminService
from util.DBPropertyUtil import get_db_config
from entity.Customer import Customer
from entity.Vehicle import Vehicle
from entity.Reservation import Reservation
from entity.Admin import Admin

def main():
    config = get_db_config("C:/Users/Nikitha/CarConnect/db.properties")

    customer_service = CustomerService(config)
    vehicle_service = VehicleService(config)
    reservation_service = ReservationService(config)
    admin_service = AdminService(config)


    width = 170  # Adjust based on your terminal size

    while True:
        print("\n" + "=" * width)
        print("🚗🔧  Welcome to CarConnect - Main Menu  🔧🚗".center(width))
        print("=" * width)

        print("👥 Customer Management".center(width))
        print("👤 [1] Register New Customer".center(width))
        print("🔍 [2] View Customer by ID".center(width))
        print("🔑 [3] View Customer by Username".center(width))
        print("✏️  [4] Update Customer Details".center(width))
        print("❌ [5] Delete a Customer".center(width))

        print("─" * width)

        print("🚘 Vehicle Management".center(width))
        print("🚘 [6] Add a New Vehicle to Fleet".center(width))
        print("📋 [7] List All Available Vehicles".center(width))
        print("🔍 [8] View Vehicle Details by ID".center(width))
        print("✏️  [9] Update Vehicle Information".center(width))
        print("🗑️  [10] Remove a Vehicle".center(width))

        print("─" * width)

        print("📅 Reservation Management".center(width))
        print("📝 [11] Create a New Reservation".center(width))
        print("🔍 [12] View Reservation by ID".center(width))
        print("📚 [13] View Reservations by Customer ID".center(width))
        print("✏️  [14] Modify an Existing Reservation".center(width))
        print("❌ [15] Cancel a Reservation".center(width))

        print("─" * width)

        print("🛡️ Admin Operations".center(width))
        print("🛡️  [16] Register a New Admin".center(width))
        print("🚪 [17] Exit the Application".center(width))
        print("=" * width)



        choice = input("Enter your choice: ")

        if choice == '1':
            cid = int(input("Customer ID: "))
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            addr = input("Address: ")
            uname = input("Username: ")
            pwd = input("Password: ")
            reg_date = datetime.today().strftime('%Y-%m-%d')
            cust = Customer(cid, fname, lname, email, phone, addr, uname, pwd, reg_date)
            customer_service.register_customer(cust)
            print("✅ Customer registered successfully.")

        elif choice == '2':
            cid = int(input("Enter Customer ID: "))
            cust = customer_service.get_customer_by_id(cid)
            print(vars(cust) if cust else "❌ Customer not found.")

        elif choice == '3':
            uname = input("Enter Username: ")
            cust = customer_service.get_customer_by_username(uname)
            print(vars(cust) if cust else "❌ Customer not found.")
        elif choice == '4':
            cid = int(input("Customer ID to update: "))
            existing_cust = customer_service.get_customer_by_id(cid)

            if not existing_cust:
                print("❌ Customer not found. Cannot update.")
            else:
                fname = input(f"First Name [{existing_cust.first_name}]: ") or existing_cust.first_name
                lname = input(f"Last Name [{existing_cust.last_name}]: ") or existing_cust.last_name
                email = input(f"Email [{existing_cust.email}]: ") or existing_cust.email
                phone = input(f"Phone [{existing_cust.phone_number}]: ") or existing_cust.phone_number
                addr = input(f"Address [{existing_cust.address}]: ") or existing_cust.address
                uname = input(f"Username [{existing_cust.username}]: ") or existing_cust.username
                pwd = input(f"Password [{existing_cust.password}]: ") or existing_cust.password
                reg_date = existing_cust.registration_date  # Keep original

                updated_cust = Customer(cid, fname, lname, email, phone, addr, uname, pwd, reg_date)
                customer_service.update_customer(updated_cust)
                print("✏️ Customer updated successfully.")

        elif choice == '5':
            cid = int(input("Enter Customer ID to delete: "))
            customer_service.delete_customer(cid)
            print("🗑️ Customer deleted successfully.")

        elif choice == '6':
            vid = int(input("Vehicle ID: "))
            model = input("Model: ")
            make = input("Make: ")
            year = int(input("Year: "))
            color = input("Color: ")
            reg_num = input("Registration Number: ")
            avail = input("Available (yes/no): ").lower() == 'yes'
            rate = float(input("Daily Rate: "))
            vehicle = Vehicle(vid, model, make, year, color, reg_num, avail, rate)
            vehicle_service.add_vehicle(vehicle)
            print("✅ Vehicle added successfully.")

        elif choice == '7':
            vehicles = vehicle_service.get_available_vehicles()
            for v in vehicles:
                print(vars(v))

        elif choice == '8':
            vid = int(input("Enter Vehicle ID: "))
            v = vehicle_service.get_vehicle_by_id(vid)
            print(vars(v) if v else "❌ Vehicle not found.")

        elif choice == '9':
            vid = int(input("Vehicle ID to update: "))
            model = input("Model: ")
            make = input("Make: ")
            year = int(input("Year: "))
            color = input("Color: ")
            reg_num = input("Registration Number: ")
            avail = input("Available (yes/no): ").lower() == 'yes'
            rate = float(input("Daily Rate: "))
            vehicle = Vehicle(vid, model, make, year, color, reg_num, avail, rate)
            vehicle_service.update_vehicle(vehicle)
            print("✏️ Vehicle updated successfully.")

        elif choice == '10':
            vid = int(input("Enter Vehicle ID to remove: "))
            vehicle_service.remove_vehicle(vid)
            print("🗑️ Vehicle removed successfully.")

        elif choice == '11':
            rid = int(input("Reservation ID: "))
            cid = int(input("Customer ID: "))
            vid = int(input("Vehicle ID: "))
            start = input("Start Date (YYYY-MM-DD): ")
            end = input("End Date (YYYY-MM-DD): ")
            cost = float(input("Total Cost: "))
            status = input("Status (pending/confirmed): ")
            res = Reservation(rid, cid, vid, start, end, cost, status)
            reservation_service.create_reservation(res)
            print("📝 Reservation created.")

        elif choice == '12':
            rid = int(input("Enter Reservation ID: "))
            res = reservation_service.get_reservation_by_id(rid)
            print(vars(res) if res else "❌ Reservation not found.")

        elif choice == '13':
            cid = int(input("Enter Customer ID: "))
            reservations = reservation_service.get_reservations_by_customer_id(cid)
            if reservations:
                for res in reservations:
                    print(vars(res))
            else:
                print("❌ No reservations found for this customer.")

        elif choice == '14':
            rid = int(input("Reservation ID to update: "))
            cid = int(input("Customer ID: "))
            vid = int(input("Vehicle ID: "))
            start = input("Start Date (YYYY-MM-DD): ")
            end = input("End Date (YYYY-MM-DD): ")
            cost = float(input("Total Cost: "))
            status = input("Status (pending/confirmed): ")
            res = Reservation(rid, cid, vid, start, end, cost, status)
            reservation_service.update_reservation(res)
            print("✏️ Reservation updated.")

        elif choice == '15':
            rid = int(input("Enter Reservation ID to cancel: "))
            reservation_service.cancel_reservation(rid)
            print("❌ Reservation cancelled.")

        elif choice == '16':
            aid = int(input("Admin ID: "))
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            uname = input("Username: ")
            pwd = input("Password: ")
            role = input("Role: ")
            join_date = datetime.today().strftime('%Y-%m-%d')
            admin = Admin(aid, fname, lname, email, phone, uname, pwd, role, join_date)
            admin_service.register_admin(admin)
            print("✅ Admin registered successfully.")

        elif choice == '17':
            print("👋 Exiting CarConnect. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
