# 🚗 CarConnect - Car Rental Platform

Welcome to **CarConnect**, a comprehensive car rental platform built using **Python** and **MySQL**. The application supports customer and admin functionalities, including secure login, vehicle management, reservation processing, and rich reporting features. It is structured following clean architecture principles with separation of concerns through packages like `entity`, `dao`, `util`, `exception`, and `main`.

---

## 📁 Project Structure
'''
CarConnect/
├── dao/
│ ├── CustomerService.py
│ ├── ICustomerService.py
│ ├── VehicleService.py
│ ├── IVehicleService.py
│ ├── ReservationService.py
│ ├── IReservationService.py
│ ├── AdminService.py
│ ├── IAdminService.py
│
├── entity/
│ ├── Customer.py
│ ├── Vehicle.py
│ ├── Reservation.py
│ ├── Admin.py
│
├── util/
│ ├── DBConnUtil.py
│ ├── DBPropertyUtil.py
│ ├── validation.py
│
├── exception/
│ ├── AuthenticationException.py
│ ├── ReservationException.py
│ ├── VehicleNotFoundException.py
│ ├── AdminNotFoundException.py
│ ├── InvalidInputException.py
│ ├── DatabaseConnectionException.py
│
├── main/
│ ├── mainmodule.py
│
├── db.properties
└── README.md
'''

---

## ⚙️ Technologies Used

- **Language:** Python 3
- **Database:** MySQL Workbench
- **Testing:** `unittest`
- **IDE:** PyCharm/VS Code
- **Package Management:** Virtual Environment (`.venv`)

---

## 📌 Key Features

### 🔐 User Authentication
- Separate login for **Customers** and **Admins**
- Validation and exception handling for credentials

### 🚘 Vehicle Management
- Add, update, view, and delete vehicles
- Search vehicles by make/model
- Filter available vehicles

### 📅 Reservation System
- Real-time reservation creation and cancellation
- Conflict detection and cost calculation
- Tracks status: `pending`, `confirmed`, `completed`, `cancelled`

### 🧑‍💼 Admin Control Panel
- Admin can manage other admins, customers, vehicles, and reservations
- Supports CRUD operations on all entities

### 📊 Reports & Analytics
- Top revenue-generating vehicles
- Most active customers
- Least utilized vehicles
- Monthly revenue trends
- Booking trends by weekday
- Inactive customers
- Reservation status summary
- Full reservation history

---

## 🧱 Database Schema

1. **Customer Table**
   - `CustomerID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `Address`, `Username`, `Password`, `RegistrationDate`

2. **Vehicle Table**
   - `VehicleID`, `Model`, `Make`, `Year`, `Color`, `RegistrationNumber`, `Availability`, `DailyRate`

3. **Reservation Table**
   - `ReservationID`, `CustomerID`, `VehicleID`, `StartDate`, `EndDate`, `TotalCost`, `Status`

4. **Admin Table**
   - `AdminID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `Username`, `Password`, `Role`, `JoinDate`

---

## 🚧 Exception Handling

Defined custom exceptions to ensure robust error reporting:

- `AuthenticationException`
- `ReservationException`
- `VehicleNotFoundException`
- `AdminNotFoundException`
- `InvalidInputException`
- `DatabaseConnectionException`

---

## 🧪 Unit Testing

Implemented unit tests for all major functionalities using `unittest`.

**Example test cases:**
- Invalid customer/admin login
- Adding and updating vehicles
- Fetching available vehicles
- Creating and canceling reservations

---
