/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.5.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: RealEstateDB
-- ------------------------------------------------------
-- Server version	11.5.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Current Database: `RealEstateDB`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `RealEstateDB` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

USE `RealEstateDB`;

--
-- Table structure for table `Agents`
--

DROP TABLE IF EXISTS `Agents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Agents` (
  `agent_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`agent_id`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Agents`
--

LOCK TABLES `Agents` WRITE;
/*!40000 ALTER TABLE `Agents` DISABLE KEYS */;
INSERT INTO `Agents` VALUES
(1,'Sarthak Puri','03688261303','yashica52@example.com'),
(2,'Wishi Sethi','3973517746','dalbir29@example.net'),
(3,'Gunbir Roy','01503542833','fsagar@example.com'),
(4,'Girik Dhar','2312239909','amarabhatnagar@example.org'),
(5,'Yamini Sani','+910657777397','mugdha29@example.org'),
(6,'Januja Thakur','2006853599','sachdevronith@example.com'),
(7,'Dalaja Murty','01864089341','sahnigavin@example.com'),
(8,'Abdul Randhawa','+918887732659','upasna08@example.com'),
(9,'Abdul Morar','07863003159','nimrat72@example.org'),
(10,'Krish Balay','+912884988498','omisha75@example.net');
/*!40000 ALTER TABLE `Agents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Clients`
--

DROP TABLE IF EXISTS `Clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Clients` (
  `client_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`client_id`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clients`
--

LOCK TABLES `Clients` WRITE;
/*!40000 ALTER TABLE `Clients` DISABLE KEYS */;
/*!40000 ALTER TABLE `Clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Properties`
--

DROP TABLE IF EXISTS `Properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Properties` (
  `property_id` int(11) NOT NULL AUTO_INCREMENT,
  `agent_id` int(11) DEFAULT NULL,
  `address` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `area` decimal(10,2) NOT NULL,
  `description` text DEFAULT NULL,
  `listing_date` date DEFAULT NULL,
  PRIMARY KEY (`property_id`),
  KEY `agent_id` (`agent_id`),
  CONSTRAINT `Properties_ibfk_1` FOREIGN KEY (`agent_id`) REFERENCES `Agents` (`agent_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Properties`
--

LOCK TABLES `Properties` WRITE;
/*!40000 ALTER TABLE `Properties` DISABLE KEYS */;
INSERT INTO `Properties` VALUES
(1,5,'13/414, Yogi Chowk, Rajahmundry-129288',1006257.77,1271.96,'1BHK','2015-09-19'),
(2,7,'66/09\nVarghese Chowk\nGuna-315699',1260992.26,1411.22,'6BHK','2014-02-10'),
(3,7,'232\nShan Path\nGorakhpur-624428',509877.94,930.86,'Orchard','2017-04-11'),
(4,3,'H.No. 845, Varma Marg, Kochi-782226',1441454.80,1844.88,'5 story','2014-05-31'),
(5,8,'92/77, Kara Ganj, Tiruppur 266241',1152585.69,1070.09,'2 story','2018-06-01'),
(6,2,'H.No. 936, Dube Street, Rajahmundry-516851',1061119.23,1593.33,'Orchard','2017-01-31'),
(7,4,'89/200, Babu Ganj, Vijayanagaram-000057',936001.57,1377.51,'4BHK','2015-02-07'),
(8,1,'79/445, Desai\nKamarhati-635517',1454833.54,134.68,'Land','2015-02-16'),
(9,5,'01, Acharya, Phagwara-837886',451804.13,1717.19,'2 story','2022-02-01'),
(10,5,'89\nDate Chowk, Ajmer 960548',733525.59,960.90,'Orchard','2014-11-29'),
(11,9,'135, Srinivas Path\nSecunderabad 554746',376463.68,843.55,'5 story','2019-12-26'),
(12,3,'01/112\nBansal Street, Mau-702064',509877.75,197.52,'Orchard','2024-07-12'),
(13,9,'754\nMorar Zila\nSalem-000824',316011.48,213.93,'Land','2018-02-27'),
(14,7,'147\nIyengar Circle\nKavali-607158',991037.94,1495.52,'Orchard','2021-04-18'),
(15,8,'37/691\nChada Chowk\nSaharsa-282215',1836004.56,1797.49,'6BHK','2023-10-15'),
(16,6,'86/61, Raju Marg, Siwan 070328',1895386.57,1705.04,'2BHK','2024-09-27'),
(17,7,'29/834\nBala Street, Bellary 296388',930971.41,1228.84,'Orchard','2017-12-15'),
(18,1,'H.No. 439\nVig Circle, Bongaigaon-540264',1012939.88,1572.74,'4 story','2020-04-06'),
(19,7,'86, Badal Chowk\nBettiah-224783',1343563.58,129.33,'Land','2022-08-05'),
(20,1,'H.No. 11, Nagar Street, Tiruppur-133892',1772701.71,736.80,'2 story','2020-12-08'),
(21,3,'H.No. 46\nYogi Road, Giridih 589429',816611.19,1077.37,'4BHK','2023-07-01'),
(22,7,'H.No. 03\nParikh Marg, Secunderabad-669982',1209857.56,1997.64,'5BHK','2014-11-04'),
(23,5,'H.No. 40\nLoke Marg\nRaipur 299746',1069681.40,764.66,'5 story','2023-04-21'),
(24,3,'860\nBobal Zila\nBijapur-515946',1490745.67,1418.23,'4BHK','2023-07-20'),
(25,9,'H.No. 462, Barad Ganj, Thiruvananthapuram-705788',1093269.13,1438.60,'6 story','2016-02-08'),
(26,6,'H.No. 111\nAhuja Path, Kirari Suleman Nagar 351945',1179637.31,1350.84,'3BHK','2020-12-07'),
(27,1,'144\nWadhwa Ganj\nNorth Dumdum-231056',909650.13,475.09,'3BHK','2014-07-28'),
(28,7,'66/720, Balay Street\nUjjain 308029',357418.92,1180.95,'Orchard','2022-10-02'),
(29,5,'H.No. 21, Prasad Circle\nBijapur 796026',827291.16,936.70,'2 story','2019-10-04'),
(30,7,'H.No. 07\nSahni\nGiridih-871462',1373164.91,1630.87,'Land','2019-06-27'),
(31,4,'75\nSant Circle\nBhilwara-468082',1725960.66,383.86,'6 story','2024-08-08'),
(32,5,'78\nGoyal Path, Danapur 636472',747341.83,1271.89,'3 story','2019-10-09'),
(33,4,'24/49\nManda\nNellore-484240',302821.67,550.49,'Orchard','2019-08-20'),
(34,5,'01/88, Magar Circle\nKatni-280576',1165419.87,833.71,'Land','2022-08-24'),
(35,4,'05/800, Bhalla Marg, Karawal Nagar 083962',205418.60,1928.27,'Orchard','2022-07-22'),
(36,3,'283, Koshy Nagar\nDarbhanga 724176',473296.03,539.15,'5 story','2022-06-29'),
(37,6,'H.No. 85, Chandra Chowk\nBardhaman 176769',347930.82,300.50,'Land','2022-01-11'),
(38,5,'H.No. 804, Anand Street\nUdaipur 727796',329991.27,1447.89,'2BHK','2016-03-09'),
(39,1,'55/91, Ghose Marg\nBikaner 196989',736486.02,1286.01,'Orchard','2020-03-15'),
(40,8,'69/015, Yadav, Bhilwara-893293',714690.62,533.67,'Orchard','2020-04-24'),
(41,8,'92\nIssac Path, Uluberia 469335',1394147.84,1460.03,'6 story','2020-02-05'),
(42,3,'H.No. 33\nChatterjee Zila, Madanapalle 396207',1742079.61,1513.23,'6 story','2016-03-13'),
(43,4,'17/634\nGala Nagar\nDibrugarh 638083',846865.04,485.58,'5 story','2022-01-03'),
(44,6,'76\nSami, Patna-211079',1716211.29,1892.39,'6BHK','2019-10-23'),
(45,7,'38/742\nMukhopadhyay Path, Amroha-263338',534335.03,1038.26,'Land','2022-05-25'),
(46,2,'H.No. 98, Jaggi Ganj, Pondicherry 634782',1890927.29,1023.05,'Land','2020-02-05'),
(47,1,'838, Sem Path\nSaharsa 648119',418379.92,1265.94,'2BHK','2014-02-17'),
(48,9,'H.No. 10\nMitter Street, Kalyan-Dombivli 290154',380982.18,1024.72,'Land','2015-03-21'),
(49,8,'H.No. 67\nSathe Nagar\nAvadi 975263',290819.20,168.22,'6 story','2024-03-01'),
(50,5,'H.No. 990\nSaran Nagar\nRatlam 079796',1633587.50,1399.50,'Orchard','2021-01-22');
/*!40000 ALTER TABLE `Properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transactions`
--

DROP TABLE IF EXISTS `Transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Transactions` (
  `transaction_id` int(11) NOT NULL AUTO_INCREMENT,
  `property_id` int(11) DEFAULT NULL,
  `transaction_date` date DEFAULT NULL,
  `amount` decimal(10,2) NOT NULL,
  `buyer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `property_id` (`property_id`),
  KEY `buyer_id` (`buyer_id`),
  CONSTRAINT `Transactions_ibfk_1` FOREIGN KEY (`property_id`) REFERENCES `Properties` (`property_id`) ON DELETE CASCADE,
  CONSTRAINT `Transactions_ibfk_2` FOREIGN KEY (`buyer_id`) REFERENCES `Clients` (`client_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transactions`
--

LOCK TABLES `Transactions` WRITE;
/*!40000 ALTER TABLE `Transactions` DISABLE KEYS */;
/*!40000 ALTER TABLE `Transactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2024-10-06 19:56:18
