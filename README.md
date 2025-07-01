# 📄 `mainmodule.py` - Application Entry Point for CarConnect

This file serves as the **core menu-driven entry point** of the CarConnect car rental system. It handles **user interaction**, invokes services, and navigates between customer/admin functionalities.

---

## 🔧 What This File Does

- Provides a **command-line interface** for customers and admins.
- Collects and validates **user input**.
- Routes requests to services in the `dao/` layer.
- Manages menu navigation, login, registration, and CRUD operations.
- Displays outputs like vehicle listings, customer profiles, and reports.

---

## 🧑‍💻 Roles and Functionalities

### 👤 Customer

#### 1. Register
- Enters first name, last name, email, phone number, address, username, and password.
- All fields go through **validation** (`validation.py`) such as:
  - Valid name (alphabets only)
  - Valid email format
  - Phone number length (10 digits)
  - Strong password (with special characters)
  - Unique username

#### 2. Login
- Enters username and password.
- Verified via `CustomerService.authenticate()`.

#### 3. Customer Menu Options

Once logged in:
- `View My Details`: Displays all profile info pulled from the DB.
- `Update My Details`: Editable fields with inline validation.
- `Manage My Vehicles`:
  - View all available vehicles.
  - Search vehicles by make/model.
  - View full vehicle info by ID.
- `Manage My Reservations`:
  - Create a reservation (Vehicle ID, From/To Date, Status).
  - View all reservations.
  - Update reservation details.
  - Cancel reservation.

---

### 👨‍💼 Admin

#### 1. Register Admin (via main menu)
- Only accessible through menu option `[2] Create Admin`.
- Similar validation and input as customer.

#### 2. Login as Admin
- Verified via `AdminService.authenticate()`.

#### 3. Admin Control Panel

Options include:
- `Manage Admins`: Add, view by ID or username, delete.
- `Manage Customers`: View all, view by ID, update, or delete.
- `Manage Vehicles`: Add, view, update, delete.
- `Manage Reservations`: Create, view by ID or customer, update, cancel.
- `View Reports`:
  - Top Vehicles by Revenue
  - Most Active Customers
  - Least Utilized Vehicles
  - Monthly Revenue Trend
  - Status Summary of Reservations
  - Booking Trends by Day of Week
  - Inactive Customers (no booking in 6+ months)
  - Full Reservation History
  - Vehicle Utilization %

---

## ✅ Input Validations Used (from `validation.py`)

| Field | Validation |
|-------|------------|
| First/Last Name | Only alphabets |
| Email | Regex pattern |
| Phone | 10-digit number |
| Username | No special characters, unique |
| Password | Minimum length + special characters |

---

## 📦 External Modules Used

- `datetime` – for handling registration/join/reservation dates.
- `sys.path` – to import services from other folders like `dao`, `entity`, `util`.
- `os` – for dynamic file path access to `db.properties`.

---

## 🔄 Application Flow Summary

```text
mainmodule.py
↓
Main Menu
│
├── [1] Create Customer → Customer object created → DB insert via CustomerService
├── [2] Create Admin → Admin object created → DB insert via AdminService
├── [3] Login as Customer
│     └── On success → Customer Menu → vehicle/reservation features
├── [4] Login as Admin
│     └── On success → Admin Control Panel → manage all resources
└── [5] Exit Application


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
├── db.properties
└── README.md

```
