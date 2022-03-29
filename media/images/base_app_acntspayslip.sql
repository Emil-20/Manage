-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 05, 2022 at 12:06 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `accountsint`
--

-- --------------------------------------------------------

--
-- Table structure for table `base_app_acntspayslip`
--

CREATE TABLE `base_app_acntspayslip` (
  `id` bigint(20) NOT NULL,
  `basic_salary` int(11) NOT NULL,
  `eno` varchar(100) NOT NULL,
  `hra` int(11) NOT NULL,
  `conveyns` varchar(100) NOT NULL,
  `tax` int(11) NOT NULL,
  `incentives` int(11) NOT NULL,
  `fromdate` date DEFAULT NULL,
  `todate` date DEFAULT NULL,
  `taxengine` varchar(100) NOT NULL,
  `incometax` int(11) NOT NULL,
  `uan` varchar(100) NOT NULL,
  `pf` int(11) NOT NULL,
  `esi` varchar(100) NOT NULL,
  `pro` varchar(100) NOT NULL,
  `leavesno` int(11) NOT NULL,
  `pr_acnt` varchar(200) NOT NULL,
  `pr_tax` int(11) NOT NULL,
  `delay` int(11) NOT NULL,
  `dateef` date DEFAULT NULL,
  `department_id` bigint(20) DEFAULT NULL,
  `designation_id` bigint(20) DEFAULT NULL,
  `user_id_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `base_app_acntspayslip`
--
ALTER TABLE `base_app_acntspayslip`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_acntspaysli_department_id_21ada824_fk_base_app_` (`department_id`),
  ADD KEY `base_app_acntspaysli_designation_id_00bcb706_fk_base_app_` (`designation_id`),
  ADD KEY `base_app_acntspaysli_user_id_id_fce5649e_fk_base_app_` (`user_id_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `base_app_acntspayslip`
--
ALTER TABLE `base_app_acntspayslip`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `base_app_acntspayslip`
--
ALTER TABLE `base_app_acntspayslip`
  ADD CONSTRAINT `base_app_acntspaysli_department_id_21ada824_fk_base_app_` FOREIGN KEY (`department_id`) REFERENCES `base_app_department` (`id`),
  ADD CONSTRAINT `base_app_acntspaysli_designation_id_00bcb706_fk_base_app_` FOREIGN KEY (`designation_id`) REFERENCES `base_app_designation` (`id`),
  ADD CONSTRAINT `base_app_acntspaysli_user_id_id_fce5649e_fk_base_app_` FOREIGN KEY (`user_id_id`) REFERENCES `base_app_user_registration` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
