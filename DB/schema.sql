-- Create the database
CREATE DATABASE casestudy_db;

-- Use the database
CREATE DATABASE IF NOT EXISTS casestudy_db;
USE casestudy_db;

-- Customer Table
CREATE TABLE Customer (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Username VARCHAR(50) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    RegistrationDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Vehicle Table
CREATE TABLE Vehicle (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,
    Model VARCHAR(50) NOT NULL,
    Make VARCHAR(50) NOT NULL,
    Year INT NOT NULL,
    Color VARCHAR(20),
    RegistrationNumber VARCHAR(20) NOT NULL UNIQUE,
    Availability BOOLEAN NOT NULL DEFAULT TRUE,
    DailyRate DECIMAL(10,2) NOT NULL
);

-- Reservation Table
CREATE TABLE Reservation (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    VehicleID INT NOT NULL,
    StartDate DATETIME NOT NULL,
    EndDate DATETIME NOT NULL,
    TotalCost DECIMAL(10,2) NOT NULL,
    Status VARCHAR(20) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID)
);

-- Admin Table
CREATE TABLE Admin (
    AdminID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15) NOT NULL,
    Username VARCHAR(50) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    Role VARCHAR(50) NOT NULL,
    JoinDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX IDX_Customer_Username ON Customer(Username);
CREATE INDEX IDX_Customer_Email ON Customer(Email);
CREATE INDEX IDX_Admin_Username ON Admin(Username);
CREATE INDEX IDX_Admin_Email ON Admin(Email);
CREATE INDEX IDX_Reservation_CustomerID ON Reservation(CustomerID);
CREATE INDEX IDX_Reservation_VehicleID ON Reservation(VehicleID);

-- Alter foreign keys to add cascade delete
ALTER TABLE Reservation DROP FOREIGN KEY Reservation_ibfk_1;
ALTER TABLE Reservation DROP FOREIGN KEY Reservation_ibfk_2;

ALTER TABLE Reservation
ADD CONSTRAINT fk_customer
FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE;

ALTER TABLE Reservation
ADD CONSTRAINT fk_vehicle
FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID) ON DELETE CASCADE;

-- Check constraint for date validation
ALTER TABLE Reservation
ADD CONSTRAINT chk_dates CHECK (StartDate <= EndDate);

-- Use database again (optional)
USE casestudy_db;

-- Insert sample customers (Tamil names)
INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
VALUES 
('Ahana', 'Sri', 'ahanasri@gmail.com', '9876543210', 'Chennai', 'ahana_Sri', 'Ahana123', NOW()),
('Divya', 'Kumar', 'divya.kumar@gmail.com', '9876501234', 'Coimbatore', 'divya_kumar', 'Divya123', NOW());
('Lavanya', 'Devi', 'lavak123@gmail.com', '9876540001', 'Trichy', 'Lavanya', 'lava123', NOW()),
('Pooja', 'Kumar', 'poojakumar@gmail.com', '9876540002', 'Salem', 'pooja', 'pooja123', NOW()),
('Sathya', 'Dev', 'sathyadev@gmail.com', '9876540003', 'Madurai', 'sathya123', 'sat123', NOW()),
('ifa', 'irfan', 'fairf@gmail.com', '9876540004', 'Erode', 'ifa_if', 'ifa123', NOW()),
('Nikirtha', 'Sri', 'nikirtha123@gmail.com', '9876540005', 'Karur', 'nikir123', 'nikir123', NOW());

-- Insert sample vehicles
INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
VALUES
('Swift', 'Maruti', 2020, 'Red', 'TN01AB1234', TRUE, 1500.00),
('Baleno', 'Maruti', 2019, 'Blue', 'TN02CD5678', TRUE, 1600.00),
('i20', 'Hyundai', 2021, 'Black', 'TN03EF9012', TRUE, 1700.00),
('Kwid', 'Renault', 2018, 'White', 'TN04GH3456', TRUE, 2500.00),
('Innova', 'Toyota', 2020, 'Silver', 'TN05IJ7890', TRUE, 3000.00),
('Fortuner', 'Toyota', 2021, 'Grey', 'TN06KL2345', TRUE, 4000.00),
('Dzire', 'Maruti', 2019, 'White', 'TN07MN6789', TRUE, 1400.00),
('Duster', 'Nissan', 2020, 'Black', 'TN08OP1234', TRUE, 1800.00),
('Ertiga', 'Maruti', 2018, 'Blue', 'TN09QR5678', TRUE, 2200.00),
('City', 'Honda', 2021, 'Red', 'TN10ST9012', TRUE, 2600.00);

-- Insert sample reservations using customer IDs and vehicles
INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
VALUES
(1, 1, '2025-07-01 09:00:00', '2025-07-03 09:00:00', 1500*3, 'Confirmed'),
(1, 2, '2025-07-05 10:00:00', '2025-07-07 10:00:00', 1600*3, 'Confirmed'),
(1, 3, '2025-07-10 08:00:00', '2025-07-12 08:00:00', 1700*3, 'Cancelled'),
(2, 4, '2025-07-02 09:00:00', '2025-07-04 09:00:00', 2500*3, 'Confirmed'),
(2, 5, '2025-07-06 10:00:00', '2025-07-08 10:00:00', 3000*3, 'Completed'),
(2, 6, '2025-07-09 08:00:00', '2025-07-11 08:00:00', 4000*3, 'Confirmed'),
(1, 7, '2025-07-12 09:00:00', '2025-07-14 09:00:00', 1400*3, 'Confirmed'),
(2, 8, '2025-07-15 10:00:00', '2025-07-17 10:00:00', 1800*3, 'Confirmed'),
(1, 9, '2025-07-18 08:00:00', '2025-07-20 08:00:00', 2200*3, 'Confirmed'),
(2, 10, '2025-07-21 09:00:00', '2025-07-23 09:00:00', 2600*3, 'Confirmed');

INSERT INTO Admin (AdminID, FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
VALUES 
(1, 'Shifana', 'Banu', 'shifana.banu@carconnect.com', '9876500101', 'shifana_b', 'adminshifa', 'admin', '2025-06-25 00:00:00'),
(2, 'Varshini', 'tamil', 'varshini.tam@carconnect.com', '9876500102', 'varshini_s', 'adminvarshu', 'admin', '2025-06-26 00:00:00'),
(3, 'Gurumeeta', 'harii', 'gurumeeta.h@carconnect.com', '9876500103', 'guru_m', 'adminguru', 'superadmin', '2025-06-27 00:00:00'),
(4, 'Nikitha', 'Yuvaraj', 'nikithays06@carconnect.com', '9361312840', 'niksuniverse', 'adminnik', 'admin', '2025-06-30 00:00:00'),

-- View data (optional)
SELECT * FROM Customer;
SELECT * FROM Admin;
SELECT * FROM Reservation;
SELECT * FROM Vehicle;
