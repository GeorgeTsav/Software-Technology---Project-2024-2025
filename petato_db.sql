-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 24, 2025 at 10:06 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `petato_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `announcements`
--

CREATE TABLE `announcements` (
  `ann_id` int(11) NOT NULL,
  `ann_title` varchar(40) NOT NULL,
  `ann_type` enum('ADOPTION','HOST','','') NOT NULL,
  `ann_pet` enum('CAT','DOG') NOT NULL,
  `adopt_description` varchar(150) DEFAULT NULL,
  `host_start_date` date DEFAULT NULL,
  `host_end_date` date DEFAULT NULL,
  `ann_user` varchar(20) NOT NULL DEFAULT 'unknown',
  `ann_date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `announcements`
--

INSERT INTO `announcements` (`ann_id`, `ann_title`, `ann_type`, `ann_pet`, `adopt_description`, `host_start_date`, `host_end_date`, `ann_user`, `ann_date`) VALUES
(1, 'Dog Adoption!', 'ADOPTION', 'DOG', 'Beautifull Little Dog!', NULL, NULL, 'george_tsavos', '2025-05-23 11:04:03'),
(2, 'Cat Hosting', 'HOST', 'CAT', 'I can host cats only because i am alergic to dogs :).', '2025-05-31', '2025-06-18', 'george_tsavos', '2025-05-23 11:05:11'),
(3, 'Cat Adoption', 'ADOPTION', 'CAT', 'CATTTTTTt', NULL, NULL, 'george_tsavos', '2025-05-24 10:49:25');

-- --------------------------------------------------------

--
-- Table structure for table `appointments`
--

CREATE TABLE `appointments` (
  `app_id` int(11) NOT NULL,
  `app_vet` int(11) NOT NULL,
  `app_date` datetime NOT NULL,
  `app_type` enum('RESERVED','FREE','','') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `eshop_items`
--

CREATE TABLE `eshop_items` (
  `item_name` varchar(15) NOT NULL DEFAULT 'unknown',
  `item_quantity` int(11) NOT NULL,
  `item_decription` text NOT NULL,
  `item_price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `eshop_payments`
--

CREATE TABLE `eshop_payments` (
  `payment_id` int(11) NOT NULL,
  `payment_item` varchar(15) NOT NULL DEFAULT 'unknown',
  `payment_user` varchar(20) NOT NULL DEFAULT 'unknown',
  `payment_date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `interested_users`
--

CREATE TABLE `interested_users` (
  `int_user` varchar(20) NOT NULL DEFAULT 'unknown',
  `int_ann` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `interested_users`
--

INSERT INTO `interested_users` (`int_user`, `int_ann`) VALUES
('giwrgos1', 3),
('giwrgos2', 1),
('giwrgos2', 2);

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `msg_id` int(11) NOT NULL,
  `msg_date` datetime NOT NULL DEFAULT current_timestamp(),
  `msg_sender` varchar(20) NOT NULL DEFAULT 'SYSTEM',
  `msg_receiver` varchar(20) NOT NULL DEFAULT 'unknown',
  `msg_text` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`msg_id`, `msg_date`, `msg_sender`, `msg_receiver`, `msg_text`) VALUES
(2, '2025-05-24 11:05:28', 'System', 'giwrgos2', 'You have been approved by the owner of the announcement 1.');

-- --------------------------------------------------------

--
-- Table structure for table `my_appointments`
--

CREATE TABLE `my_appointments` (
  `my_app_id` int(11) NOT NULL,
  `my_app_user` varchar(20) NOT NULL DEFAULT 'unknown',
  `my_app_date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `personal_diary`
--

CREATE TABLE `personal_diary` (
  `per_diary_date` date NOT NULL DEFAULT current_timestamp(),
  `per_diary_user` varchar(20) NOT NULL DEFAULT 'unknown',
  `per_diary_text` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `personal_diary`
--

INSERT INTO `personal_diary` (`per_diary_date`, `per_diary_user`, `per_diary_text`) VALUES
('2025-04-10', 'george_tsavos', 'ssfsfs'),
('2025-05-01', 'george_tsavos', ''),
('2025-05-05', 'george_tsavos', 'znbnzm'),
('2025-05-08', 'george_tsavos', 'PAME LIGO'),
('2025-05-14', 'george_tsavos', ''),
('2025-05-15', 'george_tsavos', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
('2025-05-16', 'george_tsavos', '!!!'),
('2025-05-27', 'george_tsavos', 'adadadad');

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `rev_id` int(11) NOT NULL,
  `rev_date` datetime NOT NULL DEFAULT current_timestamp(),
  `rev_text` varchar(100) DEFAULT NULL,
  `rev_score` enum('1','2','3','4','5') NOT NULL,
  `rev_writer` varchar(20) NOT NULL,
  `rev_user` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(20) NOT NULL DEFAULT 'unknown',
  `name` varchar(20) NOT NULL DEFAULT 'unknown',
  `last_name` varchar(20) NOT NULL DEFAULT 'unknown',
  `telephone` varchar(10) NOT NULL DEFAULT 'unknown',
  `password` varchar(15) NOT NULL DEFAULT 'unknown'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `name`, `last_name`, `telephone`, `password`) VALUES
('george_tsavos', 'George', 'Tsavos', '6969696969', '1084606'),
('giwrgos1', 'George', 'Tsav', '6969696969', '1084606'),
('giwrgos2', 'George', 'Tsava', '6969696969', '1084606'),
('SYSTEM', 'unknown', 'unknown', 'unknown', 'unknown');

-- --------------------------------------------------------

--
-- Table structure for table `vet`
--

CREATE TABLE `vet` (
  `vet_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL DEFAULT 'unknown',
  `last_name` varchar(20) NOT NULL DEFAULT 'unknown',
  `telephone` varchar(10) NOT NULL DEFAULT 'unknown',
  `vet_clinic` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `announcements`
--
ALTER TABLE `announcements`
  ADD PRIMARY KEY (`ann_id`),
  ADD KEY `ann_user` (`ann_user`);

--
-- Indexes for table `appointments`
--
ALTER TABLE `appointments`
  ADD PRIMARY KEY (`app_id`),
  ADD KEY `app_vet` (`app_vet`);

--
-- Indexes for table `eshop_items`
--
ALTER TABLE `eshop_items`
  ADD PRIMARY KEY (`item_name`);

--
-- Indexes for table `eshop_payments`
--
ALTER TABLE `eshop_payments`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `payment_user` (`payment_user`),
  ADD KEY `payments_item` (`payment_item`);

--
-- Indexes for table `interested_users`
--
ALTER TABLE `interested_users`
  ADD PRIMARY KEY (`int_user`,`int_ann`),
  ADD KEY `int_ann` (`int_ann`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`msg_id`),
  ADD KEY `msg_sender` (`msg_sender`),
  ADD KEY `msg_receiver` (`msg_receiver`);

--
-- Indexes for table `my_appointments`
--
ALTER TABLE `my_appointments`
  ADD KEY `app_id` (`my_app_id`),
  ADD KEY `app_user` (`my_app_user`);

--
-- Indexes for table `personal_diary`
--
ALTER TABLE `personal_diary`
  ADD PRIMARY KEY (`per_diary_date`,`per_diary_user`),
  ADD KEY `per_diary_user` (`per_diary_user`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`rev_id`),
  ADD KEY `rev_writer` (`rev_writer`),
  ADD KEY `rev_user` (`rev_user`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `vet`
--
ALTER TABLE `vet`
  ADD PRIMARY KEY (`vet_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `announcements`
--
ALTER TABLE `announcements`
  MODIFY `ann_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `appointments`
--
ALTER TABLE `appointments`
  MODIFY `app_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `eshop_payments`
--
ALTER TABLE `eshop_payments`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `msg_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
  MODIFY `rev_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `vet`
--
ALTER TABLE `vet`
  MODIFY `vet_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `announcements`
--
ALTER TABLE `announcements`
  ADD CONSTRAINT `ann_user` FOREIGN KEY (`ann_user`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `appointments`
--
ALTER TABLE `appointments`
  ADD CONSTRAINT `app_vet` FOREIGN KEY (`app_vet`) REFERENCES `vet` (`vet_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `eshop_payments`
--
ALTER TABLE `eshop_payments`
  ADD CONSTRAINT `payment_user` FOREIGN KEY (`payment_user`) REFERENCES `user` (`username`),
  ADD CONSTRAINT `payments_item` FOREIGN KEY (`payment_item`) REFERENCES `eshop_items` (`item_name`);

--
-- Constraints for table `interested_users`
--
ALTER TABLE `interested_users`
  ADD CONSTRAINT `int_ann` FOREIGN KEY (`int_ann`) REFERENCES `announcements` (`ann_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `int_user` FOREIGN KEY (`int_user`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `messages`
--
ALTER TABLE `messages`
  ADD CONSTRAINT `msg_receiver` FOREIGN KEY (`msg_receiver`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `msg_sender` FOREIGN KEY (`msg_sender`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `my_appointments`
--
ALTER TABLE `my_appointments`
  ADD CONSTRAINT `app_id` FOREIGN KEY (`my_app_id`) REFERENCES `appointments` (`app_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `app_user` FOREIGN KEY (`my_app_user`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `personal_diary`
--
ALTER TABLE `personal_diary`
  ADD CONSTRAINT `per_diary_user` FOREIGN KEY (`per_diary_user`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `review`
--
ALTER TABLE `review`
  ADD CONSTRAINT `rev_user` FOREIGN KEY (`rev_user`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `rev_writer` FOREIGN KEY (`rev_writer`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
