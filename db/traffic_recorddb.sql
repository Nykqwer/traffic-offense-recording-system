-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 24, 2024 at 03:03 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `traffic_recorddb`
--

-- --------------------------------------------------------

--
-- Table structure for table `record`
--

CREATE TABLE `record` (
  `id` int(100) NOT NULL,
  `d_name` varchar(50) NOT NULL,
  `d_license` int(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `p_no` int(12) NOT NULL,
  `email` varchar(50) NOT NULL,
  `v_reg` int(25) NOT NULL,
  `v_model` varchar(50) NOT NULL,
  `v_no` int(50) NOT NULL,
  `off_name` varchar(50) NOT NULL,
  `e_agency` varchar(50) NOT NULL,
  `offense` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `time` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `off_code` varchar(50) NOT NULL,
  `court_no` int(25) NOT NULL,
  `hearing_date` varchar(50) NOT NULL,
  `outcome` varchar(50) NOT NULL,
  `fines` varchar(50) NOT NULL,
  `payment` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `record`
--

INSERT INTO `record` (`id`, `d_name`, `d_license`, `address`, `p_no`, `email`, `v_reg`, `v_model`, `v_no`, `off_name`, `e_agency`, `offense`, `date`, `time`, `location`, `description`, `off_code`, `court_no`, `hearing_date`, `outcome`, `fines`, `payment`) VALUES
(2, 'asdasdad', 0, 'dsa123', 1231312, 'qewqew', 12312, 'qewe123', 21120, 'e1e21', '12e1e', 'ewqeqw', 'e2e', 'qweqweqe', '12e1', 'qweqwe', 'e21e21e', 0, '1231231', 'eqweqew', 'qweqe', '21312eqw'),
(3, 'zsc', 32, 'asd', 3213, 'asdq', 12312, 'eqw', 231, 'qwe21', 'qew', '1eqwqwe', '23', '123123', 'ewqqweq', '1231', 'eqw123', 3213, '1eqwq', '12312eqw', 'qweq', 'qweqwe'),
(4, 'qweewq', 2313131, '1231qweqweq', 12312313, '123eqeqweqew', 12312312, 'qweqqeqwe', 12100, 'qweq1qewqe', 'qweqe', '1231eqw', '123qew', 'qwe1', 'ewqe12', 'e1wq1', '12313', 1323, '12eqw', '12312', 'qwe1', 'qewqw');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`) VALUES
(1, 'admin', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `record`
--
ALTER TABLE `record`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `record`
--
ALTER TABLE `record`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
