-- MySQL dump 10.13  Distrib 5.6.20, for Win64 (x86_64)
--
-- Host: localhost    Database: chinese_db
-- ------------------------------------------------------
-- Server version	5.6.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(22,'Can add lesson',8,'add_lesson'),(23,'Can change lesson',8,'change_lesson'),(24,'Can delete lesson',8,'delete_lesson'),(25,'Can add word pl',9,'add_wordpl'),(26,'Can change word pl',9,'change_wordpl'),(27,'Can delete word pl',9,'delete_wordpl'),(28,'Can add word zh',10,'add_wordzh'),(29,'Can change word zh',10,'change_wordzh'),(30,'Can delete word zh',10,'delete_wordzh'),(31,'Can add word translation',11,'add_wordtranslation'),(32,'Can change word translation',11,'change_wordtranslation'),(33,'Can delete word translation',11,'delete_wordtranslation'),(34,'Can add sentence pl',12,'add_sentencepl'),(35,'Can change sentence pl',12,'change_sentencepl'),(36,'Can delete sentence pl',12,'delete_sentencepl'),(37,'Can add sentence zh',13,'add_sentencezh'),(38,'Can change sentence zh',13,'change_sentencezh'),(39,'Can delete sentence zh',13,'delete_sentencezh'),(40,'Can add sentence translation',14,'add_sentencetranslation'),(41,'Can change sentence translation',14,'change_sentencetranslation'),(42,'Can delete sentence translation',14,'delete_sentencetranslation'),(43,'Can add subscription',15,'add_subscription'),(44,'Can change subscription',15,'change_subscription'),(45,'Can delete subscription',15,'delete_subscription'),(46,'Can add word skill',16,'add_wordskill'),(47,'Can change word skill',16,'change_wordskill'),(48,'Can delete word skill',16,'delete_wordskill'),(49,'Can add lesson action',17,'add_lessonaction'),(50,'Can change lesson action',17,'change_lessonaction'),(51,'Can delete lesson action',17,'delete_lessonaction'),(52,'Can add exercise',18,'add_exercise'),(53,'Can change exercise',18,'change_exercise'),(54,'Can delete exercise',18,'delete_exercise'),(55,'Can add exercise action',19,'add_exerciseaction'),(56,'Can change exercise action',19,'change_exerciseaction'),(57,'Can delete exercise action',19,'delete_exerciseaction'),(58,'Can add word zh exercise',20,'add_wordzhexercise'),(59,'Can change word zh exercise',20,'change_wordzhexercise'),(60,'Can delete word zh exercise',20,'delete_wordzhexercise'),(61,'Can add word pl exercise',21,'add_wordplexercise'),(62,'Can change word pl exercise',21,'change_wordplexercise'),(63,'Can delete word pl exercise',21,'delete_wordplexercise'),(64,'Can add sentence zh exercise',22,'add_sentencezhexercise'),(65,'Can change sentence zh exercise',22,'change_sentencezhexercise'),(66,'Can delete sentence zh exercise',22,'delete_sentencezhexercise'),(67,'Can add sentence pl exercise',23,'add_sentenceplexercise'),(68,'Can change sentence pl exercise',23,'change_sentenceplexercise'),(69,'Can delete sentence pl exercise',23,'delete_sentenceplexercise'),(70,'Can add explanation exercise',24,'add_explanationexercise'),(71,'Can change explanation exercise',24,'change_explanationexercise'),(72,'Can delete explanation exercise',24,'delete_explanationexercise'),(73,'Can add explanation image exercise',25,'add_explanationimageexercise'),(74,'Can change explanation image exercise',25,'change_explanationimageexercise'),(75,'Can delete explanation image exercise',25,'delete_explanationimageexercise'),(76,'Can add migration history',26,'add_migrationhistory'),(77,'Can change migration history',26,'change_migrationhistory'),(78,'Can delete migration history',26,'delete_migrationhistory');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `email` varchar(75) COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$fpVv56qkTUFf$PM9ce8S60mkJIupgqNwdYYWjSOTrvV1HQhfsQg2a4qM=','2015-03-05 18:14:50',1,'admin','','','',1,1,'2015-01-18 22:27:06');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_exercise`
--

DROP TABLE IF EXISTS `chinesetool_exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_exercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lesson_id` int(11) NOT NULL,
  `type` varchar(1) COLLATE utf8_bin NOT NULL,
  `number` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chinesetool_exercise_37003e55` (`lesson_id`),
  CONSTRAINT `lesson_id_refs_id_027df89d` FOREIGN KEY (`lesson_id`) REFERENCES `chinesetool_lesson` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_exercise`
--

LOCK TABLES `chinesetool_exercise` WRITE;
/*!40000 ALTER TABLE `chinesetool_exercise` DISABLE KEYS */;
INSERT INTO `chinesetool_exercise` VALUES (52,4,'c',1),(53,4,'b',3),(54,4,'e',2),(55,4,'d',5),(56,4,'f',4),(57,5,'f',1),(58,5,'f',2),(59,5,'f',3),(60,5,'f',4),(61,6,'f',NULL),(62,6,'f',NULL),(63,6,'f',NULL),(64,6,'f',NULL),(65,6,'f',NULL),(66,6,'f',NULL),(67,6,'f',NULL),(68,6,'f',NULL),(69,6,'f',NULL),(70,6,'f',NULL),(74,8,'f',1),(75,8,'f',2),(76,8,'f',NULL),(77,8,'f',NULL),(78,8,'f',NULL),(79,8,'f',NULL),(80,8,'f',NULL),(81,8,'f',NULL),(82,8,'f',5);
/*!40000 ALTER TABLE `chinesetool_exercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_exerciseaction`
--

DROP TABLE IF EXISTS `chinesetool_exerciseaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_exerciseaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` int(11) NOT NULL,
  `lesson_action_id` int(11) NOT NULL,
  `result` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chinesetool_exerciseaction_c18e0af4` (`exercise_id`),
  KEY `chinesetool_exerciseaction_ff58a6f6` (`lesson_action_id`),
  CONSTRAINT `exercise_id_refs_id_d0ef0d56` FOREIGN KEY (`exercise_id`) REFERENCES `chinesetool_exercise` (`id`),
  CONSTRAINT `lesson_action_id_refs_id_e21c761f` FOREIGN KEY (`lesson_action_id`) REFERENCES `chinesetool_lessonaction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_exerciseaction`
--

LOCK TABLES `chinesetool_exerciseaction` WRITE;
/*!40000 ALTER TABLE `chinesetool_exerciseaction` DISABLE KEYS */;
INSERT INTO `chinesetool_exerciseaction` VALUES (85,52,38,0,1),(86,54,38,0,2),(87,53,38,0,3),(88,56,38,0,4),(89,55,38,0,5);
/*!40000 ALTER TABLE `chinesetool_exerciseaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_explanationexercise`
--

DROP TABLE IF EXISTS `chinesetool_explanationexercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_explanationexercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` int(11) NOT NULL,
  `text` longtext COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chinesetool_explanationexercise_c18e0af4` (`exercise_id`),
  CONSTRAINT `exercise_id_refs_id_5e9138eb` FOREIGN KEY (`exercise_id`) REFERENCES `chinesetool_exercise` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_explanationexercise`
--

LOCK TABLES `chinesetool_explanationexercise` WRITE;
/*!40000 ALTER TABLE `chinesetool_explanationexercise` DISABLE KEYS */;
INSERT INTO `chinesetool_explanationexercise` VALUES (1,56,'Przykładowy slajd z wytłumaczeniem. \r\nLorem ipsum dolor sit amet, consectetur adipisicing elit. Proin nibh augue, suscipit a, scelerisque sed, lacinia in, mi. Cras vel lorem. Etiam pellentesque aliquet tellus. Phasellus pharetra nulla ac diam. Quisque semper justo at risus. Donec venenatis, turpis vel hendrerit interdum, dui ligula ultricies purus, sed posuere libero dui id orci. Nam congue, pede vitae dapibus aliquet, elit magna vulputate arcu, vel tempus metus leo non est. Etiam sit amet lectus quis est congue mollis. Phasellus congue lacus eget neque. Phasellus ornare, ante vitae consectetuer consequat, purus sapien ultricies dolor, et mollis pede metus eget nisi. Praesent sodales velit quis augue. Cras suscipit, urna at aliquam rhoncus, urna quam viverra nisi, in interdum massa nibh nec erat.'),(2,57,'Slajd 1'),(3,58,'Slajd 2'),(4,59,'Slajd 3'),(5,60,'Slajd 4 - slajdy w tej lekcji mialy narzucona kolejnosc wiec wyswietlily sie w z gory znanej kolejnosci (1, 2, 3, 4)'),(6,61,'W tej lekcji kolejność jest losowa więc slajdy są losowane podczas działania z puli. Wylosowanych jest 4 z 10 dostępnych\r\n\r\nSlajd 1'),(7,62,'W tej lekcji kolejność jest losowa więc slajdy są losowane podczas działania z puli. Wylosowanych jest 4 z 10 dostępnych\r\n\r\nSlajd 2'),(8,63,'W tej lekcji kolejność jest losowa więc slajdy są losowane podczas działania z puli. Wylosowanych jest 4 z 10 dostępnych\r\n\r\nSlajd 3'),(9,64,'W tej lekcji kolejność jest losowa więc slajdy są losowane podczas działania z puli. Wylosowanych jest 4 z 10 dostępnych\r\n\r\nSlajd 4'),(10,65,'W tej lekcji kolejność jest losowa więc slajdy są losowane podczas działania z puli. Wylosowanych jest 4 z 10 dostępnych\r\n\r\nSlajd 5'),(11,66,'W tej lekcji kolejność jest losowa więc slajdy są losowane podczas działania z puli. Wylosowanych jest 4 z 10 dostępnych\r\n\r\nSlajd 6'),(12,67,'W tej lekcji kolejność jest losowa więc slajdy są losowane podczas działania z puli. Wylosowanych jest 4 z 10 dostępnych\r\n\r\nSlajd 7'),(13,68,'W tej lekcji kolejność jest losowa więc slajdy są losowane podczas działania z puli. Wylosowanych jest 4 z 10 dostępnych\r\n\r\nSlajd 8'),(14,69,'W tej lekcji kolejność jest losowa więc slajdy są losowane podczas działania z puli. Wylosowanych jest 4 z 10 dostępnych\r\n\r\nSlajd 9'),(15,70,'W tej lekcji kolejność jest losowa więc slajdy są losowane podczas działania z puli. Wylosowanych jest 4 z 10 dostępnych\r\n\r\nSlajd 10'),(19,74,'Przykład mieszany - 2 pierwsze slajdy są w kolejności ustalonej, następnie 2 wylosowane z puli 6, na koniec 1 slajd ustalony.'),(20,75,'Slajd ustalony nr 2.'),(21,76,'Slajd losowy nr 1'),(22,77,'Slajd losowy nr 2'),(23,78,'Slajd losowy nr 3'),(24,79,'Slajd losowy nr 4'),(25,80,'Slajd losowy nr 5'),(26,81,'Slajd losowy nr 6'),(27,82,'Slajd ustalony nr 5 - ostatni');
/*!40000 ALTER TABLE `chinesetool_explanationexercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_explanationimageexercise`
--

DROP TABLE IF EXISTS `chinesetool_explanationimageexercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_explanationimageexercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` int(11) NOT NULL,
  `text` longtext COLLATE utf8_bin NOT NULL,
  `image` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chinesetool_explanationimageexercise_c18e0af4` (`exercise_id`),
  CONSTRAINT `exercise_id_refs_id_2b1196a3` FOREIGN KEY (`exercise_id`) REFERENCES `chinesetool_exercise` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_explanationimageexercise`
--

LOCK TABLES `chinesetool_explanationimageexercise` WRITE;
/*!40000 ALTER TABLE `chinesetool_explanationimageexercise` DISABLE KEYS */;
/*!40000 ALTER TABLE `chinesetool_explanationimageexercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_lesson`
--

DROP TABLE IF EXISTS `chinesetool_lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(100) COLLATE utf8_bin NOT NULL,
  `exercises_number` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_lesson`
--

LOCK TABLES `chinesetool_lesson` WRITE;
/*!40000 ALTER TABLE `chinesetool_lesson` DISABLE KEYS */;
INSERT INTO `chinesetool_lesson` VALUES (4,'Szkoła',5),(5,'Przykład - fixed',4),(6,'Przykład - random',4),(8,'Przykład - mixed',5);
/*!40000 ALTER TABLE `chinesetool_lesson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_lesson_requirements`
--

DROP TABLE IF EXISTS `chinesetool_lesson_requirements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_lesson_requirements` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_lesson_id` int(11) NOT NULL,
  `to_lesson_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `from_lesson_id` (`from_lesson_id`,`to_lesson_id`),
  KEY `chinesetool_lesson_requirements_f6734edd` (`from_lesson_id`),
  KEY `chinesetool_lesson_requirements_1e803bb4` (`to_lesson_id`),
  CONSTRAINT `from_lesson_id_refs_id_d98ff244` FOREIGN KEY (`from_lesson_id`) REFERENCES `chinesetool_lesson` (`id`),
  CONSTRAINT `to_lesson_id_refs_id_d98ff244` FOREIGN KEY (`to_lesson_id`) REFERENCES `chinesetool_lesson` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_lesson_requirements`
--

LOCK TABLES `chinesetool_lesson_requirements` WRITE;
/*!40000 ALTER TABLE `chinesetool_lesson_requirements` DISABLE KEYS */;
/*!40000 ALTER TABLE `chinesetool_lesson_requirements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_lessonaction`
--

DROP TABLE IF EXISTS `chinesetool_lessonaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_lessonaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `total_exercises_number` int(11) NOT NULL,
  `current_exercise_number` int(11) NOT NULL,
  `fails` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chinesetool_lessonaction_6340c63c` (`user_id`),
  KEY `chinesetool_lessonaction_37003e55` (`lesson_id`),
  CONSTRAINT `lesson_id_refs_id_ea897e7e` FOREIGN KEY (`lesson_id`) REFERENCES `chinesetool_lesson` (`id`),
  CONSTRAINT `user_id_refs_id_6762f5c2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_lessonaction`
--

LOCK TABLES `chinesetool_lessonaction` WRITE;
/*!40000 ALTER TABLE `chinesetool_lessonaction` DISABLE KEYS */;
INSERT INTO `chinesetool_lessonaction` VALUES (38,5,5,4,1,4);
/*!40000 ALTER TABLE `chinesetool_lessonaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_sentencepl`
--

DROP TABLE IF EXISTS `chinesetool_sentencepl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_sentencepl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sentence` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sentence` (`sentence`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_sentencepl`
--

LOCK TABLES `chinesetool_sentencepl` WRITE;
/*!40000 ALTER TABLE `chinesetool_sentencepl` DISABLE KEYS */;
INSERT INTO `chinesetool_sentencepl` VALUES (2,'Gdzie jest nowa szkoła?'),(1,'Lubię uczyć się chińskiego.');
/*!40000 ALTER TABLE `chinesetool_sentencepl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_sentenceplexercise`
--

DROP TABLE IF EXISTS `chinesetool_sentenceplexercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_sentenceplexercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` int(11) NOT NULL,
  `sentence_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chinesetool_sentenceplexercise_c18e0af4` (`exercise_id`),
  KEY `chinesetool_sentenceplexercise_9bad8f02` (`sentence_id`),
  CONSTRAINT `exercise_id_refs_id_e47a095f` FOREIGN KEY (`exercise_id`) REFERENCES `chinesetool_exercise` (`id`),
  CONSTRAINT `sentence_id_refs_id_22799b68` FOREIGN KEY (`sentence_id`) REFERENCES `chinesetool_sentencepl` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_sentenceplexercise`
--

LOCK TABLES `chinesetool_sentenceplexercise` WRITE;
/*!40000 ALTER TABLE `chinesetool_sentenceplexercise` DISABLE KEYS */;
INSERT INTO `chinesetool_sentenceplexercise` VALUES (1,55,2);
/*!40000 ALTER TABLE `chinesetool_sentenceplexercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_sentencetranslation`
--

DROP TABLE IF EXISTS `chinesetool_sentencetranslation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_sentencetranslation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sentence_zh_id` int(11) NOT NULL,
  `sentence_pl_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sentence_zh_id` (`sentence_zh_id`,`sentence_pl_id`),
  KEY `chinesetool_sentencetranslation_a86f1aae` (`sentence_zh_id`),
  KEY `chinesetool_sentencetranslation_9108fd47` (`sentence_pl_id`),
  CONSTRAINT `sentence_pl_id_refs_id_b65767aa` FOREIGN KEY (`sentence_pl_id`) REFERENCES `chinesetool_sentencepl` (`id`),
  CONSTRAINT `sentence_zh_id_refs_id_5b0289db` FOREIGN KEY (`sentence_zh_id`) REFERENCES `chinesetool_sentencezh` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_sentencetranslation`
--

LOCK TABLES `chinesetool_sentencetranslation` WRITE;
/*!40000 ALTER TABLE `chinesetool_sentencetranslation` DISABLE KEYS */;
INSERT INTO `chinesetool_sentencetranslation` VALUES (1,1,1),(2,2,2);
/*!40000 ALTER TABLE `chinesetool_sentencetranslation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_sentencezh`
--

DROP TABLE IF EXISTS `chinesetool_sentencezh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_sentencezh` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sentence` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sentence` (`sentence`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_sentencezh`
--

LOCK TABLES `chinesetool_sentencezh` WRITE;
/*!40000 ALTER TABLE `chinesetool_sentencezh` DISABLE KEYS */;
INSERT INTO `chinesetool_sentencezh` VALUES (1,'我喜欢学习中文。'),(2,'新的学校在哪里？');
/*!40000 ALTER TABLE `chinesetool_sentencezh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_sentencezhexercise`
--

DROP TABLE IF EXISTS `chinesetool_sentencezhexercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_sentencezhexercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` int(11) NOT NULL,
  `sentence_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chinesetool_sentencezhexercise_c18e0af4` (`exercise_id`),
  KEY `chinesetool_sentencezhexercise_9bad8f02` (`sentence_id`),
  CONSTRAINT `exercise_id_refs_id_913ff349` FOREIGN KEY (`exercise_id`) REFERENCES `chinesetool_exercise` (`id`),
  CONSTRAINT `sentence_id_refs_id_5922332b` FOREIGN KEY (`sentence_id`) REFERENCES `chinesetool_sentencezh` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_sentencezhexercise`
--

LOCK TABLES `chinesetool_sentencezhexercise` WRITE;
/*!40000 ALTER TABLE `chinesetool_sentencezhexercise` DISABLE KEYS */;
INSERT INTO `chinesetool_sentencezhexercise` VALUES (1,54,1);
/*!40000 ALTER TABLE `chinesetool_sentencezhexercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_subscription`
--

DROP TABLE IF EXISTS `chinesetool_subscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_subscription` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_id` int(11) NOT NULL,
  `registration_date` datetime NOT NULL,
  `last_login_date` datetime NOT NULL,
  `abo_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chinesetool_subscription_4da47e07` (`name_id`),
  CONSTRAINT `name_id_refs_id_e6e066ce` FOREIGN KEY (`name_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_subscription`
--

LOCK TABLES `chinesetool_subscription` WRITE;
/*!40000 ALTER TABLE `chinesetool_subscription` DISABLE KEYS */;
/*!40000 ALTER TABLE `chinesetool_subscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_wordpl`
--

DROP TABLE IF EXISTS `chinesetool_wordpl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_wordpl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `word` (`word`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_wordpl`
--

LOCK TABLES `chinesetool_wordpl` WRITE;
/*!40000 ALTER TABLE `chinesetool_wordpl` DISABLE KEYS */;
INSERT INTO `chinesetool_wordpl` VALUES (3,'dupa'),(4,'ja'),(5,'szkoła'),(2,'tańczyć'),(6,'uczeń'),(1,'śpiewać');
/*!40000 ALTER TABLE `chinesetool_wordpl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_wordplexercise`
--

DROP TABLE IF EXISTS `chinesetool_wordplexercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_wordplexercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` int(11) NOT NULL,
  `word_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chinesetool_wordplexercise_c18e0af4` (`exercise_id`),
  KEY `chinesetool_wordplexercise_558fda87` (`word_id`),
  CONSTRAINT `exercise_id_refs_id_0250c6b5` FOREIGN KEY (`exercise_id`) REFERENCES `chinesetool_exercise` (`id`),
  CONSTRAINT `word_id_refs_id_d0c2d7d4` FOREIGN KEY (`word_id`) REFERENCES `chinesetool_wordpl` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_wordplexercise`
--

LOCK TABLES `chinesetool_wordplexercise` WRITE;
/*!40000 ALTER TABLE `chinesetool_wordplexercise` DISABLE KEYS */;
INSERT INTO `chinesetool_wordplexercise` VALUES (3,53,6);
/*!40000 ALTER TABLE `chinesetool_wordplexercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_wordskill`
--

DROP TABLE IF EXISTS `chinesetool_wordskill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_wordskill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word_zh_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `last_time` datetime NOT NULL,
  `correct` int(11) NOT NULL,
  `correct_run` int(11) NOT NULL,
  `wrong` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chinesetool_wordskill_e5b47d84` (`word_zh_id`),
  KEY `chinesetool_wordskill_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_f62e30b2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `word_zh_id_refs_id_381ffdf5` FOREIGN KEY (`word_zh_id`) REFERENCES `chinesetool_wordzh` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_wordskill`
--

LOCK TABLES `chinesetool_wordskill` WRITE;
/*!40000 ALTER TABLE `chinesetool_wordskill` DISABLE KEYS */;
/*!40000 ALTER TABLE `chinesetool_wordskill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_wordtranslation`
--

DROP TABLE IF EXISTS `chinesetool_wordtranslation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_wordtranslation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word_zh_id` int(11) NOT NULL,
  `word_pl_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `word_zh_id` (`word_zh_id`,`word_pl_id`),
  KEY `chinesetool_wordtranslation_e5b47d84` (`word_zh_id`),
  KEY `chinesetool_wordtranslation_1ac5d68e` (`word_pl_id`),
  CONSTRAINT `word_pl_id_refs_id_6d7a0bbb` FOREIGN KEY (`word_pl_id`) REFERENCES `chinesetool_wordpl` (`id`),
  CONSTRAINT `word_zh_id_refs_id_d596beb8` FOREIGN KEY (`word_zh_id`) REFERENCES `chinesetool_wordzh` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_wordtranslation`
--

LOCK TABLES `chinesetool_wordtranslation` WRITE;
/*!40000 ALTER TABLE `chinesetool_wordtranslation` DISABLE KEYS */;
INSERT INTO `chinesetool_wordtranslation` VALUES (1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5),(6,6,6);
/*!40000 ALTER TABLE `chinesetool_wordtranslation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_wordzh`
--

DROP TABLE IF EXISTS `chinesetool_wordzh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_wordzh` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(50) COLLATE utf8_bin NOT NULL,
  `pinyin` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `word` (`word`,`pinyin`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_wordzh`
--

LOCK TABLES `chinesetool_wordzh` WRITE;
/*!40000 ALTER TABLE `chinesetool_wordzh` DISABLE KEYS */;
INSERT INTO `chinesetool_wordzh` VALUES (1,'唱歌',''),(5,'学校',''),(6,'学生',''),(3,'屁股',''),(4,'我',''),(2,'跳舞','');
/*!40000 ALTER TABLE `chinesetool_wordzh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chinesetool_wordzhexercise`
--

DROP TABLE IF EXISTS `chinesetool_wordzhexercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chinesetool_wordzhexercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` int(11) NOT NULL,
  `word_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chinesetool_wordzhexercise_c18e0af4` (`exercise_id`),
  KEY `chinesetool_wordzhexercise_558fda87` (`word_id`),
  CONSTRAINT `exercise_id_refs_id_92e8b347` FOREIGN KEY (`exercise_id`) REFERENCES `chinesetool_exercise` (`id`),
  CONSTRAINT `word_id_refs_id_f3673f16` FOREIGN KEY (`word_id`) REFERENCES `chinesetool_wordzh` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chinesetool_wordzhexercise`
--

LOCK TABLES `chinesetool_wordzhexercise` WRITE;
/*!40000 ALTER TABLE `chinesetool_wordzhexercise` DISABLE KEYS */;
INSERT INTO `chinesetool_wordzhexercise` VALUES (3,52,5);
/*!40000 ALTER TABLE `chinesetool_wordzhexercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext COLLATE utf8_bin,
  `object_repr` varchar(200) COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-01-22 21:05:44',1,18,'2','Śpiew 2',3,''),(2,'2015-01-22 21:05:44',1,18,'1','Śpiew 1',3,''),(3,'2015-01-31 13:23:25',1,18,'31','Śpiew 31',3,''),(4,'2015-01-31 13:23:25',1,18,'30','Śpiew 30',3,''),(5,'2015-01-31 13:23:25',1,18,'29','Śpiew 29',3,''),(6,'2015-01-31 13:23:25',1,18,'28','Śpiew 28',3,''),(7,'2015-01-31 13:23:25',1,18,'27','Śpiew 27',3,''),(8,'2015-01-31 13:23:25',1,18,'26','Śpiew 26',3,''),(9,'2015-01-31 13:23:25',1,18,'25','Śpiew 25',3,''),(10,'2015-01-31 13:23:25',1,18,'24','Śpiew 24',3,''),(11,'2015-01-31 13:23:25',1,18,'23','Śpiew 23',3,''),(12,'2015-01-31 13:23:25',1,18,'22','Śpiew 22',3,''),(13,'2015-01-31 13:23:25',1,18,'21','Śpiew 21',3,''),(14,'2015-01-31 13:23:25',1,18,'20','Śpiew 20',3,''),(15,'2015-01-31 13:23:25',1,18,'19','Śpiew 19',3,''),(16,'2015-01-31 13:23:25',1,18,'18','Śpiew 18',3,''),(17,'2015-01-31 13:23:25',1,18,'17','Śpiew 17',3,''),(18,'2015-01-31 13:23:25',1,18,'16','Śpiew 16',3,''),(19,'2015-01-31 13:23:25',1,18,'15','Śpiew 15',3,''),(20,'2015-01-31 13:23:25',1,18,'14','Śpiew 14',3,''),(21,'2015-01-31 13:23:25',1,18,'13','Śpiew 13',3,''),(22,'2015-01-31 13:23:25',1,18,'12','Śpiew 12',3,''),(23,'2015-01-31 13:23:25',1,18,'11','Śpiew 11',3,''),(24,'2015-01-31 13:23:25',1,18,'10','Śpiew 10',3,''),(25,'2015-01-31 13:23:25',1,18,'9','Śpiew 9',3,''),(26,'2015-01-31 13:23:25',1,18,'8','Śpiew 8',3,''),(27,'2015-01-31 13:23:25',1,18,'7','Śpiew 7',3,''),(28,'2015-01-31 13:23:25',1,18,'6','Śpiew 6',3,''),(29,'2015-01-31 13:23:25',1,18,'5','Śpiew 5',3,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_bin NOT NULL,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(8,'lesson','chinesetool','lesson'),(9,'word pl','chinesetool','wordpl'),(10,'word zh','chinesetool','wordzh'),(11,'word translation','chinesetool','wordtranslation'),(12,'sentence pl','chinesetool','sentencepl'),(13,'sentence zh','chinesetool','sentencezh'),(14,'sentence translation','chinesetool','sentencetranslation'),(15,'subscription','chinesetool','subscription'),(16,'word skill','chinesetool','wordskill'),(17,'lesson action','chinesetool','lessonaction'),(18,'exercise','chinesetool','exercise'),(19,'exercise action','chinesetool','exerciseaction'),(20,'word zh exercise','chinesetool','wordzhexercise'),(21,'word pl exercise','chinesetool','wordplexercise'),(22,'sentence zh exercise','chinesetool','sentencezhexercise'),(23,'sentence pl exercise','chinesetool','sentenceplexercise'),(24,'explanation exercise','chinesetool','explanationexercise'),(25,'explanation image exercise','chinesetool','explanationimageexercise'),(26,'migration history','south','migrationhistory');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_bin NOT NULL,
  `session_data` longtext COLLATE utf8_bin NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('46sb40z4it6ll4ntiq8avovign3st603','NDgwZGY5NjZhNjc2M2Q1NDE3N2Q5ZjNlZWE0ZTlmODBkMzU5MTZkMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiZGphbmdvX2xhbmd1YWdlIjoicGwiLCJfYXV0aF91c2VyX2lkIjoxfQ==','2015-03-19 18:14:50'),('8pbjyr0ck14qenjlmy6b0mvakn7xlwz7','NDgwZGY5NjZhNjc2M2Q1NDE3N2Q5ZjNlZWE0ZTlmODBkMzU5MTZkMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiZGphbmdvX2xhbmd1YWdlIjoicGwiLCJfYXV0aF91c2VyX2lkIjoxfQ==','2015-02-05 21:14:40'),('92qbprqu3hopxfzn4fr1l294wyz3tiv9','NDgwZGY5NjZhNjc2M2Q1NDE3N2Q5ZjNlZWE0ZTlmODBkMzU5MTZkMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiZGphbmdvX2xhbmd1YWdlIjoicGwiLCJfYXV0aF91c2VyX2lkIjoxfQ==','2015-02-01 22:27:49'),('k0h8vdh3hbffpc9y9jwbgjrundnk8eal','NDgwZGY5NjZhNjc2M2Q1NDE3N2Q5ZjNlZWE0ZTlmODBkMzU5MTZkMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiZGphbmdvX2xhbmd1YWdlIjoicGwiLCJfYXV0aF91c2VyX2lkIjoxfQ==','2015-03-19 17:40:57');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) COLLATE utf8_bin NOT NULL,
  `migration` varchar(255) COLLATE utf8_bin NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-05 19:18:49
