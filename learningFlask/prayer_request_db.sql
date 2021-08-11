-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.5.4-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for prayer_request
CREATE DATABASE IF NOT EXISTS `prayer_request` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `prayer_request`;

-- Dumping structure for table prayer_request.category
CREATE TABLE IF NOT EXISTS `category` (
  `Category_id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`Category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table prayer_request.prayer_request
CREATE TABLE IF NOT EXISTS `prayer_request` (
  `Prayer_Request_id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(22) NOT NULL DEFAULT '0',
  `Description` varchar(1000) DEFAULT NULL,
  `IsAnswered` tinyint(1) NOT NULL DEFAULT 0,
  `Add_By` varchar(50) DEFAULT NULL,
  `Category_id` int(11) DEFAULT NULL,
  `Date_Added` date NOT NULL,
  `Date_Answered` date DEFAULT NULL,
  PRIMARY KEY (`Prayer_Request_id`),
  KEY `FK_prayer_request_category` (`Category_id`),
  CONSTRAINT `FK_prayer_request_category` FOREIGN KEY (`Category_id`) REFERENCES `category` (`Category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
