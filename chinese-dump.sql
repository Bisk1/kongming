-- MySQL dump 10.13  Distrib 5.6.20, for Win64 (x86_64)
--
-- Host: localhost    Database: chinese_db
-- ------------------------------------------------------
-- Server version	5.6.20-log

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
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add lesson action',7,'add_lessonaction'),(20,'Can change lesson action',7,'change_lessonaction'),(21,'Can delete lesson action',7,'delete_lessonaction'),(22,'Can add exercise action',8,'add_exerciseaction'),(23,'Can change exercise action',8,'change_exerciseaction'),(24,'Can delete exercise action',8,'delete_exerciseaction'),(25,'Can add lesson',9,'add_lesson'),(26,'Can change lesson',9,'change_lesson'),(27,'Can delete lesson',9,'delete_lesson'),(28,'Can add exercise',10,'add_exercise'),(29,'Can change exercise',10,'change_exercise'),(30,'Can delete exercise',10,'delete_exercise'),(31,'Can add typing',11,'add_typing'),(32,'Can change typing',11,'change_typing'),(33,'Can delete typing',11,'delete_typing'),(34,'Can add explanation',12,'add_explanation'),(35,'Can change explanation',12,'change_explanation'),(36,'Can delete explanation',12,'delete_explanation'),(37,'Can add exercise type',13,'add_exercisetype'),(38,'Can change exercise type',13,'change_exercisetype'),(39,'Can delete exercise type',13,'delete_exercisetype'),(40,'Can add subscription',14,'add_subscription'),(41,'Can change subscription',14,'change_subscription'),(42,'Can delete subscription',14,'delete_subscription'),(43,'Can add word skill',15,'add_wordskill'),(44,'Can change word skill',15,'change_wordskill'),(45,'Can delete word skill',15,'delete_wordskill'),(46,'Can add word pl',16,'add_wordpl'),(47,'Can change word pl',16,'change_wordpl'),(48,'Can delete word pl',16,'delete_wordpl'),(49,'Can add word zh',17,'add_wordzh'),(50,'Can change word zh',17,'change_wordzh'),(51,'Can delete word zh',17,'delete_wordzh'),(52,'Can add word translation',18,'add_wordtranslation'),(53,'Can change word translation',18,'change_wordtranslation'),(54,'Can delete word translation',18,'delete_wordtranslation'),(55,'Can add text pl',19,'add_textpl'),(56,'Can change text pl',19,'change_textpl'),(57,'Can delete text pl',19,'delete_textpl'),(58,'Can add text zh',20,'add_textzh'),(59,'Can change text zh',20,'change_textzh'),(60,'Can delete text zh',20,'delete_textzh'),(61,'Can add text translation',21,'add_texttranslation'),(62,'Can change text translation',21,'change_texttranslation'),(63,'Can delete text translation',21,'delete_texttranslation');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$WUg3rwD15oKt$M8BRDtLilFwnmA18Q/tTfRoVFpJBC9sA+MHDVyX/G4M=','2015-07-18 14:09:05',1,'admin','','','',1,1,'2015-07-18 14:08:46');
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-07-18 14:09:30',1,13,'1','Typing (typing) - typing',1,''),(2,'2015-07-18 14:09:42',1,13,'2','Explanation (explanation) - explanation',1,''),(3,'2015-07-19 10:27:53',1,20,'2','sdfsdfsdf',3,''),(4,'2015-07-19 10:27:53',1,20,'1','sdfs',3,'');
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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'lesson action','learn','lessonaction'),(8,'exercise action','learn','exerciseaction'),(9,'lesson','lessons','lesson'),(10,'exercise','exercises','exercise'),(11,'typing','exercises','typing'),(12,'explanation','exercises','explanation'),(13,'exercise type','exercises','exercisetype'),(14,'subscription','users','subscription'),(15,'word skill','users','wordskill'),(16,'word pl','translations','wordpl'),(17,'word zh','translations','wordzh'),(18,'word translation','translations','wordtranslation'),(19,'text pl','translations','textpl'),(20,'text zh','translations','textzh'),(21,'text translation','translations','texttranslation');
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
INSERT INTO `django_session` VALUES ('j8un6sdjttwr87sg5zet9a0qpnw5yjr7','NDgwZGY5NjZhNjc2M2Q1NDE3N2Q5ZjNlZWE0ZTlmODBkMzU5MTZkMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiZGphbmdvX2xhbmd1YWdlIjoicGwiLCJfYXV0aF91c2VyX2lkIjoxfQ==','2015-08-01 14:09:05');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercises_exercise`
--

DROP TABLE IF EXISTS `exercises_exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exercises_exercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lesson_id` int(11) NOT NULL,
  `number` int(11) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exercises_exercise_37003e55` (`lesson_id`),
  KEY `exercises_exercise_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_97fa8206` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `lesson_id_refs_id_a23d54a7` FOREIGN KEY (`lesson_id`) REFERENCES `lessons_lesson` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises_exercise`
--

LOCK TABLES `exercises_exercise` WRITE;
/*!40000 ALTER TABLE `exercises_exercise` DISABLE KEYS */;
INSERT INTO `exercises_exercise` VALUES (8,1,1,12,4),(9,1,2,12,5),(10,1,3,11,5),(11,1,4,12,6),(12,1,5,12,7),(13,1,6,11,6),(14,1,7,12,8),(15,2,1,12,9),(16,2,2,12,10),(17,2,3,11,7),(18,2,4,11,8),(19,2,5,12,11),(20,2,6,11,9),(21,2,7,11,10),(22,2,8,11,11),(23,2,10,11,12),(24,2,9,11,13),(25,3,1,12,12),(30,3,9,11,14),(31,3,8,11,15),(32,3,7,11,16),(33,3,6,11,17),(34,3,5,11,18),(35,3,4,11,19),(36,3,3,11,20),(37,3,2,11,21),(38,3,10,11,22),(39,4,1,12,17),(40,4,2,12,18),(41,4,3,11,23),(43,4,4,11,25),(44,4,6,11,26),(45,4,7,12,19),(47,4,5,11,27),(48,5,1,12,21),(49,5,2,12,22),(50,6,1,12,23),(51,6,2,11,28),(52,6,3,12,24),(53,6,4,12,25),(54,6,5,12,26),(55,6,6,11,29),(56,6,7,11,30);
/*!40000 ALTER TABLE `exercises_exercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercises_exercisetype`
--

DROP TABLE IF EXISTS `exercises_exercisetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exercises_exercisetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8_bin NOT NULL,
  `slug` varchar(20) COLLATE utf8_bin NOT NULL,
  `model_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exercises_exercisetype_29840309` (`model_id`),
  CONSTRAINT `model_id_refs_id_ae3a4766` FOREIGN KEY (`model_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises_exercisetype`
--

LOCK TABLES `exercises_exercisetype` WRITE;
/*!40000 ALTER TABLE `exercises_exercisetype` DISABLE KEYS */;
INSERT INTO `exercises_exercisetype` VALUES (1,'Typing','typing',11),(2,'Explanation','explanation',12);
/*!40000 ALTER TABLE `exercises_exercisetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercises_explanation`
--

DROP TABLE IF EXISTS `exercises_explanation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exercises_explanation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext COLLATE utf8_bin NOT NULL,
  `image` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises_explanation`
--

LOCK TABLES `exercises_explanation` WRITE;
/*!40000 ALTER TABLE `exercises_explanation` DISABLE KEYS */;
INSERT INTO `exercises_explanation` VALUES (4,'Podczas pierwszej lekcji nauczysz się, jak wpisywać tekst w postaci chińskich znaków za pomocą zwykłej klawiatury.',''),(5,'Na kolejnym slajdzie pojawi się słowo \'ja\' do przetłumaczenia z języka polskiego na chiński. Puste pole przygotowane jest do wypełnienia chińskimi znakami. Gdy będziesz pisał zwykłe litery (łacińskie) przy pomocy klawiatury, pojawią się chińskie znaki odpowiadające Twoim. Wprowadź transliterację \'wo\' i wybierz pierwszą odpowiedź klikając ją lewym przyciskiem myszy lub klawiszem \'1\'.',''),(6,'Ten sposób zapisu nazywa się \"pinyin\". Jest to obecnie najpowszechniejsza metoda zapisu chińskich znaków za pomocą liter łacińskich. Tutaj możesz z niego korzystać na każdej lekcji.',''),(7,'Teraz czeka Cię odwrotne zadanie. Przetłumacz chiński znak 我 na słowo polskie (to samo które tłumaczyłeś przed chwilą)',''),(8,'Znasz już zasady działania - możesz zapoznać się z kolejnymi lekcjami!',''),(9,'ja - 我',''),(10,'ty - 你',''),(11,'on - 他\r\nona - 她',''),(12,'Liczba mnoga jest tworzona w prosty sposób - przez dodanie znaku 们 na końcu:\r\n我们 - my\r\n你们 - wy\r\n他们 - oni\r\n她们 - one (o kobietach)\r\n它们 - one (o zwierzętach i rzeczach)',''),(17,'Najprostsze przywitanie to 你好！, czyli \"Cześć!\". Powstaje ono przez połączenie 你 (ty) i 好 (dobry). Jeżeli zwracasz się do wielu osób, lepiej użyć jednej z form:\r\n您好 - cześć wam\r\nlub\r\n大家好 - cześć wszystkim',''),(18,'Nieco bardziej formalnym zwrotem jest:\r\n您好!\r\nSłowo 您 również oznacza drugą osobę liczby pojedynczej (\"ty\"), ale jest używane w zwrotach grzecznościowych.\r\nNie ma zwrotu 您们好 - jeżeli zwracasz się w sposób grzecznościowy do grupy osób, możesz również użyć formy 您.',''),(19,'Zwrot 你好 nie jest tak potoczny jak polskie \"cześć\", możesz go więc używać wobec obcych lub starszych od ciebie osób.',''),(21,'Język mandaryński (podobnie jak inne odmiany chińskiego) jest językiem tonalnym. Oznacza to, że intonacja słów wyraża nie tylko emocje mówcy, ale także nadaje słowom znaczenie. Jedno słowo, wymówione na 4 sposoby, za każdym razem na inną melodię, będzie nieodróżnialne dla niewprawnego słuchacza, ale może oznaczać 4 całkowicie różne rzeczy dla Chińczyka!\r\nPrzykład:\r\n妈 - mama\r\n马 - koń\r\n麻 - konopia\r\n吗 - nakrzyczeć na kogoś',''),(22,'Pierwszy ton jest płaski i wysoki. W pinyin oznacza się go płaską linią nad literą lub cyfrą 1, na przykład:\r\n妈\r\n他\r\n发',''),(23,'jak się masz? - 你好吗？\r\nDosłownie: ty dobrze?\r\nZwrot 吗 na końcu sygnalizuje pytanie. Zwykle na tego rodzaju pytanie można odpowiedzieć \"tak\" lub \"nie\"',''),(24,'我很好！- Dobrze！\r\nDosłownie: Ja bardzo dobrze! To typowa odpowiedź na to pytanie.',''),(25,'Aby zadać to samo pytanie rozmówcy, skorzystaj z frazy: \r\n你呢？ - A ty?',''),(26,'Zwrot 呢 dodany na końcu odnosi zadane wcześniej pytanie na kogoś lub coś innego, np. tego, kto jako pierwszy je zadał. Jest więc odpowiednikiem polskiego \"A ...\" na początku zdania, np. A ty? A oni? A jutro?','');
/*!40000 ALTER TABLE `exercises_explanation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercises_typing`
--

DROP TABLE IF EXISTS `exercises_typing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exercises_typing` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exercises_typing_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_73863d1b` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises_typing`
--

LOCK TABLES `exercises_typing` WRITE;
/*!40000 ALTER TABLE `exercises_typing` DISABLE KEYS */;
INSERT INTO `exercises_typing` VALUES (5,19,3),(6,20,3),(7,19,3),(8,19,4),(9,19,5),(10,20,4),(11,20,3),(12,19,6),(13,20,5),(14,20,6),(15,19,7),(16,20,7),(17,20,8),(18,20,9),(19,19,8),(20,19,9),(21,20,10),(22,20,11),(23,19,10),(25,20,13),(26,19,11),(27,20,14),(28,20,17),(29,19,16),(30,20,19);
/*!40000 ALTER TABLE `exercises_typing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learn_exerciseaction`
--

DROP TABLE IF EXISTS `learn_exerciseaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `learn_exerciseaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` int(11) NOT NULL,
  `lesson_action_id` int(11) NOT NULL,
  `result` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `learn_exerciseaction_c18e0af4` (`exercise_id`),
  KEY `learn_exerciseaction_ff58a6f6` (`lesson_action_id`),
  CONSTRAINT `exercise_id_refs_id_89ff9a05` FOREIGN KEY (`exercise_id`) REFERENCES `exercises_exercise` (`id`),
  CONSTRAINT `lesson_action_id_refs_id_65a41530` FOREIGN KEY (`lesson_action_id`) REFERENCES `learn_lessonaction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learn_exerciseaction`
--

LOCK TABLES `learn_exerciseaction` WRITE;
/*!40000 ALTER TABLE `learn_exerciseaction` DISABLE KEYS */;
INSERT INTO `learn_exerciseaction` VALUES (7,25,9,0,1),(52,15,14,0,1),(53,16,14,0,2),(54,17,14,0,3),(55,18,14,0,4),(56,19,14,0,5),(57,20,14,0,6),(58,21,14,0,7),(59,22,14,0,8),(60,24,14,0,9),(61,23,14,0,10),(62,20,14,0,11);
/*!40000 ALTER TABLE `learn_exerciseaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learn_lessonaction`
--

DROP TABLE IF EXISTS `learn_lessonaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `learn_lessonaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `total_exercises_number` int(11) NOT NULL,
  `current_exercise_number` int(11) NOT NULL,
  `fails` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  `status` varchar(1) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `learn_lessonaction_6340c63c` (`user_id`),
  KEY `learn_lessonaction_37003e55` (`lesson_id`),
  CONSTRAINT `lesson_id_refs_id_620aeb9f` FOREIGN KEY (`lesson_id`) REFERENCES `lessons_lesson` (`id`),
  CONSTRAINT `user_id_refs_id_52d756df` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learn_lessonaction`
--

LOCK TABLES `learn_lessonaction` WRITE;
/*!40000 ALTER TABLE `learn_lessonaction` DISABLE KEYS */;
INSERT INTO `learn_lessonaction` VALUES (1,5,0,0,1,1,NULL),(2,0,0,0,1,3,'p'),(9,1,1,0,1,3,NULL),(14,11,3,0,1,2,NULL);
/*!40000 ALTER TABLE `learn_lessonaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lessons_lesson`
--

DROP TABLE IF EXISTS `lessons_lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lessons_lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(100) COLLATE utf8_bin NOT NULL,
  `exercises_number` int(11) NOT NULL,
  `requirement_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lessons_lesson_19c1813d` (`requirement_id`),
  CONSTRAINT `requirement_id_refs_id_7179d31e` FOREIGN KEY (`requirement_id`) REFERENCES `lessons_lesson` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lessons_lesson`
--

LOCK TABLES `lessons_lesson` WRITE;
/*!40000 ALTER TABLE `lessons_lesson` DISABLE KEYS */;
INSERT INTO `lessons_lesson` VALUES (1,'Witaj!',7,NULL),(2,'Osoba - liczba pojedyncza',11,1),(3,'Osoba - liczba mnoga',10,2),(4,'Przywitanie',7,3),(5,'Tony',2,1),(6,'Jak się masz?',7,2);
/*!40000 ALTER TABLE `lessons_lesson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `translations_textpl`
--

DROP TABLE IF EXISTS `translations_textpl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `translations_textpl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `text` (`text`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `translations_textpl`
--

LOCK TABLES `translations_textpl` WRITE;
/*!40000 ALTER TABLE `translations_textpl` DISABLE KEYS */;
INSERT INTO `translations_textpl` VALUES (17,'A on?'),(15,'Cześć wam!'),(14,'Cześć wszystkim!'),(10,'Cześć!'),(11,'Cześć! (grzecznościowo)'),(1,'Jak się masz?'),(16,'Mam się dobrze.'),(2,'asdasd'),(3,'ja'),(7,'my'),(6,'on'),(5,'ona'),(13,'one'),(9,'oni'),(4,'ty'),(8,'wy'),(12,'她们');
/*!40000 ALTER TABLE `translations_textpl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `translations_texttranslation`
--

DROP TABLE IF EXISTS `translations_texttranslation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `translations_texttranslation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text_zh_id` int(11) NOT NULL,
  `text_pl_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `text_zh_id` (`text_zh_id`,`text_pl_id`),
  KEY `translations_texttranslation_b17d8cc8` (`text_zh_id`),
  KEY `translations_texttranslation_00218c61` (`text_pl_id`),
  CONSTRAINT `text_pl_id_refs_id_7889d818` FOREIGN KEY (`text_pl_id`) REFERENCES `translations_textpl` (`id`),
  CONSTRAINT `text_zh_id_refs_id_d5e3d032` FOREIGN KEY (`text_zh_id`) REFERENCES `translations_textzh` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `translations_texttranslation`
--

LOCK TABLES `translations_texttranslation` WRITE;
/*!40000 ALTER TABLE `translations_texttranslation` DISABLE KEYS */;
INSERT INTO `translations_texttranslation` VALUES (7,3,3),(9,4,6),(8,5,4),(3,6,8),(5,7,13),(4,8,12),(2,9,9),(1,10,7),(6,11,13),(10,12,5),(12,13,10),(13,13,14),(16,14,10),(17,14,15),(11,15,10),(15,16,10),(14,16,11),(18,17,1),(19,18,16),(20,19,17);
/*!40000 ALTER TABLE `translations_texttranslation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `translations_textzh`
--

DROP TABLE IF EXISTS `translations_textzh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `translations_textzh` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `text` (`text`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `translations_textzh`
--

LOCK TABLES `translations_textzh` WRITE;
/*!40000 ALTER TABLE `translations_textzh` DISABLE KEYS */;
INSERT INTO `translations_textzh` VALUES (8,'one'),(4,'他'),(9,'他们'),(19,'他呢？'),(5,'你'),(6,'你们'),(14,'你们好！'),(17,'你好吗？'),(15,'你好！'),(13,'大家好!'),(12,'她'),(7,'她们'),(11,'它们'),(16,'您好！'),(3,'我'),(10,'我们'),(18,'我很好。');
/*!40000 ALTER TABLE `translations_textzh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `translations_wordpl`
--

DROP TABLE IF EXISTS `translations_wordpl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `translations_wordpl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `word` (`word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `translations_wordpl`
--

LOCK TABLES `translations_wordpl` WRITE;
/*!40000 ALTER TABLE `translations_wordpl` DISABLE KEYS */;
/*!40000 ALTER TABLE `translations_wordpl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `translations_wordtranslation`
--

DROP TABLE IF EXISTS `translations_wordtranslation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `translations_wordtranslation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word_zh_id` int(11) NOT NULL,
  `word_pl_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `word_zh_id` (`word_zh_id`,`word_pl_id`),
  KEY `translations_wordtranslation_e5b47d84` (`word_zh_id`),
  KEY `translations_wordtranslation_1ac5d68e` (`word_pl_id`),
  CONSTRAINT `word_pl_id_refs_id_e4386972` FOREIGN KEY (`word_pl_id`) REFERENCES `translations_wordpl` (`id`),
  CONSTRAINT `word_zh_id_refs_id_11323b48` FOREIGN KEY (`word_zh_id`) REFERENCES `translations_wordzh` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `translations_wordtranslation`
--

LOCK TABLES `translations_wordtranslation` WRITE;
/*!40000 ALTER TABLE `translations_wordtranslation` DISABLE KEYS */;
/*!40000 ALTER TABLE `translations_wordtranslation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `translations_wordzh`
--

DROP TABLE IF EXISTS `translations_wordzh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `translations_wordzh` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(50) COLLATE utf8_bin NOT NULL,
  `pinyin` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `word` (`word`,`pinyin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `translations_wordzh`
--

LOCK TABLES `translations_wordzh` WRITE;
/*!40000 ALTER TABLE `translations_wordzh` DISABLE KEYS */;
/*!40000 ALTER TABLE `translations_wordzh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_subscription`
--

DROP TABLE IF EXISTS `users_subscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_subscription` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_id` int(11) NOT NULL,
  `registration_date` datetime NOT NULL,
  `last_login_date` datetime NOT NULL,
  `abo_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_subscription_4da47e07` (`name_id`),
  CONSTRAINT `name_id_refs_id_f0ccbbf7` FOREIGN KEY (`name_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_subscription`
--

LOCK TABLES `users_subscription` WRITE;
/*!40000 ALTER TABLE `users_subscription` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_subscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_wordskill`
--

DROP TABLE IF EXISTS `users_wordskill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_wordskill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word_zh_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `last_time` datetime NOT NULL,
  `correct` int(11) NOT NULL,
  `correct_run` int(11) NOT NULL,
  `wrong` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_wordskill_e5b47d84` (`word_zh_id`),
  KEY `users_wordskill_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_2045ed5a` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `word_zh_id_refs_id_0a0dcba0` FOREIGN KEY (`word_zh_id`) REFERENCES `translations_wordzh` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_wordskill`
--

LOCK TABLES `users_wordskill` WRITE;
/*!40000 ALTER TABLE `users_wordskill` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_wordskill` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-20 18:57:41
