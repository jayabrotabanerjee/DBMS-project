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
(1,'Aditya Deshmukh','02686778979','vigchampak@example.net'),
(2,'Sneha Naidu','+917968420819','lakshmibatta@example.com'),
(3,'Advay Gara','0314692082','cyogi@example.com'),
(4,'Leela Warrior','9593093280','obajwa@example.org'),
(5,'Oscar Savant','07387209164','janani74@example.com'),
(6,'Manbir Pant','+915009018068','chasmumrana@example.net'),
(7,'Balveer Bakshi','05855072551','fmadan@example.net'),
(8,'Omaja Tella','08294183731','reyanshkala@example.com'),
(9,'Prisha Bains','+918467802330','udeol@example.org'),
(10,'Kavya Date','1613781820','biswasnaveen@example.org');
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
  `sold` tinyint(1) DEFAULT NULL,
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
(1,8,'84/64, Varghese Road Mau-114018',537906.75,612.47,'Orchard','2014-08-12',0),
(2,5,'63/16, Mohanty Nagar, Ozhukarai 202872',410567.25,417.59,'5BHK','2022-08-17',0),
(3,6,'30/51 Loke Road, Tenali 385828',423529.83,356.60,'Orchard','2021-05-10',0),
(4,8,'29/21 Murthy, Narasaraopet 210430',1379394.26,1177.31,'3BHK','2022-01-08',0),
(5,2,'489 Grover Chowk Nagercoil-663359',1295856.02,471.46,'2 story','2024-08-01',0),
(6,7,'64/26, Sawhney Marg, Ramagundam 245355',453069.74,553.18,'3 story','2023-10-14',0),
(7,4,'35/01, Mallick Jalandhar 331296',651097.11,1237.57,'Land','2019-03-10',0),
(8,2,'50/149 Jhaveri Road, Bijapur-229245',433004.67,908.57,'Land','2017-04-15',0),
(9,6,'783 Narain Chowk Dhanbad-612846',611978.24,1909.16,'Orchard','2020-01-20',0),
(10,5,'31/74, Manne Chowk Jorhat 585465',967126.93,1530.25,'Orchard','2022-01-23',0),
(11,4,'72/23 Ram Road, Tadepalligudem-149281',737961.75,842.28,'2 story','2013-12-12',0),
(12,8,'291 Hans Street Kadapa-939784',794829.16,236.17,'Orchard','2024-05-06',0),
(13,9,'092, Keer Nagar Kozhikode-344068',1365740.39,1095.01,'Orchard','2020-09-23',0),
(14,8,'249, Kalla Path, Chandrapur-316473',1488814.96,858.73,'6 story','2023-12-04',0),
(15,2,'85, Gera Path, Pali-246729',683502.73,1327.98,'Orchard','2020-04-14',0),
(16,2,'82/253 Choudhry Street Kulti 108061',224940.74,328.98,'Land','2015-07-06',0),
(17,7,'42/59, Kara Nagar Durgapur-132347',272157.88,919.25,'Orchard','2021-04-08',0),
(18,4,'H.No. 144, Ahluwalia Street Pudukkottai 106189',1752402.22,1663.49,'5 story','2016-08-05',0),
(19,1,'82/145 Bakshi Nanded 898186',1392725.75,1714.84,'Land','2021-05-20',0),
(20,9,'434, Narain Circle Bally 491301',817072.79,865.27,'Orchard','2018-03-08',0),
(21,4,'H.No. 52 Choudhary Path Madanapalle 268409',1488832.27,1777.82,'5 story','2017-12-17',0),
(22,2,'51 Chad Zila Agra-413362',1282130.16,841.29,'2 story','2024-05-14',0),
(23,1,'985, Balakrishnan Ganj, Berhampore 002659',1956667.33,879.81,'Orchard','2015-02-07',0),
(24,4,'82/422 Boase Nagar, Alappuzha 646219',1979329.69,1137.03,'Orchard','2015-02-04',0),
(25,9,'H.No. 057, Khanna Street Ratlam 446593',724935.33,463.67,'Land','2014-05-26',0),
(26,2,'03/672, Sundaram Path Mysore 942566',1923923.71,1920.67,'6 story','2015-09-13',0),
(27,1,'29, Borah Ganj, Sambalpur-965555',1173498.40,1039.03,'Land','2013-10-16',0),
(28,8,'H.No. 27, Choudhury Nagar Rajpur Sonarpur 955690',482318.74,1596.44,'6BHK','2016-06-16',0),
(29,9,'223, Bahri Road Bhopal 567666',251560.33,1612.21,'Land','2014-03-21',0),
(30,6,'618 Bahri Zila, Sonipat-016487',1085217.15,429.65,'Land','2019-10-30',0),
(31,1,'99/408, Rana Street Singrauli-112569',1618733.49,968.08,'5 story','2023-02-28',0),
(32,7,'39 Ramanathan Marg, New Delhi 745144',531191.12,466.56,'Orchard','2017-01-11',0),
(33,4,'11/988, Hayer, Jaunpur-920636',976837.81,1178.21,'Orchard','2016-05-05',0),
(34,5,'44/834 Kulkarni Road Karaikudi-097699',1325537.26,1073.57,'Land','2020-10-19',0),
(35,7,'45/38, Soman Sirsa 123113',805668.06,744.08,'6 story','2019-07-04',0),
(36,6,'71/242 Tandon Marg Sambhal 491888',546689.40,846.55,'Orchard','2014-04-18',0),
(37,2,'07/62 Agate Marg, Kulti 960681',1488437.63,330.75,'3 story','2014-06-12',0),
(38,5,'H.No. 03, Merchant Zila, Chittoor-665657',1885626.29,1893.27,'5 story','2020-07-11',0),
(39,7,'664 Amble Road, Srinagar 882325',883240.40,935.40,'Orchard','2022-03-15',0),
(40,2,'273, Andra Circle Coimbatore-533545',1322075.47,1081.10,'Land','2015-07-01',0),
(41,7,'19/82 Ghosh Circle, Korba-654028',1634859.19,1064.90,'Land','2019-06-18',0),
(42,3,'H.No. 25 Dar Road, Panipat-354260',677687.83,1339.58,'5 story','2014-11-24',0),
(43,8,'H.No. 78, Choudhury Street, Meerut 523235',965924.60,1062.60,'5 story','2017-03-15',0),
(44,7,'H.No. 28, Ratti Nagar Satna 364658',1174965.14,119.94,'Orchard','2022-10-23',0),
(45,6,'H.No. 593, Wason Path Kamarhati 455624',863533.18,1231.12,'4BHK','2019-01-20',0),
(46,9,'H.No. 440, Banerjee Chowk, Belgaum 647469',291004.02,1448.38,'5BHK','2015-10-05',0),
(47,9,'660 Sankaran Nagar, Dhule 304117',1472621.91,1637.43,'Orchard','2023-01-16',0),
(48,7,'H.No. 751 Varghese Circle, Lucknow-915629',600989.50,933.01,'Orchard','2019-08-23',0),
(49,2,'503, Raman Street Bidar 041045',1485980.96,190.32,'Orchard','2020-05-12',0),
(50,4,'04/199, Dey Road, Avadi-656150',987806.09,1762.84,'Orchard','2016-03-26',0);
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

-- Dump completed on 2024-10-07 21:26:06
