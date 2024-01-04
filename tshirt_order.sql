-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 05:14 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tshirt_order`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_order_details`
--

CREATE TABLE `user_order_details` (
  `Full_Name` text NOT NULL,
  `Phone_Num` varchar(11) NOT NULL,
  `Sleeve_Type` text NOT NULL,
  `Size` varchar(4) NOT NULL,
  `Quantity` int(3) NOT NULL,
  `Total_Price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_order_details`
--

INSERT INTO `user_order_details` (`Full_Name`, `Phone_Num`, `Sleeve_Type`, `Size`, `Quantity`, `Total_Price`) VALUES
('Nurul Binti Arman ', '01158309673', 'Long Sleeve', 'L', 3, 150),
('Dania Binti Zaidy', '01920084091', 'Long Sleeve', 'M', 8, 360),
('Rayyan Bin Mikail', '01937690883', 'Short Sleeve', 'XL', 2, 90),
('Amri Bin Amsyar', '01983944981', 'Short Sleeve', 'M', 7, 283.5);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
