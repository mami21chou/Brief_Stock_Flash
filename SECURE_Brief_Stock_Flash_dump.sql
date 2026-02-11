-- MySQL dump 10.13  Distrib 8.0.44, for Linux (x86_64)
--
-- Host: localhost    Database: SECURE_Brief_Stock_Flash
-- ------------------------------------------------------
-- Server version	8.0.44-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Categories`
--

DROP TABLE IF EXISTS `Categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Categories` (
  `id_categorie` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  PRIMARY KEY (`id_categorie`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Categories`
--

LOCK TABLES `Categories` WRITE;
/*!40000 ALTER TABLE `Categories` DISABLE KEYS */;
INSERT INTO `Categories` VALUES (1,'Fruit'),(2,'Legume'),(3,'Boisson'),(4,'Pate'),(5,'Fruit'),(6,'Legume'),(7,'Boisson'),(8,'Pate');
/*!40000 ALTER TABLE `Categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Produits`
--

DROP TABLE IF EXISTS `Produits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Produits` (
  `id_produit` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `prix` int NOT NULL,
  `quantite_initiale` float NOT NULL,
  `disponibilite` tinyint(1) DEFAULT '1',
  `id_categorie` int NOT NULL,
  PRIMARY KEY (`id_produit`),
  KEY `id_categorie` (`id_categorie`),
  CONSTRAINT `Produits_ibfk_1` FOREIGN KEY (`id_categorie`) REFERENCES `Categories` (`id_categorie`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Produits`
--

LOCK TABLES `Produits` WRITE;
/*!40000 ALTER TABLE `Produits` DISABLE KEYS */;
INSERT INTO `Produits` VALUES (1,'banane',100,23,1,1),(2,'kiwi',350,12,1,1),(3,'choux',200,23,1,2),(4,'navet',200,20,1,2);
/*!40000 ALTER TABLE `Produits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Utilisateurs`
--

DROP TABLE IF EXISTS `Utilisateurs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Utilisateurs` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `adresse` varchar(100) NOT NULL,
  `telephone` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) DEFAULT 'user',
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `telephone` (`telephone`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `password` (`password`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Utilisateurs`
--

LOCK TABLES `Utilisateurs` WRITE;
/*!40000 ALTER TABLE `Utilisateurs` DISABLE KEYS */;
INSERT INTO `Utilisateurs` VALUES (1,'Sambe','Adji','Diourbel','776543233','adji@gmail.com','1234','user'),(2,'Sow','Aissata','Pikine','773213233','sow@gmail.com','1111','admin'),(3,'Lom','Adji','Keur Massar','783343233','lom@gmail.com','3333','user'),(4,'Gueye','Binetou','Guediawaye','775433545','binetou@gmail.com','5555','user'),(5,'Badiane','Bineta','Dakar','776587575','bb@gmail.com','7777','user'),(6,'Samb','Fassa','Bargny','787646543','samb@gmail.com','$2b$14$6l/rVSQFTqdHzCpMQ91y/e7p35Yr7mkOMnAC1e87djxFlwkaNWWja','user'),(7,'Diallo','Aliou','Rufisque','778655555','diallo@gmail.com','$2b$14$IdYoatYYBVjJ5PQu.DMMDOPBrgAN9kc5ABfn16LOukEGtoVcS2Gb6','user'),(8,'Talla','Cheikh','Dakar','777777777','talla@gmail.com','$2b$14$CjzmQrN/UgQLV2W5/xs9KuY.1vHThb2VEH0syjYU/QHBgeYBhfi3K','user'),(9,'Ali','Moussa','Thiaroye','771111112','ali@gmail.com','$2b$14$Tol7l2fTlD9e1nAGUzDhkOZ7ukMJHSgi9R4XgfGIn3Wu132wlv5gq','user'),(10,'Fall','Rokiyatou','Mariste','776565655','fall@gmail.com','$2b$14$m3ZIDFIdsoQ2suqh6pFZo.MDTtf0i0DMWlFl6CGQkUMs.kO/94/pe','user'),(14,'Fall','Assane','Rufisque','789000000','assane@gmail.com','$2b$14$DCNbeQhq3.9c/uhkfH8Ca.n/pCCZ2mF1XhnAXBGTgprc1X1jVgDKG','user'),(15,'Wade','Adji','Bargny','709877678','wade@gmail.com','$2b$14$eSt0COYSZMQbc9pEreWQ1O2iiYF3WRj8N1hV8ks7N2TAb0Bk1F.LW','user');
/*!40000 ALTER TABLE `Utilisateurs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-11 21:53:06
