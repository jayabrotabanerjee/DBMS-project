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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Agents`
--

LOCK TABLES `Agents` WRITE;
/*!40000 ALTER TABLE `Agents` DISABLE KEYS */;
INSERT INTO `Agents` VALUES
(1,'Girish Sahota','+912196945463','diyamohanty@example.com'),
(2,'Krisha Sinha','02481771475','arya28@example.net'),
(3,'Warjas Basu','02232219307','sanghaisaac@example.com'),
(4,'Patrick Yadav','03407175500','savantnidhi@example.net'),
(5,'Imaran Thakur','08011022442','bsami@example.net'),
(6,'Mitali Majumdar','+915663153071','bnatarajan@example.org'),
(7,'Tejas Tank','+919551224211','kchaudhari@example.org');
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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clients`
--

LOCK TABLES `Clients` WRITE;
/*!40000 ALTER TABLE `Clients` DISABLE KEYS */;
INSERT INTO `Clients` VALUES
(1,'Zarna Sharma','00009595988','prasadorinder@example.org'),
(2,'Benjamin Varkey','01569474126','sapte@example.org'),
(3,'Teerth Karnik','+919329905141','xray@example.net'),
(4,'Faraj Jhaveri','9448947381','hemang54@example.org'),
(5,'William Krishna','+915052303335','benjaminnatt@example.net'),
(6,'Warhi Sandal','+910130419656','edwinbrinda@example.com'),
(7,'Yadavi Majumdar','06282261151','abdulsha@example.com'),
(8,'Vritti Jhaveri','04952866289','msundaram@example.net'),
(9,'Samuel Nigam','02765446901','zaitra73@example.org'),
(10,'Meghana Varghese','+913760738313','irasidhu@example.org'),
(11,'Om Borra','+916667418642','falak03@example.org'),
(12,'Chandresh Narula','03477226352','garimamallick@example.org'),
(13,'Megha Srinivasan','5338427145','shravya18@example.org'),
(14,'Baljiwan Sur','06694130254','lokeindali@example.org'),
(15,'Anita Krishnamurthy','6896761661','bakhshi51@example.org'),
(16,'Ekiya Keer','9940036583','aachalraja@example.com'),
(17,'Wriddhish Sahni','6773403135','ezachariah@example.net'),
(18,'Harinakshi Taneja','3344792118','dalaja23@example.com'),
(19,'Zayyan Patel','+914504514741','bina89@example.com'),
(20,'Laban Ravi','+918519587346','jandra@example.org'),
(21,'Brijesh Chacko','05431984285','anviwarrior@example.net'),
(22,'Lila Dyal','1706325522','apandya@example.net'),
(23,'Vasudha Kumer','+911499037791','acharyaagastya@example.com'),
(24,'Warinder Dara','01601661471','kibedayamai@example.com'),
(25,'Pratyush Dewan','00513522696','ishaanpau@example.com'),
(26,'Naveen Bassi','02504697918','khannamanthan@example.net'),
(27,'Agastya Sankar','5530377850','qarin81@example.com');
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
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Properties`
--

LOCK TABLES `Properties` WRITE;
/*!40000 ALTER TABLE `Properties` DISABLE KEYS */;
INSERT INTO `Properties` VALUES
(1,1,'H.No. 798 Bandi Street, Arrah 552929',494392.55,199.95,'5 story','2020-10-23',1),
(2,6,'27, Dubey, Guntakal-612587',1331024.50,1217.98,'Land','2020-03-10',1),
(3,2,'92/951, Ben Circle, Bettiah-078999',1901885.12,230.52,'2 story','2013-11-02',1),
(4,1,'941 Chhabra Marg, Tadepalligudem-165002',1000500.46,1886.47,'Land','2021-01-24',1),
(5,5,'H.No. 40, Rastogi Circle, Indore 155290',1341780.13,1372.02,'Land','2013-11-05',0),
(6,3,'28/457 Bhattacharyya Road, Pune-392019',950913.50,1533.76,'Land','2024-08-28',1),
(7,6,'17/06, Lad Circle, Ramgarh-417817',696570.71,1526.94,'4BHK','2021-10-24',0),
(8,4,'H.No. 390 Roy, Jehanabad-262917',1450567.71,761.15,'4BHK','2020-03-03',1),
(9,1,'22/28, Manne Circle, Rajkot 923695',290021.96,1116.16,'Orchard','2020-03-10',0),
(10,2,'71/956, Soni Street Sagar-193622',1781185.53,1503.44,'Land','2024-03-02',0),
(11,3,'H.No. 512 Karnik Marg, Kollam 628259',1858666.36,1314.53,'4 story','2022-12-09',1),
(12,1,'H.No. 905 Amble Street Muzaffarnagar-527931',1841113.95,1096.57,'3BHK','2022-05-27',0),
(13,3,'H.No. 54, Gour, Visakhapatnam-040281',1274436.51,1840.98,'4BHK','2018-04-20',1),
(14,6,'53/40, Warrior Circle, Navi Mumbai-269518',1399411.28,1668.21,'2 story','2017-04-27',0),
(15,2,'H.No. 37, Bava Ganj Malda-986907',321269.88,1961.45,'2 story','2013-12-14',0),
(16,3,'51/067, Manda Road, Vijayanagaram 258799',200086.92,815.58,'Orchard','2014-03-13',1),
(17,5,'587, Rana Zila, Guna-499097',758457.54,1112.25,'Land','2021-10-26',1),
(18,1,'59/205 Chandra Road, Singrauli-768260',335333.34,611.64,'Land','2024-01-03',1),
(19,6,'178 Cheema Marg, Tadepalligudem-469024',1984530.35,718.58,'Land','2022-07-16',0),
(20,2,'08 Parmar Chowk, Gangtok-226050',1011909.43,999.10,'2BHK','2017-02-07',1),
(21,3,'H.No. 170, Gola Marg, Secunderabad-779806',1992037.13,1264.12,'Orchard','2015-09-02',0),
(22,1,'H.No. 189, Vig Ganj Durg 997316',517899.43,1384.87,'Orchard','2022-03-30',1),
(23,1,'61 Ramesh Marg, Tadipatri-899070',425023.83,906.78,'Orchard','2021-04-12',1),
(24,3,'H.No. 15 Prakash Marg, Panipat 395866',311090.90,1864.69,'2BHK','2021-03-11',1),
(25,5,'591, Wable Street Phusro 545666',540940.23,475.09,'Orchard','2018-05-21',1),
(26,4,'49/17, Dutta Circle Hapur 609806',1612065.21,458.56,'2BHK','2017-07-04',1),
(27,1,'H.No. 81 Dubey Ganj Dehradun 204896',1186754.95,303.36,'Orchard','2022-04-06',1),
(28,5,'60/323 Bera Chowk Tiruvottiyur 652861',260148.82,134.49,'Orchard','2022-01-27',1),
(29,2,'28/28, Roy Circle, Siliguri-252839',1452011.04,1262.10,'Land','2020-03-04',1),
(30,3,'86/59, Agate Nagar, Bidar 501620',725632.00,120.00,'Land','2019-01-31',1),
(31,3,'96, Pau Path Jamshedpur 864695',1464729.27,1214.87,'Land','2023-11-04',1),
(32,2,'H.No. 948, Hans Chowk, Yamunanagar 676631',724351.05,1524.15,'Orchard','2016-12-26',1),
(33,3,'57, Arya Zila, Kakinada 285832',1408008.06,1294.94,'4 story','2021-02-11',1),
(34,1,'H.No. 68, Bhat Haridwar-921118',1641023.08,852.43,'5BHK','2015-02-15',1),
(35,6,'76 Karpe Zila Pallavaram-364286',1139249.67,1873.87,'Orchard','2024-03-04',1),
(36,3,'98 Sampath Zila, Tiruvottiyur 821645',886542.99,126.15,'5 story','2015-08-12',1),
(37,4,'H.No. 57, Walia, Miryalaguda 166720',1206942.41,1392.70,'4 story','2018-10-09',1),
(38,2,'87/360, Zachariah Chowk, Visakhapatnam 341274',748716.33,803.75,'Land','2019-02-26',1),
(39,1,'84/90, Chad Circle, Thrissur-821282',1267155.50,1884.69,'4 story','2020-05-26',1),
(40,3,'03/82 Rai Chowk Anand 313454',1421674.66,886.44,'1BHK','2015-01-14',0),
(41,2,'H.No. 969 Dave Ganj Mysore 081511',778457.52,1027.15,'2 story','2021-12-25',0),
(42,1,'H.No. 27 Kapoor Path Ghaziabad-297679',1866687.22,1716.92,'2 story','2016-01-18',1),
(43,4,'H.No. 037, Chacko Marg, Raurkela Industrial Township 565637',1087701.67,958.24,'Orchard','2019-03-07',0),
(44,3,'26 Kalita Street, Raiganj-307120',1783453.85,649.55,'Land','2023-08-17',1),
(45,2,'34/442 Pradhan Road Bellary 562815',1092535.15,1148.01,'2BHK','2021-06-11',1),
(46,5,'327, Dutta Zila, Chittoor-139195',989224.77,685.36,'Orchard','2017-04-23',1),
(47,5,'80/177 Keer Road Hubli–Dharwad 983971',1604897.72,1332.41,'Land','2017-03-27',1),
(48,2,'H.No. 875, Kapadia Road Aurangabad 952341',1329112.97,544.10,'6 story','2023-07-25',0),
(49,3,'04/43, Bali Aligarh-310399',1152397.79,1839.29,'4 story','2023-04-26',1),
(50,5,'40, Verma Ganj Kollam-685140',452178.56,1502.44,'5BHK','2014-04-27',1),
(51,6,'H.No. 40, Bansal Road Yamunanagar 049152',583564.73,441.47,'Land','2021-11-15',1),
(52,3,'86/915, Lala Chowk, Kulti-314218',486830.96,1814.12,'Orchard','2022-08-20',1),
(53,5,'H.No. 301, Choudhary Nizamabad 853212',528819.95,1705.44,'Land','2016-05-18',1),
(54,5,'53 Mittal Nagar Saharanpur-222687',1217053.85,1125.62,'Land','2019-07-17',1),
(55,4,'34, Nagarajan, Mysore 670599',363641.81,418.19,'5 story','2015-07-08',1),
(56,1,'H.No. 07 Bandi Chowk Anand 667183',1723310.33,909.91,'Orchard','2022-03-29',0),
(57,2,'H.No. 00 Bassi, Aurangabad-839405',1851583.64,1153.12,'6BHK','2018-06-08',1),
(58,5,'93/03 Kapoor Road Bhiwani-350424',975596.18,1218.99,'Land','2024-01-21',0),
(59,1,'429, Oza Zila Ongole 709793',421878.65,522.38,'4 story','2021-05-10',1),
(60,2,'39/626, Mander, Jalgaon 712171',384099.68,921.37,'Land','2024-09-27',1),
(61,5,'H.No. 423 Verma Street, Bongaigaon 765342',1295742.10,1505.87,'Land','2018-05-30',0),
(62,2,'94/66 Chadha Street Thane-241185',789180.37,1474.57,'3BHK','2015-03-29',0);
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
  `buyer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transactions`
--

LOCK TABLES `Transactions` WRITE;
/*!40000 ALTER TABLE `Transactions` DISABLE KEYS */;
INSERT INTO `Transactions` VALUES
(1,15,'2022-09-18',23),
(2,38,'2022-10-25',11),
(3,53,'2022-04-17',23),
(4,34,'2024-04-06',6),
(5,27,'2023-04-08',10),
(6,24,'2022-06-18',24),
(7,37,'2023-04-13',16),
(8,29,'2021-05-13',17),
(9,51,'2024-05-06',12),
(10,5,'2024-09-14',14),
(11,33,'2023-10-20',18),
(12,45,'2017-10-30',26),
(13,22,'2021-08-17',11),
(14,2,'2020-03-22',3),
(15,50,'2023-12-28',15),
(16,56,'2023-08-08',21),
(17,1,'2022-09-05',21),
(18,21,'2022-11-28',11),
(19,31,'2022-02-26',12),
(20,52,'2023-12-15',26),
(21,41,'2022-04-03',23),
(22,48,'2024-05-18',25),
(23,17,'2024-03-27',22),
(24,58,'2024-04-11',22),
(25,35,'2018-02-08',20),
(26,26,'2024-05-15',0),
(27,36,'2021-01-12',10),
(28,7,'2021-03-05',11),
(29,59,'2024-09-27',9),
(30,28,'2021-02-12',4),
(31,0,'2021-12-26',18),
(32,46,'2018-07-22',5),
(33,16,'2023-10-28',5),
(34,23,'2023-06-17',22),
(35,19,'2023-12-14',20),
(36,25,'2021-10-21',24),
(37,44,'2024-04-16',10),
(38,43,'2024-04-02',14),
(39,10,'2023-04-19',17),
(40,49,'2020-08-12',17),
(41,32,'2024-09-09',0),
(42,3,'2024-05-29',16),
(43,54,'2024-02-27',19),
(44,12,'2020-06-15',11),
(45,30,'2024-04-19',2);
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

-- Dump completed on 2024-10-12 22:52:48
