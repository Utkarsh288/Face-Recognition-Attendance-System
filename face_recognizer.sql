-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 18, 2022 at 11:43 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognizer`
--

-- --------------------------------------------------------

--
-- Table structure for table `stdattendance`
--

CREATE TABLE `stdattendance` (
  `std_id` varchar(45) NOT NULL,
  `std_roll_no` varchar(45) NOT NULL,
  `std_dep` varchar(45) NOT NULL,
  `std_name` varchar(45) NOT NULL,
  `std_time` varchar(45) NOT NULL,
  `std_date` varchar(45) NOT NULL,
  `std_attendance` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stdattendance`
--

INSERT INTO `stdattendance` (`std_id`, `std_roll_no`, `std_dep`, `std_name`, `std_time`, `std_date`, `std_attendance`) VALUES
('5', '1914416', ' Utkarsh Kumar Singh', ' Computer', ' 12:20:07', ' 12/11/2022', ' Present');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `Dep` varchar(45) NOT NULL,
  `course` varchar(45) NOT NULL,
  `Year` varchar(45) NOT NULL,
  `Semester` varchar(45) NOT NULL,
  `Student_id` varchar(45) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Division` varchar(45) NOT NULL,
  `Roll` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `Dob` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Phone` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `Teacher` varchar(45) NOT NULL,
  `PhotoSample` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`Dep`, `course`, `Year`, `Semester`, `Student_id`, `Name`, `Division`, `Roll`, `Gender`, `Dob`, `Email`, `Phone`, `Address`, `Teacher`, `PhotoSample`) VALUES
('IT', 'TE', '2023-24', 'Semester-1', '1235', 'florentia', 'E2', '02', 'Female', '12322', '123@gmail.com', '1234567890', 'dryhgyhnflkn', 'kakashi sensei', 'Yes'),
('IT', 'FE', '2020-21', 'Semester-2', '33', 'Raju', 'B1', '1914416', 'Male', '28/08/2001', 'raju123@gmail.com', '924984923314', 'aisfiejfiidmsfnihgkljbgis', 'Monsun', 'No'),
('Computer', 'SE', '2022-23', 'Semester-1', '5', 'Utkarsh Kumar Singh', 'A1', '1914416', 'Male', '28/08/2001', 'utka@gmail.com', '48832484298', 'idifusfnks', 'asufhsf', 'Yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `stdattendance`
--
ALTER TABLE `stdattendance`
  ADD PRIMARY KEY (`std_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`Student_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
