import sys
import os
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
from util.validation import is_valid_name, is_valid_email, is_valid_phone, is_valid_username, is_valid_password

def customer_login_menu(customer_service, vehicle_service, reservation_service):
    uname = input("Username: ")
    pwd = input("Password: ")
    cust = customer_service.authenticate(uname, pwd)
    if cust:
        print(f"✅ Welcome, {uname}!")

        customer_menu(customer_service, vehicle_service, reservation_service, cust)
    else:
        print("❌ Invalid username or password.")

def admin_login_menu(admin_service, customer_service, vehicle_service, reservation_service):
    uname = input("Username: ")
    pwd = input("Password: ")
    admin = admin_service.authenticate(uname, pwd)
    if admin:
        print(f"✅ Welcome Admin {admin.first_name}!")
        admin_menu(admin_service, customer_service, vehicle_service, reservation_service)
    else:
        print("❌ Invalid admin credentials.")


def customer_menu(customer_service, vehicle_service, reservation_service, current_customer):
    while True:
        print("\n📋 Customer Menu:")
        print(" [1] View My Details")
        print(" [2] Update My Details")
        print(" [3] Manage My Vehicles")
        print(" [4] Manage My Reservations")
        print(" [0] Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("✅ Customer Details:")
            for key, value in vars(current_customer).items():
                print(f"{key.capitalize()}: {value}")

        elif choice == '2':
            print("🔧 Update Your Details (press Enter to keep current values):")
            input("Press Enter to begin updating...")

            fname = input(f"First Name [{current_customer.first_name}]: ") or current_customer.first_name
            if not is_valid_name(fname): print("⚠️ Invalid first name."); fname = current_customer.first_name

            lname = input(f"Last Name [{current_customer.last_name}]: ") or current_customer.last_name
            if not is_valid_name(lname): print("⚠️ Invalid last name."); lname = current_customer.last_name

            email = input(f"Email [{current_customer.email}]: ") or current_customer.email
            if not is_valid_email(email): print("⚠️ Invalid email."); email = current_customer.email

            phone = input(f"Phone [{current_customer.phone_number}]: ") or current_customer.phone_number
            if not is_valid_phone(phone): print("⚠️ Invalid phone."); phone = current_customer.phone_number

            addr = input(f"Address [{current_customer.address}]: ") or current_customer.address

            uname = input(f"Username [{current_customer.username}]: ") or current_customer.username
            if not is_valid_username(uname): print("⚠️ Invalid username."); uname = current_customer.username

            pwd = input("Password (leave blank to keep current): ") or current_customer.password
            if not is_valid_password(pwd): print("⚠️ Weak password."); pwd = current_customer.password

            updated_cust = Customer(
                current_customer.customer_id, fname, lname, email,
                phone, addr, uname, pwd, current_customer.registration_date
            )
            customer_service.update_customer(updated_cust)
            current_customer = updated_cust
            print("✏️ Updated your details.")

        elif choice == '3':
            while True:
                print("\n🚘 Browse Vehicles:")
                print(" [1] View All Available Vehicles")
                print(" [2] Search Vehicle by Make or Model")
                print(" [3] View Vehicle Details by ID")
                print(" [0] Back to Customer Menu")
                vchoice = input("Enter your choice: ")

                if vchoice == '1':
                    vehicles = vehicle_service.get_available_vehicles()
                    if vehicles:
                        print("\n📋 Available Vehicles:")
                        for v in vehicles:
                            print(
                                f"ID: {v.vehicle_id} | {v.make} {v.model} ({v.year}) | ₹{v.daily_rate}/day | Available: {v.availability}")
                    else:
                        print("🚫 No available vehicles found.")

                elif vchoice == '2':
                    keyword = input("Enter Make or Model to search: ").lower()
                    vehicles = vehicle_service.get_available_vehicles()
                    matches = [v for v in vehicles if keyword in v.make.lower() or keyword in v.model.lower()]
                    if matches:
                        for v in matches:
                            print(f"ID: {v.vehicle_id} | {v.make} {v.model} ({v.year}) | ₹{v.daily_rate}/day")
                    else:
                        print("🚫 No matches found.")

                elif vchoice == '3':
                    vid = int(input("Enter Vehicle ID: "))
                    v = vehicle_service.get_vehicle_by_id(vid)
                    if v and v.availability:
                        print(f"\n🔍 Vehicle Details:")
                        for key, value in vars(v).items():
                            print(f"{key.replace('_', ' ').title()}: {value}")
                    else:
                        print("🚫 Vehicle not found or unavailable.")

                elif vchoice == '0':
                    break
                else:
                    print("⚠️ Invalid choice.")

        elif choice == '4':
            while True:
                print("\n📅 My Reservations:")
                print(" [1] Create Reservation")
                print(" [2] View My Reservations")
                print(" [3] Update Reservation")
                print(" [4] Cancel Reservation")
                print(" [0] Back to Customer Menu")
                rchoice = input("Enter your choice: ")

                if rchoice == '1':
                    vid = int(input("Vehicle ID: "))
                    st = input("From (YYYY-MM-DD): ")
                    en = input("To (YYYY-MM-DD): ")
                    stt = input("Status: ")
                    r = Reservation(None, current_customer.customer_id, vid, st, en, 0.0, stt)
                    reservation_service.create_reservation(r)
                    print(f"✅ Reservation created (ID {r.get_reservation_id()})")

                elif rchoice == '2':
                    rs = reservation_service.get_reservations_by_customer_id(current_customer.customer_id)
                    if rs:
                        for r in rs:
                            print("-" * 40)
                            for key, value in vars(r).items():
                                print(f"{key.replace('_', ' ').title()}: {value}")
                    else:
                        print("🚫 No reservations found.")

                elif rchoice == '3':
                    rid = int(input("Reservation ID: "))
                    r = reservation_service.get_reservation_by_id(rid)
                    if r and r.customer_id == current_customer.customer_id:
                        vid = int(input("Vehicle ID: "))
                        st = input(f"From [{r.start_date}]: ") or r.start_date
                        en = input(f"To [{r.end_date}]: ") or r.end_date
                        stt = input(f"Status [{r.status}]: ") or r.status
                        updated_r = Reservation(rid, current_customer.customer_id, vid, st, en, 0.0, stt)
                        reservation_service.update_reservation(updated_r)
                        print("✅ Reservation updated.")
                    else:
                        print("🚫 Reservation not found or access denied.")

                elif rchoice == '4':
                    rid = int(input("Reservation ID: "))
                    r = reservation_service.get_reservation_by_id(rid)
                    if r and r.customer_id == current_customer.customer_id:
                        reservation_service.cancel_reservation(rid)
                        print("❌ Reservation canceled.")
                    else:
                        print("🚫 Reservation not found or access denied.")

                elif rchoice == '0':
                    break

                else:
                    print("⚠️ Invalid choice.")

        elif choice == '0':
            print("👋 Logging out...")
            break

        else:
            print("⚠️ Invalid choice.")

from datetime import datetime

def admin_menu(admin_service, customer_service, vehicle_service, reservation_service):
    while True:
        print("\n👨‍💼 Admin Control Panel:")
        print(" [1] Manage Admins")
        print(" [2] Manage Customers")
        print(" [3] Manage Vehicles")
        print(" [4] Manage Reservations")
        print(" [5] View Reports")
        print(" [0] Exit to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            admin_management_menu(admin_service)
        elif choice == '2':
            print("\n📂 Entering Customer Management...")
            admin_customer_operations(customer_service)
        elif choice == '3':
            print("\n🚘 Entering Vehicle Management...")
            vehicle_menu(vehicle_service)
        elif choice == '4':
            print("\n📅 Entering Reservation Management...")
            reservation_menu(reservation_service)
        elif choice == '5':
            admin_reports_menu(admin_service)
        elif choice == '0':
            print("⬅️ Returning to Main Menu...")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

def admin_management_menu(admin_service):
    while True:
        print("\n🔐 Admin Management Menu:")
        print(" [1] Register New Admin")
        print(" [2] View Admin by ID")
        print(" [3] View Admin by Username")
        print(" [4] Delete Admin")
        print(" [0] Back to Admin Panel")

        sub_choice = input("Choose an option: ")

        if sub_choice == '1':
            while True:
                fname = input("First Name: ")
                if is_valid_name(fname): break
                print("❌ Invalid first name.")

            while True:
                lname = input("Last Name: ")
                if is_valid_name(lname): break
                print("❌ Invalid last name.")

            while True:
                email = input("Email: ")
                if is_valid_email(email): break
                print("❌ Invalid email format.")

            while True:
                phone = input("Phone (10 digits): ")
                if is_valid_phone(phone): break
                print("❌ Invalid phone number.")

            while True:
                uname = input("Username: ")
                if is_valid_username(uname): break
                print("❌ Invalid username.")

            while True:
                pwd = input("Password: ")
                if is_valid_password(pwd): break
                print("❌ Password too weak.")

            role = input("Role (e.g. Manager): ")
            join_date = datetime.today().strftime('%Y-%m-%d')

            admin = Admin(None, fname, lname, email, phone, uname, pwd, role, join_date)
            admin_service.register_admin(admin)
            print("✅ Admin registered.")
            print(f"✅ Admin created with ID: {admin.admin_id}")

        elif sub_choice == '2':
            admin_id = int(input("Enter Admin ID: "))
            admin = admin_service.get_admin_by_id(admin_id)
            if admin:
                print("\n🧾 Admin Details:")
                for key, value in vars(admin).items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
            else:
                print("❌ Admin not found.")

        elif sub_choice == '3':
            username = input("Username: ")
            admin = admin_service.get_admin_by_username(username)
            if admin:
                print("\n🧾 Admin Details:")
                for key, value in vars(admin).items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
            else:
                print("❌ Admin not found.")

        elif sub_choice == '4':
            aid = int(input("Admin ID to delete: "))
            admin_service.delete_admin(aid)
            print("🗑️ Admin deleted.")

        elif sub_choice == '0':
            break
        else:
            print("⚠️ Invalid choice. Try again.")

def admin_reports_menu(admin_service):
    while True:
        print("\n📊 Admin Reports Menu:")
        print(" [1] Top Vehicles by Revenue")
        print(" [2] Most Active Customers")
        print(" [3] Vehicle Least Utilization")
        print(" [4] Monthly Revenue Trend")
        print(" [5] Reservation Status Summary")
        print(" [6] Booking Trend by Weekday")
        print(" [7] Inactive Customers")
        print(" [8] Reservation History")
        print(" [9] Vehicle Utilization")
        print(" [0] Back to Admin Menu")

        report_choice = input("Choose report to view: ")

        if report_choice == '1':
            data = admin_service.get_top_vehicles_by_revenue()
            print("\n🚗 Top Revenue-Generating Vehicles:")
            for row in data:
                print(f"Vehicle ID: {row['VehicleID']}, Make: {row['Make']}, Model: {row['Model']}, Revenue: ₹{row['TotalRevenue']}")

        elif report_choice == '2':
            data = admin_service.get_most_active_customers()
            print("\n👥 Most Active Customers:")
            for row in data:
                print(f"Customer ID: {row['CustomerID']}, Name: {row['FirstName']} {row['LastName']}, Total Bookings: {row['TotalBookings']}")

        elif report_choice == '3':
            data = admin_service.get_least_utilized_vehicles()
            print("\n📉 Least Utilized Vehicles:")
            for row in data:
                print(f"Vehicle ID: {row['VehicleID']}, Make: {row['Make']}, Model: {row['Model']}, Days Booked: {row['DaysBooked']}")

        elif report_choice == '4':
            data = admin_service.get_monthly_revenue_trend()
            print("\n📅 Monthly Revenue Trend:")
            for row in data:
                print(f"Month: {row['Month']}, Revenue: ₹{row['MonthlyRevenue']}, Bookings: {row['TotalBookings']}")

        elif report_choice == '5':
            data = admin_service.get_reservation_status_summary()
            print("\n📌 Reservation Status Summary:")
            for row in data:
                print(f"Status: {row['Status']}, Count: {row['Count']}")

        elif report_choice == '6':
            data = admin_service.get_booking_by_weekday()
            print("\n📆 Bookings by Day of Week:")
            for row in data:
                print(f"{row['DayOfWeek']}: {row['TotalReservations']} bookings")

        elif report_choice == '7':
            data = admin_service.get_inactive_customers()
            print("\n😴 Inactive Customers (6+ months):")
            for row in data:
                print(f"Customer ID: {row['CustomerID']}, Name: {row['FirstName']} {row['LastName']}, Last Booking: {row['LastBooking']}")

        elif report_choice == '8':
            data = admin_service.get_reservation_history()
            print("\n📜 Reservation History:")
            for r in data:
                print(f"Reservation ID: {r['ReservationID']}, CustomerID: {r['CustomerID']}, VehicleID: {r['VehicleID']}, "
                      f"Start: {r['StartDate']}, End: {r['EndDate']}, Total Cost: ₹{r['TotalCost']}, Status: {r['Status']}")

        elif report_choice == '9':
            data = admin_service.get_vehicle_utilization()
            print("\n🚘 Vehicle Utilization:")
            for v in data:
                print(f"Vehicle ID: {v['VehicleID']}, Days Booked: {v['DaysBooked']}, Utilization: {v['UtilizationPercent']}%")

        elif report_choice == '0':
            break
        else:
            print("⚠️ Invalid choice. Try again.")



def admin_customer_operations(customer_service):
    while True:
        print("\n👥 Admin - Manage Customers:")
        print(" [1] List All Customers")
        print(" [2] View Customer by ID")
        print(" [3] Update Customer")
        print(" [4] Delete Customer")
        print(" [0] Back to Admin Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            customers = customer_service.list_all_customers()
            for c in customers:
                print(f"ID: {c.customer_id}, Name: {c.first_name} {c.last_name}, Email: {c.email}, Username: {c.username}")

        elif choice == '2':
            cid = input("Enter Customer ID: ")
            customer = customer_service.get_customer_by_id(cid)
            if customer:
                print("\n✅ Customer Details:")
                for key, value in vars(customer).items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
            else:
                print("❌ Customer not found.")

        elif choice == '3':
            cid = input("Enter Customer ID to update: ")
            customer = customer_service.get_customer_by_id(cid)
            if customer:
                fname = input(f"First Name [{customer.first_name}]: ") or customer.first_name
                if not is_valid_name(fname): fname = customer.first_name

                lname = input(f"Last Name [{customer.last_name}]: ") or customer.last_name
                if not is_valid_name(lname): lname = customer.last_name

                email = input(f"Email [{customer.email}]: ") or customer.email
                if not is_valid_email(email): email = customer.email

                phone = input(f"Phone [{customer.phone_number}]: ") or customer.phone_number
                if not is_valid_phone(phone): phone = customer.phone_number

                addr = input(f"Address [{customer.address}]: ") or customer.address

                uname = input(f"Username [{customer.username}]: ") or customer.username
                if not is_valid_username(uname): uname = customer.username

                pwd = input("Password (leave blank to keep current): ") or customer.password
                if not is_valid_password(pwd): pwd = customer.password

                updated_customer = Customer(customer.customer_id, fname, lname, email, phone, addr, uname, pwd, customer.registration_date)
                customer_service.update_customer(updated_customer)
                print("✅ Customer updated successfully.")
            else:
                print("❌ Customer not found.")

        elif choice == '4':
            cid = input("Enter Customer ID to delete: ")
            confirm = input("Are you sure? This action cannot be undone (yes/no): ").lower()
            if confirm == 'yes':
                customer_service.delete_customer(cid)
                print("🗑️ Customer deleted.")
            else:
                print("Action cancelled.")

        elif choice == '0':
            break

        else:
            print("⚠️ Invalid choice. Try again.")

def vehicle_menu(vehicle_service):
    while True:
        print("\n🚘 Vehicle Management:")
        print(" [1] Add Vehicle")
        print(" [2] View All Vehicles")
        print(" [3] View Vehicle by ID")
        print(" [4] Update Vehicle")
        print(" [5] Delete Vehicle")
        print(" [0] Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            m = input("Make: "); mo = input("Model: ")
            yr = int(input("Year: ")); col = input("Color: ")
            reg = input("Reg. plate: "); av = input("Available? (yes/no): ").lower() == 'yes'
            rate = float(input("Daily rate: "))
            v = Vehicle(None, m, mo, yr, col, reg, av, rate)
            vehicle_service.add_vehicle(v)
            print(f"✅ Vehicle added (ID {v.vehicle_id})")

        elif choice == '2':
            vs = vehicle_service.get_available_vehicles()
            for v in vs:
                print(f"| ID:{v.vehicle_id} {v.make}-{v.model}, ₹{v.daily_rate}, Available:{v.availability}")

        elif choice == '3':
            vid = int(input("Vehicle ID: "))
            v = vehicle_service.get_vehicle_by_id(vid)
            if v:
                print("\n🚘 Vehicle Details:")
                print("-" * 40)
                for key, value in vars(v).items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
            else:
                print("❌ Vehicle not found.")

        elif choice == '4':
            vid = int(input("Vehicle ID: "))
            m = input("Make: "); mo = input("Model: ")
            yr = int(input("Year: ")); col = input("Color: ")
            reg = input("Reg. plate: "); av = input("Available? (yes/no): ").lower() == 'yes'
            rate = float(input("Daily rate: "))
            v = Vehicle(vid, m, mo, yr, col, reg, av, rate)
            vehicle_service.update_vehicle(v)
            print("✅ Vehicle updated.")

        elif choice == '5':
            vid = int(input("Vehicle ID: "))
            vehicle_service.remove_vehicle(vid)
            print("🗑️ Vehicle deleted.")

        elif choice == '0':
            break

        else:
            print("⚠️ Invalid choice.")

def reservation_menu(reservation_service):
    while True:
        print("\n📅 Reservation Management:")
        print(" [1] Create Reservation")
        print(" [2] View by Reservation ID")
        print(" [3] View by Customer ID")
        print(" [4] Update Reservation")
        print(" [5] Cancel Reservation")
        print(" [0] Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            cid = int(input("Customer ID: ")); vid = int(input("Vehicle ID: "))
            st = input("From (YYYY-MM-DD): "); en = input("To (YYYY-MM-DD): ")
            stt = input("Status: ")
            r = Reservation(None, cid, vid, st, en, 0.0, stt)
            reservation_service.create_reservation(r)
            print(f"✅ Reservation created (ID {r.get_reservation_id()})")

        elif choice == '2':
            rid = int(input("Reservation ID: "))
            r = reservation_service.get_reservation_by_id(rid)
            if r:
                print("✅ Reservation Details:")
                for key, value in vars(r).items():
                    print(f"{key.capitalize()}: {value}")
            else:
                print("❌ Not found.")

        elif choice == '3':
            cid = int(input("Customer ID: "))
            rs = reservation_service.get_reservations_by_customer_id(cid)
            if rs:
                print("\n📄 Reservation(s) Found:")
                for r in rs:
                    print("-" * 40)
                    for key, value in vars(r).items():
                        print(f"{key.replace('_', ' ').title()}: {value}")
            else:
                print("❌ No reservations found for this customer.")

        elif choice == '4':
            rid = int(input("Res ID: ")); cid = int(input("Customer ID: "))
            vid = int(input("Vehicle ID: "))
            st = input("From (YYYY-MM-DD): "); en = input("To (YYYY-MM-DD): ")
            stt = input("Status: ")
            r = Reservation(rid, cid, vid, st, en, 0.0, stt)
            reservation_service.update_reservation(r)
            print("✅ Updated Reservation.")

        elif choice == '5':
            rid = int(input("Reservation ID: "))
            reservation_service.cancel_reservation(rid)
            print("❌ Reservation canceled.")

        elif choice == '0':
            break

        else:
            print("⚠️ Invalid choice.")



def main():
    config = get_db_config("C:/Users/Nikitha/CarConnect/db.properties")
    customer_service = CustomerService(config)
    vehicle_service = VehicleService(config)
    reservation_service = ReservationService(config)
    admin_service = AdminService(config)

    width = 50
    while True:
        print("=" * width)
        print("🚗🔧  Welcome to CarConnect - Main Menu  🔧🚗".center(width))
        print("=" * width)

        print("[1] Create Customer")
        print("[2] Create Admin")
        print("[3] Login as Customer")
        print("[4] Login as Admin")
        print("[5] Exit Application")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            while True:
                fname = input("First Name: ")
                if is_valid_name(fname): break
                print("❌ Invalid first name.")

            while True:
                lname = input("Last Name: ")
                if is_valid_name(lname): break
                print("❌ Invalid last name.")

            while True:
                email = input("Email: ")
                if is_valid_email(email): break
                print("❌ Invalid email format.")

            while True:
                phone = input("Phone (10 digits): ")
                if is_valid_phone(phone): break
                print("❌ Invalid phone number.")

            addr = input("Address: ")

            while True:
                uname = input("Username: ")
                if is_valid_username(uname): break
                print("❌ Invalid username.")

            while True:
                pwd = input("Password: ")
                if is_valid_password(pwd): break
                print("❌ Password too weak.")

            reg_date = datetime.today().strftime('%Y-%m-%d')
            cust = Customer(None, fname, lname, email, phone, addr, uname, pwd, reg_date)
            customer_service.register_customer(cust)
            print(f"✅ Customer created with ID: {cust.customer_id}")

        elif choice == '2':
            admin_menu(admin_service, customer_service, vehicle_service, reservation_service)

        elif choice == '3':

            customer_login_menu(customer_service, vehicle_service, reservation_service)

        elif choice == '4':
            admin_login_menu(admin_service, customer_service, vehicle_service, reservation_service)

        elif choice == '5':
            print("🚪 Exiting CarConnect Application")
            print("Thanks for visiting !!")
            break

        else:
            print("⚠️ Invalid choice. Please select a valid option.")


if __name__ == '__main__':
    main()


