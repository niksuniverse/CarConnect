# 🚗 CarConnect Application

**CarConnect** is a Python-based Car Rental Management System designed to simplify and digitalize the entire car rental process for both customers and administrators. This project simulates a real-world rental platform, integrating user-friendly menus, secure authentication, vehicle and reservation handling, and performance analytics, all backed by a MySQL relational database.

This system allows:
- **Customers** to register, search available vehicles, book or cancel reservations, and manage their profile.
- **Admins** to control every module: customer accounts, vehicles, reservations, and detailed reporting for business insights.

The system is developed using modular architecture with clear separation of concerns via packages:
- `entity/` for models  
- `dao/` for database services  
- `util/` for helper utilities  
- `exception/` for custom errors  
- `main/` for UI flow and entry point

---

# 📄 `mainmodule.py` - Application Entry Point for CarConnect

This file serves as the **core menu-driven entry point** of the CarConnect system. It handles user interaction, invokes services, and navigates between customer and admin functionalities.

---

## 🔧 What This File Does

- Provides a **command-line interface** for customers and admins.
- Collects and validates user input.
- Routes requests to services in the `dao/` layer.
- Manages menu navigation, login, registration, and CRUD operations.
- Displays outputs like vehicle listings, customer profiles, and reports.

---

## 🧑‍💻 Roles and Functionalities

### 👤 Customer

#### 1. Register
- Inputs: First name, last name, email, phone number, address, username, and password.
- Validated through `validation.py`:
  - Names should contain only alphabets.
  - Valid email format required.
  - Phone number must be 10 digits.
  - Password must include special characters.
  - Username must be unique.

#### 2. Login
- Authenticates credentials via `CustomerService.authenticate()`.

#### 3. After Login - Customer Menu
- **View My Details**  
- **Update My Details**
- **Manage My Vehicles**
  - View all available vehicles.
  - Search by make or model.
  - View vehicle details by ID.
- **Manage My Reservations**
  - Create reservation.
  - View existing reservations.
  - Update reservation details.
  - Cancel reservation.

---

### 👨‍💼 Admin

#### 1. Register Admin
- Similar to customer registration (via menu option).

#### 2. Login
- Authenticates via `AdminService.authenticate()`.

#### 3. Admin Dashboard
- **Manage Admins**
  - Add, view, delete admins.
- **Manage Customers**
  - View, update, delete customers.
- **Manage Vehicles**
  - Add, view, update, delete vehicles.
- **Manage Reservations**
  - Create, view by ID/customer, update, cancel.
- **Reports**
  - Top Revenue Vehicles
  - Most Active Customers
  - Least Utilized Vehicles
  - Monthly Revenue Trend
  - Status Summary
  - Booking Trends by Day
  - Inactive Customers
  - Reservation History
  - Vehicle Utilization %

---

## ✅ Input Validations Used (via `validation.py`)

| Field           | Validation                            |
|----------------|----------------------------------------|
| First/Last Name| Only alphabets                         |
| Email          | Valid regex format                     |
| Phone Number   | Must be 10 digits                      |
| Username       | Unique, no special characters          |
| Password       | Minimum length + special characters    |

---

## 📦 External Modules Used

- `datetime` – for handling dates (reservations, registration, etc.)
- `sys.path` – to import services and utility modules
- `os` – to manage file paths and connect to `db.properties`

---

## 🧱 Database Tables and Details

**1. Customer Table:** CustomerID (PK), FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate  
**2. Admin Table:** AdminID (PK), FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate  
**3. Vehicle Table:** VehicleID (PK), Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate  
**4. Reservation Table:** ReservationID (PK), CustomerID (FK), VehicleID (FK), StartDate, EndDate, TotalCost, Status

---

## 🔄 Application Flow Summary

```text
CarConnect/
├── dao/
│   ├── CustomerService.py
│   ├── ICustomerService.py
│   ├── VehicleService.py
│   ├── IVehicleService.py
│   ├── ReservationService.py
│   ├── IReservationService.py
│   ├── AdminService.py
│   ├── IAdminService.py
│
├── entity/
│   ├── Customer.py
│   ├── Vehicle.py
│   ├── Reservation.py
│   ├── Admin.py
│
├── util/
│   ├── DBConnUtil.py
│   ├── DBPropertyUtil.py
│   ├── validation.py
│
├── exception/
│   ├── AuthenticationException.py
│   ├── ReservationException.py
│   ├── VehicleNotFoundException.py
│   ├── AdminNotFoundException.py
│   ├── InvalidInputException.py
│   ├── DatabaseConnectionException.py
│
├── main/
│   ├── mainmodule.py
│
├── test/
│   ├── test_add_vehicle.py
│   ├── test_list_all_available_vehicles.py
│   ├── test_update_Customer_info.py
|
├── DB/
│   ├── Schema.sql
|
├── db.properties
└── README.md
```

---

## 🛠️ Technologies Used

- **Language:** Python 3  
- **Database:** MySQL Workbench  
- **IDE:** PyCharm  
- **Version Control:** Git & GitHub  
- **Architecture:** Modular (DAO, Entity, Exception, Util, Main)  
- **Database Connector:** MySQL Connector for Python  
- **Testing:** unittest

---

## 🙌 Acknowledgements

This project was completed as part of the **Python foundational training** training at **Hexavarsity** by **Hexaware Technologies**.  
Special thanks to our mentor **Mr. Munna Pandey** and all reviewers for their guidance and support throughout the project journey.

---

## 👩‍💻 Author

**Nikitha Y S**  
🎓 B.Tech Artificial Intelligence and Data Science  
💼 Graduate Engineer Trainee @ Hexaware Technologies  

📧 Email: [nikithays06@gmail.com](mailto:nikithays06@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/nikithays](https://www.linkedin.com/in/nikitha-y-s-6b129223a/)  
💻 GitHub: [github.com/niksuniverse](https://github.com/niksuniverse)
