-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: otzo.angeljovenfes.mx    Database: otzo
-- ------------------------------------------------------
-- Server version	8.4.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administracion`
--

DROP TABLE IF EXISTS `administracion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administracion` (
  `id_empleado` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido_paterno` varchar(50) DEFAULT NULL,
  `apellido_materno` varchar(50) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `genero` enum('Masculino','Femenino') DEFAULT NULL,
  `direccion_calle` varchar(100) DEFAULT NULL,
  `direccion_colonia` varchar(100) DEFAULT NULL,
  `direccion_codigopostal` int DEFAULT NULL,
  `direccion_estado` varchar(100) DEFAULT NULL,
  `direccion_municipio` varchar(100) DEFAULT NULL,
  `contacto_correo` varchar(100) DEFAULT NULL,
  `contraseña` varchar(8) DEFAULT NULL,
  `contacto_telefono` varchar(15) DEFAULT NULL,
  `area_Trabajo` enum('Almacen','Administracion','Clientes','DBA','Fidelizacion','Reabastecimiento','Ventas','Servicio al cliente') DEFAULT NULL,
  `fechaDe_Alta` datetime DEFAULT NULL,
  `ultimo_acceso` datetime DEFAULT NULL,
  `estado_cuenta` enum('Activo','Inactivo','Suspendido','Baneado') DEFAULT NULL,
  PRIMARY KEY (`id_empleado`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administracion`
--

LOCK TABLES `administracion` WRITE;
/*!40000 ALTER TABLE `administracion` DISABLE KEYS */;
INSERT INTO `administracion` VALUES (1,'BRYAN URIEL','ALMARAZ','BAÑOS','2000-10-26','Masculino','Calle de la Industria 123','Centro',54060,'Estado de México','Tlalnepantla de Baz','alorn9553@gmail.com','123456','5589674321','Reabastecimiento','2024-11-20 04:13:03','2024-11-20 04:13:03','Inactivo'),(2,'IAN DORIAN','FLORES','MENESES','2000-06-10','Masculino','Avenida de los Inventarios 456','Colonia Norte',53400,'Estado de México','Naucalpan','ianflores420@aragon.unam.mx','123456','5652417035','Almacen','2024-11-20 04:13:03','2024-11-20 04:13:03','Inactivo'),(3,'ANGEL CRISTIAN','JOVEN','JIMENEZ','2000-11-03','Masculino','Boulevard Creativo 789','Colonia Este',56106,'Estado de México','Texcoco','cchangeljoven@gmail.com','123456','5622584107','Fidelizacion','2024-11-20 04:13:03','2024-12-05 09:42:06','Activo'),(4,'LEONARDO DANIEL','MARTINEZ','RIOS','2000-02-27','Masculino','Calle Data Center 321','Residencial Sur',51200,'Estado de México','Valle de Bravo','leoyforce777@gmail.com','123456','5665782413','DBA','2024-11-20 04:13:03','2024-11-20 04:13:03','Activo'),(5,'SAMANTHA QUETZALLI','MATLALCUATZI','MARTINEZ','2000-01-22','Femenino','Avenida Gestión 654','Colonia Centro',52166,'Estado de México','Metepec','sam443510@gmail.com','123456','5519556832','Administracion','2024-11-20 04:13:03','2024-11-29 13:26:02','Inactivo'),(6,'KEVIN','MENDOZA','LUGO','2000-06-18','Masculino','Calle Clientes 987','Colonia Poniente',55600,'Estado de México','Zumpango','kevinmendozalugo@gmail.com','123456','5584623591','Clientes','2024-11-20 04:13:03','2024-11-20 04:13:03','Inactivo'),(7,'JULIO CESAR','NEGRETE','GUTIERREZ','2000-09-30','Masculino','Boulevard Ventas 741','Colonia Alta',52966,'Estado de México','Atizapán de Zaragoza','julionegrete97@aragon.unam.mx','123456','5502065371','Ventas','2024-11-20 04:13:03','2024-11-20 04:13:03','Activo'),(8,'LUIS GIOVANNI','RIVERA','ROJAS','2000-07-03','Masculino','Calle Atención 852','Colonia Baja',56337,'Estado de México','Chimalhuacán','giovannirivera45@aragon.unam.mx','123456','5624685739','Servicio al cliente','2024-11-20 04:13:03','2024-11-20 04:13:03','Activo'),(11,'admin','_','_','2024-11-29','Masculino','SIN DATO','SIN DATO',0,'SIN DATO','SIN DATO','admin@otzo.com','123456','00000000','Administracion','2024-11-29 12:38:11','2024-12-07 00:44:44','Activo'),(12,'ROBERTO MISAEL','SOBERANES','JAIME','2024-11-29','Masculino','_','_',0,'_','_','misaelsoberanesr8@aragon.unam.mx','12345678','00000000','Administracion','2024-11-29 13:19:05','2024-12-05 20:30:05','Activo'),(13,'adminServer','_','_','2024-12-05','Masculino','_','_',0,'_','_','admin@example.com','123456','00000000','Administracion','2024-12-05 09:40:59','2024-12-05 09:41:23','Inactivo');
/*!40000 ALTER TABLE `administracion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `idCliente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido_paterno` varchar(50) DEFAULT NULL,
  `apellido_materno` varchar(50) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `genero` enum('Masculino','Femenino') DEFAULT NULL,
  `direccion_calle` varchar(100) DEFAULT NULL,
  `direccion_colonia` varchar(100) DEFAULT NULL,
  `direccion_codigopostal` int DEFAULT NULL,
  `direccion_estado` varchar(100) DEFAULT NULL,
  `direccion_municipio` varchar(100) DEFAULT NULL,
  `contacto_correo` varchar(100) DEFAULT NULL,
  `contraseña` varchar(8) DEFAULT NULL,
  `contacto_telefono` varchar(15) DEFAULT NULL,
  `fechaDe_Alta` datetime DEFAULT NULL,
  `ultimo_acceso` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `estado_cuenta` enum('Activo','Inactivo','Suspendido') DEFAULT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Juan','Perez','Lopez','1985-05-10','Masculino','Calle Reforma 12','Centro Histórico',60000,'Ciudad de México','Cuauhtémoc','juan.perez@example.com','12345678','5551234567','2024-11-20 04:07:59','2024-12-07 01:25:22','Activo'),(2,'Maria','Gomez','Hernandez','1992-11-25','Femenino','Avenida Insurgentes 456','Colonia Roma',67600,'Ciudad de México','Cuauhtémoc','maria.gomez@example.com','12345678','5552345678','2024-11-20 04:07:59','2024-12-05 23:17:19','Activo'),(3,'Luis','Martinez','Garcia','1980-07-14','Masculino','Calle Juárez 789','Colonia Del Valle',3100,'Ciudad de México','Benito Juárez','luis.martinez@example.com','12345678','5553456789','2024-11-20 04:07:59','2024-11-20 10:07:59','Activo'),(4,'Ana','Rodriguez','Sanchez','1995-12-30','Femenino','Calle Madero 321','Colonia Condesa',6140,'Ciudad de México','Cuauhtémoc','ana.rodriguez@example.com','12345678','5554567890','2024-11-20 04:07:59','2024-11-20 10:07:59','Activo'),(5,'Carlos','Lopez','Jimenez','1988-02-19','Masculino','Avenida Universidad 654','Coyoacán',4000,'Ciudad de México','Coyoacán','carlos.lopez@example.com','12345678','5555678901','2024-11-20 04:07:59','2024-12-02 07:49:25','Inactivo'),(6,'Sofia','Ramirez','Torres','1999-03-07','Femenino','Paseo de la Reforma 987','Colonia Polanco',11560,'Ciudad de México','Miguel Hidalgo','sofia.ramirez@example.com','12345678','5556789012','2024-11-20 04:07:59','2024-11-20 10:07:59','Activo'),(7,'Fernando','Diaz','Ortega','1975-08-23','Masculino','Calle Tacuba 741','Centro Histórico',6010,'Ciudad de México','Cuauhtémoc','fernando.diaz@example.com','12345678','5557890123','2024-11-20 04:07:59','2024-11-20 10:07:59','Inactivo'),(8,'Laura','Ruiz','Navarro','2001-04-11','Femenino','Avenida Revolución 852','San Ángel',1000,'Ciudad de México','Álvaro Obregón','laura.ruiz@example.com','12345678','5558901234','2024-11-20 04:07:59','2024-11-20 10:07:59','Inactivo'),(9,'Pedro','Hernandez','Ramos','1983-09-17','Masculino','Calle Pino Suárez 963','Centro Histórico',6090,'Ciudad de México','Cuauhtémoc','pedro.hernandez@example.com','12345678','5559012345','2024-11-20 04:07:59','2024-12-02 07:51:39','Suspendido'),(10,'Lucia','Castro','Paredes','1996-06-02','Femenino','Calle Londres 159','Zona Rosa',6600,'Ciudad de México','Cuauhtémoc','lucia.castro@example.com','12345678','5550123456','2024-11-20 04:07:59','2024-11-20 10:07:59','Suspendido'),(19,'cliente','_','_',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'cliente@otzo.com','123456',NULL,'2024-11-29 13:24:07','2024-11-29 19:24:12','Activo'),(20,'Roberto Misael','Soberanes','Jaime','2024-11-29','Masculino','_','_',0,'_','_','misaelsoberanesr8@aragon.unam.mx','12345678','00000000','2024-11-29 13:29:20','2024-12-06 02:28:59','Activo'),(21,'clienteServer2','_','_','2024-12-05','Masculino','_','_',0,'_','_','cliente@example.com','123456','00000000','2024-12-05 09:38:05','2024-12-05 16:02:00','Inactivo'),(22,'clienteServer','_','_','2024-12-05','Masculino','_','_',0,'_','_','cliente2@example.com','123456','00000000','2024-12-05 09:43:51','2024-12-05 16:13:11','Activo'),(23,'Moisés','Montiel','Ríos','2024-12-06','Masculino','Orizaba','Estado de Veracruz',9856,'CDMX','Iztapalapa','songugeta@gmail.com','123456','5538823857','2024-12-05 20:27:53','2024-12-06 02:31:56','Activo'),(24,'Vianey','Moreno','Acosta',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'moreno121202@gmail.com','123456',NULL,'2024-12-06 19:22:45','2024-12-07 01:23:12','Activo');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_inventario`
--

DROP TABLE IF EXISTS `detalle_inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_inventario` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `id_inventario` int DEFAULT NULL,
  `codigo_producto` varchar(10) DEFAULT NULL,
  `fecha_producto` datetime DEFAULT NULL,
  `caducidad_producto` datetime DEFAULT NULL,
  `costo_unitario` decimal(10,2) DEFAULT NULL,
  `vendido` tinyint(1) DEFAULT '0',
  `devuelto` tinyint DEFAULT NULL,
  PRIMARY KEY (`id_producto`),
  UNIQUE KEY `codigo_producto_UNIQUE` (`codigo_producto`),
  KEY `id_inventario_idx` (`id_inventario`),
  CONSTRAINT `id_inventario` FOREIGN KEY (`id_inventario`) REFERENCES `inventario` (`id_inventario`)
) ENGINE=InnoDB AUTO_INCREMENT=205 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_inventario`
--

LOCK TABLES `detalle_inventario` WRITE;
/*!40000 ALTER TABLE `detalle_inventario` DISABLE KEYS */;
INSERT INTO `detalle_inventario` VALUES (1,1,'LYHK3CXB','2024-11-28 19:05:45','2024-12-28 19:05:45',13.08,1,0),(2,1,'I8STD17L','2024-11-28 19:05:45','2024-12-28 19:05:45',13.08,1,0),(3,1,'6NR79NJX','2024-11-28 19:05:45','2024-12-28 19:05:45',13.08,1,0),(4,1,'FJLQMB77','2024-11-28 19:05:45','2024-12-28 19:05:45',13.08,1,0),(5,1,'65SOTCJG','2024-11-28 19:05:45','2024-12-28 19:05:45',13.08,1,0),(6,1,'I5ZJX8RL','2024-11-28 19:05:45','2024-12-28 19:05:45',13.08,1,0),(7,1,'0GD1VZY0','2024-11-28 19:05:45','2024-12-28 19:05:45',13.08,1,0),(8,1,'0RTNOWEP','2024-11-28 19:05:45','2024-12-28 19:05:45',13.08,1,0),(9,1,'ID0E5P60','2024-11-28 19:05:45','2024-12-28 19:05:45',13.08,1,0),(10,1,'VBVTAMAA','2024-11-28 19:05:45','2024-12-28 19:05:45',13.08,1,0),(11,1,'JNCNG6MQ','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(12,1,'HMENK3CI','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(13,1,'A95IFQR2','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(14,1,'LW5VNAYE','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(15,1,'BM3KWDW9','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(16,1,'I5LCL2FT','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(17,1,'RKB2PJH3','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(18,1,'QNUDWKH2','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(19,1,'UG8FYTWJ','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(20,1,'S3615036','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(21,1,'8TTTQOYJ','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(22,1,'PJNLHFL5','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(23,1,'ZYFN79DF','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(24,1,'JOLR2DGC','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(25,1,'ZNOOIYHT','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(26,1,'JO7MPX8R','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(27,1,'6QVB265M','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,1,0),(28,1,'4UBBYV9D','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(29,1,'K4XQWFZ3','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(30,1,'F1Q9O4TM','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(31,1,'PMSJBANN','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(32,1,'BB3LCL0T','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(33,1,'QHDKLFDR','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(34,1,'GUHIUAJ6','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(35,1,'QT25PN0G','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(36,1,'RL7F0QHK','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(37,1,'SG41431Y','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(38,1,'2LEPLDLK','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(39,1,'J4R98X39','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(40,1,'0I4J0YAZ','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(41,1,'BA7T5LKO','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(42,1,'NWFC4U10','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(43,1,'JVFTD7MN','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(44,1,'C8GM21P2','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(45,1,'4LSPZJJ0','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(46,1,'IEGSLCDK','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(47,1,'9WJA1YJQ','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(48,1,'WFQX9VI5','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(49,1,'Q92PRZCA','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(50,1,'90J5MQSD','2024-11-28 19:06:10','2024-12-28 19:06:10',16.05,0,0),(51,2,'PB3DEZ2R','2024-11-28 19:09:29','2024-12-28 19:09:29',5.59,1,0),(52,2,'T48O7ZBC','2024-11-28 19:09:29','2024-12-28 19:09:29',5.59,1,0),(53,2,'ZQ3WHRNR','2024-11-28 19:09:29','2024-12-28 19:09:29',5.59,1,0),(54,2,'423LMQXO','2024-11-28 19:09:29','2024-12-28 19:09:29',5.59,1,0),(55,2,'8W722L9B','2024-11-28 19:09:29','2024-12-28 19:09:29',5.59,1,0),(56,2,'EYLCVSHD','2024-11-28 19:09:29','2024-12-28 19:09:29',5.59,0,0),(57,2,'MDUO7LC4','2024-11-28 19:09:29','2024-12-28 19:09:29',5.59,0,0),(58,2,'XJLOTYIY','2024-11-28 19:09:29','2024-12-28 19:09:29',5.59,0,0),(59,2,'A3WQLE97','2024-11-28 19:09:29','2024-12-28 19:09:29',5.59,0,0),(60,2,'QSBRGH2J','2024-11-28 19:09:29','2024-12-28 19:09:29',5.59,0,0),(61,8,'S1790LJQ','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,1,0),(62,8,'VW6B5AE0','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(63,8,'KUFHJDFF','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(64,8,'JCZZ3U99','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(65,8,'AA54AKRG','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(66,8,'CR4YH7VW','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(67,8,'0Q6N7VR2','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(68,8,'ID9MOOWG','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(69,8,'H6BV6IYQ','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(70,8,'FJZJ0DD8','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(71,8,'MAXAKFI9','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(72,8,'RE22P8G5','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(73,8,'68WPQBHC','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(74,8,'879D1Y4W','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(75,8,'KGCW8ZJ0','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(76,8,'3CCRUBVA','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(77,8,'OUKABNQ3','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(78,8,'EDYB2HGD','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(79,8,'WJX6RYC3','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(80,8,'492KNLUB','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(81,8,'NCOQEQAN','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(82,8,'G5I3ARA2','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(83,8,'L9Y4H9BV','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(84,8,'6SXW59I7','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(85,8,'ZTM27R9I','2024-11-28 19:22:46','2024-12-28 19:22:46',15.23,0,0),(86,7,'KQTM0SEY','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,1,0),(87,7,'CSE6MQQV','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,1,0),(88,7,'XVGUYYA1','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(89,7,'3BXF4ZVS','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(90,7,'60XI3AQX','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(91,7,'BVLDYWRX','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(92,7,'J6G1VGFP','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(93,7,'MX95CXKQ','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(94,7,'TFM5VGEH','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(95,7,'OKRN3563','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(96,7,'0NHPN5LB','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(97,7,'AIPZ16I7','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(98,7,'RLD0AQLF','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(99,7,'KD9LEJPY','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(100,7,'2VCK6J3B','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(101,7,'XF1DVHBE','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(102,7,'HKY6FGQ4','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(103,7,'4O8WENA6','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(104,7,'1QS4TUE1','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(105,7,'MTP642FR','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(106,7,'UPQTSGDA','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(107,7,'GNQUWVBK','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(108,7,'BUKMOP4O','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(109,7,'W88U0OKJ','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(110,7,'AU5PFN67','2024-11-28 22:17:16','2024-12-28 22:17:16',2.79,0,0),(111,3,'ZDVU0V7J','2024-11-30 17:05:28','2024-12-30 17:05:28',11.82,1,0),(112,3,'MIC8YJ7R','2024-11-30 17:05:28','2024-12-30 17:05:28',11.82,0,0),(113,3,'9Y3B4D9D','2024-11-30 17:05:28','2024-12-30 17:05:28',11.82,0,0),(114,3,'VM2GU2GK','2024-11-30 17:05:28','2024-12-30 17:05:28',11.82,0,0),(115,3,'Q2GW74L8','2024-11-30 17:05:28','2024-12-30 17:05:28',11.82,0,0),(116,3,'FWZYAY3Y','2024-11-30 17:05:28','2024-12-30 17:05:28',11.82,0,0),(117,3,'F6VSD1K4','2024-11-30 17:05:28','2024-12-30 17:05:28',11.82,0,0),(118,3,'AAUDTZG8','2024-11-30 17:05:28','2024-12-30 17:05:28',11.82,0,0),(119,3,'5F6B7N9K','2024-11-30 17:05:28','2024-12-30 17:05:28',11.82,0,0),(120,3,'Q0VVH282','2024-11-30 17:05:28','2024-12-30 17:05:28',11.82,0,0),(121,9,'K218Z43X','2024-11-30 18:21:19','2024-12-30 18:21:19',7165.51,1,0),(122,6,'Y8KYPUMN','2024-11-30 20:05:44','2024-12-30 20:05:44',19.46,1,0),(123,6,'2T0E09GM','2024-11-30 20:05:44','2024-12-30 20:05:44',19.46,1,0),(124,6,'LTJMV8PC','2024-11-30 20:05:44','2024-12-30 20:05:44',19.46,0,0),(125,6,'BA35K7GG','2024-11-30 20:05:44','2024-12-30 20:05:44',19.46,0,0),(126,6,'X26Y60YJ','2024-11-30 20:05:44','2024-12-30 20:05:44',19.46,0,0),(127,6,'4VMXCDCA','2024-11-30 20:05:44','2024-12-30 20:05:44',19.46,0,0),(128,6,'MLA0ZTJD','2024-11-30 20:05:44','2024-12-30 20:05:44',19.46,0,0),(129,6,'9FHTJ8NS','2024-11-30 20:05:44','2024-12-30 20:05:44',19.46,0,0),(130,6,'XQXJ4JMX','2024-11-30 20:05:44','2024-12-30 20:05:44',19.46,0,0),(131,6,'C0DJHQ8Y','2024-11-30 20:05:44','2024-12-30 20:05:44',19.46,0,0),(132,3,'MJSUWWAD','2024-12-01 00:39:53','2024-12-31 00:39:53',16.55,0,0),(133,3,'VZCT52JK','2024-12-01 00:39:53','2024-12-31 00:39:53',16.55,0,0),(134,3,'9AFAH60S','2024-12-01 00:39:53','2024-12-31 00:39:53',16.55,0,0),(135,9,'U8D3NXUH','2024-12-02 01:54:01','2025-01-01 01:54:01',6242.98,1,0),(136,11,'JLC5QF7L','2024-12-02 01:55:55','2025-01-01 01:55:55',8172.80,1,0),(137,12,'MCIXLAX9','2024-12-03 02:22:44','2025-01-02 02:22:44',3.03,0,0),(138,12,'7NH2JM26','2024-12-03 02:22:44','2025-01-02 02:22:44',3.03,0,0),(139,12,'EJJMN20C','2024-12-03 02:22:44','2025-01-02 02:22:44',3.03,0,0),(140,12,'G1IVCKHL','2024-12-03 02:22:44','2025-01-02 02:22:44',3.03,0,0),(141,12,'LVFGX5E0','2024-12-03 02:22:44','2025-01-02 02:22:44',3.03,0,0),(142,13,'MGJ6DDCS','2024-12-03 02:45:40','2025-01-02 02:45:40',39.92,0,0),(143,13,'ES2KFNSD','2024-12-03 02:45:40','2025-01-02 02:45:40',39.92,0,0),(144,13,'93G3N7GG','2024-12-03 02:45:40','2025-01-02 02:45:40',39.92,0,0),(145,13,'IA83575K','2024-12-03 02:45:40','2025-01-02 02:45:40',39.92,0,0),(146,13,'TGYTI10J','2024-12-03 02:45:40','2025-01-02 02:45:40',39.92,0,0),(147,13,'YUKKWB6V','2024-12-03 02:45:40','2025-01-02 02:45:40',39.92,0,0),(148,13,'45KP4MV0','2024-12-03 02:45:40','2025-01-02 02:45:40',39.92,0,0),(149,13,'PLHKC3CX','2024-12-03 02:45:40','2025-01-02 02:45:40',39.92,0,0),(150,11,'LTX3KKAR','2024-12-03 13:55:41','2025-01-02 13:55:41',1470.12,1,0),(151,11,'1R9M0CK8','2024-12-03 14:18:25','2025-01-02 14:18:25',7876.99,0,0),(152,14,'2TOBGXLM','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,1,0),(153,14,'6A29MK9V','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(154,14,'KLJKFNVE','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(155,14,'J2GMVMDN','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(156,14,'NFLUTRLA','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(157,14,'Z5LMA6CH','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(158,14,'RVGFNY8O','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(159,14,'B6D21CB8','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(160,14,'PK1A1X80','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(161,14,'BNLZUKBP','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(162,14,'VY0U31TG','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(163,14,'H3FS7YXR','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(164,14,'CQ3OVP7S','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(165,14,'WAI68MMO','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(166,14,'59AFD1P8','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(167,14,'VLBHRTN9','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(168,14,'WUFZPEDG','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(169,14,'EK7VSEMQ','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(170,14,'ITXG75MX','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(171,14,'NWNAJJDZ','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(172,14,'B9GKMKCX','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(173,14,'GHE0MLR8','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(174,14,'HQ058U32','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(175,14,'K8C2NT71','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(176,14,'GL66O4HL','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(177,14,'DASJ3OMC','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(178,14,'GUCQKZRW','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(179,14,'HK59Q07D','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(180,14,'F0BLTFJL','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(181,14,'M0HXP437','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(182,14,'5U6X9W43','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(183,14,'6BWALZIV','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(184,14,'ALCVG5XI','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(185,14,'6DZ0N8IG','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(186,14,'CS7HBHSJ','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(187,14,'LFQG437J','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(188,14,'WWRZ2305','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(189,14,'056G4T83','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(190,14,'PGUQM3G4','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(191,14,'T4Q03IYW','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(192,14,'W9VFM04O','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(193,14,'WOGGE3HF','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(194,14,'MTNBG5AR','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(195,14,'0IDDWOOO','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(196,14,'PMJGIWWM','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(197,14,'RFCCTDZO','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(198,14,'DLM17ZRI','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(199,14,'CAK035V9','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(200,14,'9QGOC8CZ','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(201,14,'HYY81Y5P','2024-12-04 16:48:03','2025-01-03 16:48:03',152.62,0,0),(202,1,'95RL1T9X','2024-12-05 13:43:35','2025-01-04 13:43:35',4.38,0,0),(203,1,'PTDZM1FC','2024-12-05 13:43:35','2025-01-04 13:43:35',4.38,0,0),(204,9,'LJZE1NVA','2024-12-05 16:27:57','2025-01-04 16:27:57',628.11,0,0);
/*!40000 ALTER TABLE `detalle_inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_ventas`
--

DROP TABLE IF EXISTS `detalle_ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_ventas` (
  `id_detalle_venta` int NOT NULL AUTO_INCREMENT,
  `id_venta` int NOT NULL,
  `id_producto` int DEFAULT NULL,
  `nombre_producto` varchar(255) NOT NULL,
  `codigo_producto` varchar(100) NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `categoria_producto` varchar(100) NOT NULL,
  `devuelto` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id_detalle_venta`),
  KEY `id_venta` (`id_venta`),
  KEY `id_producto_idx` (`id_producto`),
  KEY `nombre_producto_idx` (`nombre_producto`),
  KEY `codigo_producto_idx` (`codigo_producto`),
  CONSTRAINT `codigo_producto` FOREIGN KEY (`codigo_producto`) REFERENCES `detalle_inventario` (`codigo_producto`),
  CONSTRAINT `detalle_ventas_ibfk_1` FOREIGN KEY (`id_venta`) REFERENCES `ventas` (`id_venta`),
  CONSTRAINT `id_producto` FOREIGN KEY (`id_producto`) REFERENCES `detalle_inventario` (`id_producto`),
  CONSTRAINT `nombre_producto` FOREIGN KEY (`nombre_producto`) REFERENCES `inventario` (`nombre_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_ventas`
--

LOCK TABLES `detalle_ventas` WRITE;
/*!40000 ALTER TABLE `detalle_ventas` DISABLE KEYS */;
INSERT INTO `detalle_ventas` VALUES (1,2,1,'Coca Cola','LYHK3CXB',20.00,'Bebidas',1),(2,2,1,'Coca Cola','I8STD17L',20.00,'Bebidas',0),(3,2,2,'Pepsi','PB3DEZ2R',15.50,'Bebidas',1),(4,3,1,'Coca Cola','6NR79NJX',20.00,'Bebidas',0),(5,3,2,'Pepsi','T48O7ZBC',15.50,'Bebidas',1),(6,4,2,'Pepsi','ZQ3WHRNR',15.50,'Bebidas',0),(7,5,1,'Coca Cola','FJLQMB77',20.00,'Bebidas',0),(8,6,1,'Coca Cola','65SOTCJG',20.00,'Bebidas',0),(9,7,1,'Coca Cola','I5ZJX8RL',20.00,'Bebidas',0),(10,8,2,'Pepsi','423LMQXO',15.50,'Bebidas',0),(11,9,9,'XBOX 360','K218Z43X',12000.00,'Electrónicos',0),(12,10,11,'PS4','JLC5QF7L',10000.00,'Electrónicos',0),(13,10,9,'XBOX 360','U8D3NXUH',12000.00,'Electrónicos',0),(14,11,13,'Pedigree Adulto','MGJ6DDCS',60.00,'Mascotas',1),(15,12,13,'Pedigree Adulto','ES2KFNSD',60.00,'Mascotas',1),(16,13,1,'Coca Cola','0GD1VZY0',20.00,'Bebidas',0),(17,14,1,'Coca Cola','0RTNOWEP',20.00,'Bebidas',0),(18,15,1,'Coca Cola','0RTNOWEP',20.00,'Bebidas',0),(19,16,1,'Coca Cola','0RTNOWEP',20.00,'Bebidas',0),(20,17,1,'Coca Cola','ID0E5P60',20.00,'Bebidas',0),(21,18,1,'Coca Cola','VBVTAMAA',20.00,'Bebidas',0),(22,19,2,'Pepsi','PB3DEZ2R',15.50,'Bebidas',0),(23,20,1,'Coca Cola','JNCNG6MQ',20.00,'Bebidas',0),(24,20,1,'Coca Cola','HMENK3CI',20.00,'Bebidas',0),(25,21,1,'Coca Cola','A95IFQR2',20.00,'Bebidas',0),(26,22,1,'Coca Cola','LW5VNAYE',20.00,'Bebidas',0),(27,23,1,'Coca Cola','BM3KWDW9',20.00,'Bebidas',0),(28,24,1,'Coca Cola','I5LCL2FT',20.00,'Bebidas',0),(29,25,1,'Coca Cola','RKB2PJH3',20.00,'Bebidas',0),(30,25,1,'Coca Cola','QNUDWKH2',20.00,'Bebidas',0),(31,25,1,'Coca Cola','UG8FYTWJ',20.00,'Bebidas',0),(32,25,1,'Coca Cola','S3615036',20.00,'Bebidas',1),(33,25,1,'Coca Cola','8TTTQOYJ',20.00,'Bebidas',1),(34,26,1,'Coca Cola','PJNLHFL5',20.00,'Bebidas',1),(35,27,11,'PS4','LTX3KKAR',10000.00,'Bebidas',1),(36,28,8,'Takis Fuego','S1790LJQ',16.00,'Botanas',1),(37,29,8,'Takis Fuego','S1790LJQ',16.00,'Botanas',1),(38,30,1,'Coca Cola','S3615036',20.00,'Bebidas',0),(39,31,1,'Coca Cola','LYHK3CXB',20.00,'Bebidas',0),(40,32,1,'Coca Cola','8TTTQOYJ',20.00,'Bebidas',0),(41,33,11,'PS4','LTX3KKAR',10000.00,'Electrónicos',0),(42,34,1,'Coca Cola','PJNLHFL5',20.00,'Bebidas',1),(43,35,1,'Coca Cola','PJNLHFL5',20.00,'Bebidas',0),(44,36,1,'Coca Cola','ZYFN79DF',20.00,'Bebidas',0),(45,37,1,'Coca Cola','JOLR2DGC',20.00,'Bebidas',0),(46,37,7,'Toreadas','KQTM0SEY',18.00,'Botanas',1),(47,37,8,'Takis Fuego','S1790LJQ',16.00,'Botanas',0),(48,38,1,'Coca Cola','ZNOOIYHT',22.00,'Bebidas',0),(49,39,1,'Coca Cola','JO7MPX8R',22.00,'Bebidas',0),(50,39,2,'Pepsi','T48O7ZBC',15.50,'Bebidas',0),(51,39,3,'Fanta','ZDVU0V7J',23.00,'Bebidas',0),(52,39,6,'Sabritas Xtra Flamin Hot','Y8KYPUMN',22.30,'Botanas',0),(53,39,7,'Toreadas','KQTM0SEY',18.00,'Botanas',0),(54,39,14,'Dragon Ball Sparking Zero','2TOBGXLM',1200.00,'Electrónicos',0),(55,40,1,'Coca Cola','6QVB265M',22.00,'Bebidas',0),(56,41,7,'Toreadas','CSE6MQQV',18.00,'Botanas',0),(57,41,6,'Sabritas Xtra Flamin Hot','2T0E09GM',22.30,'Botanas',0),(58,41,2,'Pepsi','8W722L9B',15.50,'Bebidas',0);
/*!40000 ALTER TABLE `detalle_ventas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventario`
--

DROP TABLE IF EXISTS `inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario` (
  `id_inventario` int NOT NULL AUTO_INCREMENT,
  `nombre_producto` varchar(256) NOT NULL,
  `imagen_producto` varchar(256) DEFAULT NULL,
  `categoria_producto` varchar(256) NOT NULL,
  `cantidad_producto` int NOT NULL,
  `descripcion_producto` text,
  `precio_unitario` decimal(10,2) NOT NULL,
  `descontinuado` tinyint NOT NULL DEFAULT '0',
  `cantidad_maxima_producto` int NOT NULL,
  PRIMARY KEY (`id_inventario`),
  UNIQUE KEY `nombre_producto_UNIQUE` (`nombre_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario`
--

LOCK TABLES `inventario` WRITE;
/*!40000 ALTER TABLE `inventario` DISABLE KEYS */;
INSERT INTO `inventario` VALUES (1,'Coca Cola','https://www.pngarts.com/files/3/Coca-Cola-PNG-Pic.png','Bebidas',23,'Coca Cola de 500 ml',22.00,0,50),(2,'Pepsi','https://www.pngarts.com/files/3/Pepsi-PNG-Transparent-Image.png','Bebidas',6,'Pepsi de 500 ml',15.50,0,10),(3,'Fanta','https://www.pngarts.com/files/17/Fanta-Free-PNG-HQ-Image.png','Bebidas',17,'Fanta de 500 ml',23.00,0,18),(4,'Squirt','https://cdn.shopify.com/s/files/1/0566/4391/1854/products/7501071120411_3ab88f04-b432-48a5-b986-e95f491eb1b4.webp?v=1672961786','Bebidas',0,'Squirt de 2.5 L',16.00,1,0),(5,'Jarrito Sabor Naranja','https://cdn.shopify.com/s/files/1/0566/4391/1854/files/7501441604114_be9adb5b-fee1-487e-9b43-8a3955106919.png?v=1683140993','Bebidas',0,'Jarrito sabor naranja de 2.5 L',17.00,1,28),(6,'Sabritas Xtra Flamin Hot','https://superlavioleta.com/cdn/shop/products/sa-sabritas-flamin-hot-42gr.png?v=1609560369','Botanas',8,'Sabritas Xtra Flamin Hot tamaño normal',22.30,0,10),(7,'Toreadas','https://www.barcel.com.mx/themes/custom/barceldos/images/files/Toreadas_Habanero.png','Botanas',23,'Toreadas Estándar',18.00,0,50),(8,'Takis Fuego','https://www.barcel.com.mx/themes/custom/barceldos/images/files/takis_fuego.png','Botanas',24,'Takis morados chidos',16.00,0,25),(9,'XBOX 360','https://wecmuseum.org/images/8/83/Xbox-360-and-kinect.png','Electrónicos',1,'XBOX 360 (2012) SIN ABRIR FULL EMPAQUETADO - INCLUYE CONTROL INALAMBRICO Y KINECT (ENVIO GRATIS)',12000.00,0,1),(11,'PS4','https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/PS4-Console-wDS4.png/640px-PS4-Console-wDS4.png','Electrónicos',1,'PS4 REACONDICIONADO',10000.00,0,1),(12,'Protector Solar Solaris','https://static.vecteezy.com/system/resources/thumbnails/025/230/146/small_2x/sunscreen-or-sunblock-cream-tube-isolated-on-transparent-background-free-png.png','Cuidado Personal',5,'Protector solar de 100 ml marca Solaris',70.00,0,100),(13,'Pedigree Adulto','https://www.pedigree.com.mx/cdn-cgi/image/format=auto,q=90/sites/g/files/fnmzdf1501/files/2022-10/7506174514471-product-image-1.png','Mascotas',8,'Pedigree Adulto',75.00,0,10),(14,'Dragon Ball Sparking Zero','https://cdn11.bigcommerce.com/s-xs1cevxe43/images/stencil/original/products/2960/14523/dragon-ball-sparking-zero-ultimate__91441.1717798062.png?c=2','Electrónicos',49,'Dragon Ball Sparking Zero Edición Deluxe',1200.00,0,50);
/*!40000 ALTER TABLE `inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ips`
--

DROP TABLE IF EXISTS `ips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ips` (
  `idip` int NOT NULL AUTO_INCREMENT,
  `ip` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idip`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ips`
--

LOCK TABLES `ips` WRITE;
/*!40000 ALTER TABLE `ips` DISABLE KEYS */;
INSERT INTO `ips` VALUES (1,'189.203.39.42');
/*!40000 ALTER TABLE `ips` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puntos`
--

DROP TABLE IF EXISTS `puntos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puntos` (
  `idclientes_puntos` int NOT NULL AUTO_INCREMENT,
  `idrango` int DEFAULT NULL,
  `total_puntos` int DEFAULT '0',
  `ultima_actualizacionPuntos` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ultima_actualizacionRangos` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `habilitado` int NOT NULL,
  PRIMARY KEY (`idclientes_puntos`),
  KEY `idrango` (`idrango`),
  CONSTRAINT `puntos_ibfk_1` FOREIGN KEY (`idrango`) REFERENCES `rangos` (`idrango`),
  CONSTRAINT `puntos_ibfk_2` FOREIGN KEY (`idclientes_puntos`) REFERENCES `clientes` (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puntos`
--

LOCK TABLES `puntos` WRITE;
/*!40000 ALTER TABLE `puntos` DISABLE KEYS */;
INSERT INTO `puntos` VALUES (1,6,55,'2024-12-05 17:55:16','2024-12-05 17:55:16',1),(2,1,0,'2024-12-05 15:35:39','2024-12-05 15:35:39',1),(3,1,0,'2024-12-05 15:35:39','2024-12-05 15:35:39',1),(4,1,0,'2024-12-05 15:35:39','2024-12-05 15:35:39',1),(5,1,0,'2024-12-05 15:35:39','2024-12-05 15:35:39',0),(6,1,0,'2024-12-05 15:35:39','2024-12-05 15:35:39',1),(7,1,0,'2024-12-05 15:35:39','2024-12-05 15:35:39',0),(8,1,0,'2024-12-05 15:35:39','2024-12-05 15:35:39',0),(9,1,0,'2024-12-05 15:35:39','2024-12-05 15:35:39',0),(10,1,0,'2024-12-05 15:35:39','2024-12-05 15:35:39',0),(19,1,0,'2024-12-05 15:35:39','2024-12-05 15:35:39',1),(20,1,1,'2024-12-06 02:29:42','2024-12-06 02:29:42',1),(21,1,0,'2024-12-05 15:39:12','2024-12-05 15:39:12',0),(22,1,482,'2024-12-05 15:53:46','2024-12-05 15:53:46',1),(23,1,43,'2024-12-06 02:36:00','2024-12-06 02:36:00',1),(24,1,3,'2024-12-07 01:24:26','2024-12-07 01:24:26',1);
/*!40000 ALTER TABLE `puntos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quejas`
--

DROP TABLE IF EXISTS `quejas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quejas` (
  `idQueja` int NOT NULL AUTO_INCREMENT,
  `id_Cliente` int DEFAULT NULL,
  `id_empleado` int DEFAULT NULL,
  `fechaHora` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `descripcion` text,
  `categoria` varchar(50) DEFAULT NULL,
  `estado` varchar(20) DEFAULT NULL,
  `prioridad` int DEFAULT NULL,
  `comentarioSeguimiento` text,
  PRIMARY KEY (`idQueja`),
  UNIQUE KEY `idQueja` (`idQueja`),
  KEY `id_Cliente` (`id_Cliente`),
  CONSTRAINT `quejas_ibfk_1` FOREIGN KEY (`id_Cliente`) REFERENCES `clientes` (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quejas`
--

LOCK TABLES `quejas` WRITE;
/*!40000 ALTER TABLE `quejas` DISABLE KEYS */;
INSERT INTO `quejas` VALUES (1,1,11,'2024-12-03 17:31:04','Mal trato de sus empleados','Servicio al cliente','Finalizada',3,'565654'),(2,2,11,'2024-12-03 17:31:04','Uno de sus refrigeradores no enfria correctamente','Instalaciones','Pendiente',2,'hdp'),(3,3,3,'2024-12-03 17:31:04','Falta de dulces en el mostrador','Productos','Finalizada',1,'Las investigaciones concluyeron que la visita se dio en horario de reabasto'),(4,4,4,'2024-12-03 17:31:04','Falta de señalizaciones de piso mojado','Otros','Finalizada',2,'Las investigaciones concluyeron que el empleado no señalo correctamente como es el protocolo'),(5,5,5,'2024-12-03 17:31:04','Pregunte por la existencia de uno de sus productos y el empleado me contesto de mala manera','Servicio al cliente','Finalizada',3,'Se realizaron las investigaciones debidas y se tomaron las acciones debidas contra el empleado implicado'),(6,6,11,'2024-12-03 17:31:04','Me cobraron productos que yo no pedi','Cobros indebidos','Finalizada',3,'Se confirmo el reingreso al cliente'),(7,1,11,'2024-12-05 01:08:13','Nomas por que si','Servicio al cliente','Activa',1,'jkhkjh'),(8,1,0,'2024-12-05 01:13:45','Nomas por que si x2','Productos','Pendiente',1,''),(9,1,0,'2024-12-05 01:20:08','Otra por que si x3','Otros','Pendiente',1,''),(10,1,0,'2024-12-05 01:21:48','otra por que si x4','Instalaciones','Pendiente',1,''),(11,1,0,'2024-12-05 04:59:19','dkalja','Instalaciones','Pendiente',1,''),(12,1,0,'2024-12-05 05:02:00','kladjlkasjda','Servicio al cliente','Pendiente',1,''),(13,1,0,'2024-12-05 05:11:34','puro alter table','Otros','Pendiente',1,''),(14,1,0,'2024-12-05 05:53:13','jsljdlksajfk','Servicio al cliente','Pendiente',1,''),(15,1,11,'2024-12-05 15:46:02','queja prueba producción','Otros','Finalizada',1,'recibida prueba producción'),(16,21,11,'2024-12-05 16:00:23','hola mi cuenta esta inactiva, ayudaaaaa','Servicio al cliente','Activa',1,'alchile que bueno'),(17,1,0,'2024-12-05 18:02:53',' no había dulces ','Productos','Pendiente',1,''),(18,23,11,'2024-12-06 02:37:21','Ninguna queja xd','Servicio al cliente','Finalizada',1,'Gracias bro. Todo un crack. Caile al R6 :)');
/*!40000 ALTER TABLE `quejas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rangos`
--

DROP TABLE IF EXISTS `rangos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rangos` (
  `idrango` int NOT NULL AUTO_INCREMENT,
  `nombre_rango` varchar(20) NOT NULL,
  `porcentaje_puntos` int NOT NULL,
  `porcentaje_devolucionPuntos` int NOT NULL,
  `num_ComprasRequisito` int NOT NULL,
  PRIMARY KEY (`idrango`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rangos`
--

LOCK TABLES `rangos` WRITE;
/*!40000 ALTER TABLE `rangos` DISABLE KEYS */;
INSERT INTO `rangos` VALUES (1,'INVITADO',5,5,0),(2,'BRONCE',10,20,5),(3,'PLATA',20,40,10),(4,'ORO',30,60,15),(5,'PLATINO',40,80,20),(6,'DIAMANTE',50,100,25);
/*!40000 ALTER TABLE `rangos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sugerencias`
--

DROP TABLE IF EXISTS `sugerencias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sugerencias` (
  `idSugerencia` int NOT NULL AUTO_INCREMENT,
  `id_Cliente` int DEFAULT NULL,
  `fechaHora` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `descripcion` text,
  `categoria` varchar(50) DEFAULT NULL,
  `estado` varchar(20) DEFAULT NULL,
  `comentarioSeguimiento` text,
  `id_empleado` int DEFAULT NULL,
  PRIMARY KEY (`idSugerencia`),
  UNIQUE KEY `idSugerencia` (`idSugerencia`),
  KEY `id_Cliente` (`id_Cliente`),
  CONSTRAINT `sugerencias_ibfk_1` FOREIGN KEY (`id_Cliente`) REFERENCES `clientes` (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sugerencias`
--

LOCK TABLES `sugerencias` WRITE;
/*!40000 ALTER TABLE `sugerencias` DISABLE KEYS */;
INSERT INTO `sugerencias` VALUES (1,1,'2024-12-03 17:51:20','Deberian de tener una forma de identificar a los empleados en capacitación para evitar inconvenientes','Servicio al cliente','Finalizada','Se tomo la sugerencia y se envio al area pertinente',1),(2,2,'2024-12-03 17:51:20','Falta más variedad de bebidas','Productos','Activa','Se esta trabajando en el tema con el area de ventas y reabastecimiento',2),(3,3,'2024-12-03 17:51:20','Deberian de capacitar a sus empleados para poder comunicarse con personas capacidades diferentes como sordo-mudos','Servicio al cliente','Activa','Se esta evaluando la posibilidad de capacitar a los empleados para este tipo de sucesos',3),(4,4,'2024-12-03 17:51:20','Falta más variedad de frituras','Productos','Activa','sadsad',11),(5,5,'2024-12-03 17:51:20','Deberian intruducir productos de limpieza en su catalogo','Productos','Activa','Se esta evaluando la solicitud con las areas encargadas',5),(6,6,'2024-12-03 17:51:20','Deberian de ampliar su estacionamiento','Instalaciones','Finalizada','Se determino que no es posible cumplir esta sugerencia',6),(8,1,'2024-12-05 05:36:08','pt','Servicio al cliente','Pendiente','',0),(9,1,'2024-12-05 15:46:18','sugerencia prueba producción','Otros','Finalizada','recibido prueba producción',11),(10,21,'2024-12-05 16:01:02','deberian de añadir mas productos, esta muy vacia su tienda XD','Productos','Finalizada','no',11),(11,1,'2024-12-05 18:03:45','deberian agregar mas dulces','Productos','Activa','se mando al area de inventario para su consideración',11),(12,23,'2024-12-06 02:37:29','Buena aplicación','Servicio al cliente','Pendiente','',0),(13,24,'2024-12-07 01:29:52','La imagen podría ser más llamativa ','Instalaciones','Pendiente','',0);
/*!40000 ALTER TABLE `sugerencias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `id_venta` int NOT NULL AUTO_INCREMENT,
  `monto_recibido` decimal(10,2) DEFAULT NULL,
  `total_venta` decimal(10,2) NOT NULL,
  `fecha_venta` datetime NOT NULL,
  `metodo_pago` varchar(50) NOT NULL,
  `id_cliente` int NOT NULL,
  `id_empleado` int DEFAULT NULL,
  PRIMARY KEY (`id_venta`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_trabajador` (`id_empleado`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`idCliente`),
  CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`id_empleado`) REFERENCES `administracion` (`id_empleado`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES (2,100.00,55.50,'2024-12-01 20:32:12','efectivo',1,7),(3,100.00,35.50,'2024-12-02 01:39:47','efectivo',1,11),(4,15.50,15.50,'2024-12-02 01:42:25','puntos',1,12),(5,20.00,20.00,'2024-12-02 01:45:01','tarjeta',1,4),(6,20.00,20.00,'2024-12-02 01:46:14','tarjeta',1,3),(7,100.00,20.00,'2024-12-02 01:48:11','efectivo',1,11),(8,1000.58,15.50,'2024-12-02 01:49:44','efectivo',5,5),(9,12000.00,12000.00,'2024-12-02 01:51:48','tarjeta',9,1),(10,30000.00,22000.00,'2024-12-02 01:59:28','efectivo',1,5),(11,100.00,60.00,'2024-12-03 12:41:33','efectivo',1,6),(12,60.00,60.00,'2024-12-03 12:43:11','puntos',1,6),(13,0.00,20.00,'2024-12-03 13:11:50','efectivo',1,1),(14,0.00,20.00,'2024-12-03 13:11:52','efectivo',1,1),(15,0.00,20.00,'2024-12-03 13:11:53','efectivo',1,1),(16,0.00,20.00,'2024-12-03 13:11:53','efectivo',1,1),(17,0.00,20.00,'2024-12-03 13:11:54','efectivo',1,1),(18,20.00,20.00,'2024-12-03 13:14:10','efectivo',1,1),(19,20.00,15.50,'2024-12-03 13:21:02','efectivo',1,6),(20,100.30,40.00,'2024-12-03 13:22:01','efectivo',1,6),(21,100.30,20.00,'2024-12-03 13:24:44','efectivo',1,5),(22,100.30,20.00,'2024-12-03 13:25:15','efectivo',1,2),(23,200.00,20.00,'2024-12-03 13:26:08','efectivo',1,7),(24,500.00,20.00,'2024-12-03 13:40:18','efectivo',1,5),(25,100.00,100.00,'2024-12-03 13:53:36','puntos',1,3),(26,20.00,20.00,'2024-12-03 13:54:02','tarjeta',1,8),(27,10000.00,10000.00,'2024-12-03 14:17:31','tarjeta',1,8),(28,50.00,16.00,'2024-12-03 17:08:54','efectivo',1,4),(29,55.00,16.00,'2024-12-03 17:10:00','efectivo',1,4),(30,20.00,20.00,'2024-12-04 01:45:09','tarjeta',1,5),(31,20.00,20.00,'2024-12-04 16:50:19','efectivo',1,5),(32,100.00,20.00,'2024-12-05 09:47:14','efectivo',22,13),(33,10000.00,10000.00,'2024-12-05 09:48:01','tarjeta',22,1),(34,20.00,20.00,'2024-12-05 09:48:35','puntos',22,4),(35,100.00,20.00,'2024-12-05 09:55:03','efectivo',21,3),(36,100.00,20.00,'2024-12-05 09:56:03','efectivo',1,6),(37,54.00,54.00,'2024-12-05 11:54:21','tarjeta',1,6),(38,22.00,22.00,'2024-12-05 20:29:42','tarjeta',20,3),(39,1300.80,1300.80,'2024-12-05 20:35:16','tarjeta',23,5),(40,22.00,22.00,'2024-12-05 20:36:00','puntos',23,6),(41,100.00,55.80,'2024-12-06 19:24:26','efectivo',24,12);
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'otzo'
--

--
-- Dumping routines for database 'otzo'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-07 20:36:54
