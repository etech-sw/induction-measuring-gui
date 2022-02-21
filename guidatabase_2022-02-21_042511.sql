/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/ guidatabase /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE guidatabase;

DROP TABLE IF EXISTS customers;
CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` int DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `street` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `postal_code` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS devices;
CREATE TABLE `devices` (
  `id` int NOT NULL AUTO_INCREMENT,
  `device_manufacturer` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `inductance` int NOT NULL,
  `dimensions` varchar(255) NOT NULL,
  `name_customer` varchar(255) NOT NULL,
  `surname_customer` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO customers(id,name,surname,email,phone,company,street,location,postal_code) VALUES(1,'MAKOLLE','Edmond Ghislain','edghimakoll@gmail.com',691678378,NULL,NULL,NULL,NULL),(2,'GUIFFOU','Joel',NULL,NULL,'ETECH',NULL,'Yaounde',NULL),(3,'MFOSSA','Abdel Aziz','abdelmfossa@gmail.com',NULL,'CUTI',NULL,'Yaounde',NULL),(4,'AGUEGUIA','Raoul',NULL,NULL,'ETECH',NULL,NULL,NULL),(5,'PEMHA','Luque',NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO devices(id,device_manufacturer,type,inductance,dimensions,name_customer,surname_customer) VALUES(1,'Spule 1','Spule',80,'100x100','PEMHA','Luque'),(2,'Spule 2','Spule',81,'100x50','GUIFFOU','Joel'),(3,'Spule 10','Spule',90,'150x200','MAKOLLE','Edmond Ghislain'),(4,'Spule 7','Device',100,'250x250','AGUEGUIA','Raoul'),(5,'Spule 8','Spule',60,'400x200','MFOSSA','Abdel ');