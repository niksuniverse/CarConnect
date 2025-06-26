
-- Create the database
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

-- Indexes for performance
CREATE INDEX IDX_Customer_Username ON Customer(Username);
CREATE INDEX IDX_Customer_Email ON Customer(Email);
CREATE INDEX IDX_Admin_Username ON Admin(Username);
CREATE INDEX IDX_Admin_Email ON Admin(Email);
CREATE INDEX IDX_Reservation_CustomerID ON Reservation(CustomerID);
CREATE INDEX IDX_Reservation_VehicleID ON Reservation(VehicleID);
SELECT * FROM customer;
SELECT * FROM admin;
SELECT * FROM reservation;
SELECT * FROM vehicle;

use casestudy_db;
-- Customer Table
INSERT INTO Customer (CustomerID, FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
VALUES
(1, 'Ravi', 'Sharma', 'ravi1@example.com', '+91-9000000001', 'Delhi', 'ravi1', 'pass1', '2024-06-01'),
(2, 'Priya', 'Verma', 'priya1@example.com', '+91-9000000002', 'Delhi', 'priya1', 'pass2', '2024-06-02'),
(3, 'Amit', 'Kumar', 'amit1@example.com', '+91-9000000003', 'Mumbai', 'amit1', 'pass3', '2024-06-03'),
(4, 'Neha', 'Joshi', 'neha1@example.com', '+91-9000000004', 'Mumbai', 'neha1', 'pass4', '2024-06-04'),
(5, 'Karan', 'Singh', 'karan1@example.com', '+91-9000000005', 'Bangalore', 'karan1', 'pass5', '2024-06-05'),
(6, 'Simran', 'Patel', 'simran1@example.com', '+91-9000000006', 'Chennai', 'simran1', 'pass6', '2024-06-06'),
(7, 'Arjun', 'Yadav', 'arjun1@example.com', '+91-9000000007', 'Hyderabad', 'arjun1', 'pass7', '2024-06-07'),
(8, 'Pooja', 'Rao', 'pooja1@example.com', '+91-9000000008', 'Hyderabad', 'pooja1', 'pass8', '2024-06-08'),
(9, 'Rahul', 'Kapoor', 'rahul1@example.com', '+91-9000000009', 'Pune', 'rahul1', 'pass9', '2024-06-09'),
(10, 'Sneha', 'Shah', 'sneha1@example.com', '+91-9000000010', 'Pune', 'sneha1', 'pass10', '2024-06-10'),
(11, 'Manish', 'Chopra', 'manish@example.com', '+91-9000000011', 'Delhi', 'manish1', 'pass11', '2024-06-11'),
(12, 'Anita', 'Gupta', 'anita@example.com', '+91-9000000012', 'Delhi', 'anita1', 'pass12', '2024-06-12'),
(13, 'Varun', 'Mehta', 'varun@example.com', '+91-9000000013', 'Mumbai', 'varun1', 'pass13', '2024-06-13'),
(14, 'Riya', 'Jain', 'riya@example.com', '+91-9000000014', 'Mumbai', 'riya1', 'pass14', '2024-06-14'),
(15, 'Deepak', 'Desai', 'deepak@example.com', '+91-9000000015', 'Chennai', 'deepak1', 'pass15', '2024-06-15'),
(16, 'Tina', 'Bose', 'tina@example.com', '+91-9000000016', 'Kolkata', 'tina1', 'pass16', '2024-06-16'),
(17, 'Rohit', 'Nair', 'rohit@example.com', '+91-9000000017', 'Kochi', 'rohit1', 'pass17', '2024-06-17'),
(18, 'Meena', 'Das', 'meena@example.com', '+91-9000000018', 'Delhi', 'meena1', 'pass18', '2024-06-18'),
(19, 'Sanjay', 'Reddy', 'sanjay@example.com', '+91-9000000019', 'Hyderabad', 'sanjay1', 'pass19', '2024-06-19'),
(20, 'Divya', 'Naik', 'divya@example.com', '+91-9000000020', 'Pune', 'divya1', 'pass20', '2024-06-20');


INSERT INTO Vehicle (VehicleID, Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
VALUES(1, 'SUV', 'Toyota', 2022, 'Black', 'MH01AA1001', TRUE, 2500),
(2, 'SUV', 'Toyota', 2023, 'Black', 'MH01AA1002', TRUE, 2600),
(3, 'SUV', 'Mahindra', 2022, 'White', 'MH01AA1003', TRUE, 2550),
(4, 'Sedan', 'Honda', 2023, 'Red', 'DL02BB2001', TRUE, 2000),
(5, 'Sedan', 'Honda', 2023, 'Red', 'DL02BB2002', TRUE, 2050),
(6, 'Sedan', 'Hyundai', 2022, 'Blue', 'DL02BB2003', TRUE, 2100),
(7, 'Hatchback', 'Maruti', 2021, 'Gray', 'KA03CC3001', TRUE, 1500),
(8, 'Hatchback', 'Maruti', 2021, 'Gray', 'KA03CC3002', TRUE, 1550),
(9, 'Hatchback', 'Hyundai', 2022, 'White', 'KA03CC3003', TRUE, 1600),
(10, 'SUV', 'Ford', 2022, 'Black', 'MH04DD4001', TRUE, 2700),
(11, 'SUV', 'Ford', 2023, 'Black', 'MH04DD4002', TRUE, 2750),
(12, 'SUV', 'Toyota', 2022, 'White', 'MH04DD4003', TRUE, 2500),
(13, 'Sedan', 'Hyundai', 2023, 'Blue', 'DL05EE5001', TRUE, 2150),
(14, 'Sedan', 'Hyundai', 2023, 'Blue', 'DL05EE5002', TRUE, 2200),
(15, 'Sedan', 'Tesla', 2023, 'White', 'DL05EE5003', TRUE, 2400),
(16, 'Hatchback', 'Nissan', 2022, 'Gray', 'KA06FF6001', TRUE, 1700),
(17, 'Hatchback', 'Nissan', 2021, 'Gray', 'KA06FF6002', TRUE, 1650),
(18, 'Hatchback', 'Volkswagen', 2022, 'Blue', 'KA06FF6003', TRUE, 1800),
(19, 'SUV', 'Kia', 2022, 'Black', 'MH07GG7001', TRUE, 2600),
(20, 'SUV', 'Kia', 2023, 'Black', 'MH07GG7002', TRUE, 2650);


INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status) VALUES
(1, 1, '2024-07-01 10:00:00', '2024-07-05 10:00:00', 10000.00, 'confirmed'),
(2, 3, '2024-07-02 09:00:00', '2024-07-04 09:00:00', 5100.00, 'pending'),
(3, 5, '2024-07-03 14:00:00', '2024-07-07 14:00:00', 8200.00, 'confirmed'),
(4, 2, '2024-07-04 08:00:00', '2024-07-06 08:00:00', 5200.00, 'cancelled'),
(5, 4, '2024-07-05 12:00:00', '2024-07-10 12:00:00', 10000.00, 'confirmed'),
(6, 6, '2024-07-06 16:00:00', '2024-07-08 16:00:00', 4200.00, 'pending'),
(7, 7, '2024-07-07 11:00:00', '2024-07-10 11:00:00', 4500.00, 'confirmed'),
(8, 8, '2024-07-08 09:30:00', '2024-07-12 09:30:00', 6200.00, 'confirmed'),
(9, 9, '2024-07-09 13:00:00', '2024-07-11 13:00:00', 3200.00, 'confirmed'),
(10, 10, '2024-07-10 07:00:00', '2024-07-15 07:00:00', 13500.00, 'pending'),
(11, 11, '2024-07-11 15:00:00', '2024-07-13 15:00:00', 5500.00, 'confirmed'),
(12, 12, '2024-07-12 10:30:00', '2024-07-14 10:30:00', 5200.00, 'cancelled'),
(13, 13, '2024-07-13 08:45:00', '2024-07-17 08:45:00', 8600.00, 'confirmed'),
(14, 14, '2024-07-14 09:15:00', '2024-07-16 09:15:00', 4400.00, 'pending'),
(15, 15, '2024-07-15 14:30:00', '2024-07-20 14:30:00', 12000.00, 'confirmed'),
(16, 16, '2024-07-16 17:00:00', '2024-07-18 17:00:00', 3400.00, 'confirmed'),
(17, 17, '2024-07-17 11:15:00', '2024-07-19 11:15:00', 3300.00, 'confirmed'),
(18, 18, '2024-07-18 13:20:00', '2024-07-22 13:20:00', 7200.00, 'pending'),
(19, 19, '2024-07-19 10:50:00', '2024-07-21 10:50:00', 5200.00, 'cancelled'),
(20, 20, '2024-07-20 12:00:00', '2024-07-25 12:00:00', 14500.00, 'confirmed');

INSERT INTO Admin (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate) VALUES
('Anil','Mehta','anil.mehta@example.com','+91-9000001001','anilmehta','adminpass1','manager','2024-01-05 09:00:00'),
('Sunita','Roy','sunita.roy@example.com','+91-9000001002','sunitaroy','adminpass2','staff','2024-01-10 10:30:00'),
('Rahul','Sharma','rahul.sharma@example.com','+91-9000001003','rahulsharma','adminpass3','manager','2024-02-01 11:15:00'),
('Priya','Sen','priya.sen@example.com','+91-9000001004','priyasen','adminpass4','staff','2024-02-15 12:45:00'),
('Vikram','Patel','vikram.patel@example.com','+91-9000001005','vikrampatel','adminpass5','staff','2024-03-01 14:00:00'),
('Neha','Das','neha.das@example.com','+91-9000001006','nehadas','adminpass6','manager','2024-03-10 15:20:00'),
('Rohit','Khan','rohit.khan@example.com','+91-9000001007','rohitkhan','adminpass7','staff','2024-03-20 16:10:00'),
('Deepa','Nair','deepa.nair@example.com','+91-9000001008','deepanair','adminpass8','staff','2024-04-01 09:30:00'),
('Manish','Verma','manish.verma@example.com','+91-9000001009','manishverma','adminpass9','manager','2024-04-05 10:50:00'),
('Tina','Rao','tina.rao@example.com','+91-9000001010','tinarao','adminpass10','staff','2024-04-15 11:40:00'),
('Arjun','Singh','arjun.singh@example.com','+91-9000001011','arjunsingh','adminpass11','staff','2024-05-01 13:05:00'),
('Meena','Kumar','meena.kumar@example.com','+91-9000001012','meenakumar','adminpass12','manager','2024-05-10 14:25:00'),
('Sandeep','Chopra','sandeep.chopra@example.com','+91-9000001013','sandeepchopra','adminpass13','staff','2024-05-20 15:35:00'),
('Riya','Jain','riya.jain@example.com','+91-9000001014','riyajain','adminpass14','staff','2024-06-01 08:45:00'),
('Amit','Desai','amit.desai@example.com','+91-9000001015','amitdesai','adminpass15','manager','2024-06-05 09:55:00'),
('Simran','Gill','simran.gill@example.com','+91-9000001016','simrangill','adminpass16','staff','2024-06-10 10:15:00'),
('Karan','Kapoor','karan.kapoor@example.com','+91-9000001017','karankapoor','adminpass17','staff','2024-06-15 11:25:00'),
('Tina','Shah','tina.shah@example.com','+91-9000001018','tinashah','adminpass18','manager','2024-06-20 12:35:00'),
('Rohini','Iyer','rohini.iyer@example.com','+91-9000001019','rohiniiyer','adminpass19','staff','2024-06-22 13:45:00'),
('Ajay','Reddy','ajay.reddy@example.com','+91-9000001020','ajayreddy','adminpass20','staff','2024-06-25 14:55:00');

SELECT * FROM customer;
SELECT * FROM admin;
SELECT * FROM reservation;
SELECT * FROM vehicle;