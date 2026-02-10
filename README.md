Configuration de  la base de données      
Pour la configuration de la base de donnée Brief_Stock_Flash , j’ai procédé comme suit: 
1- J’ai fais la modélisation de deux tables Produits et Categorie sur draw.io puis
2- J’ai ouvert Mysql Workbench 
2-1 j’ai créé ma base de donnée avec la commande sql: 
      	CREATE DATABASE Brief_Stock_Flash; 
2-2 j’ai créé mes deux tables avec les commandes 3-
CREATE TABLE Categories(
id_categorie int primary key auto_increment,
nom varchar(100) not null
);
Et
CREATE TABLE Produits(
id_produit int primary key auto_increment , 
nom varchar(100) not null, 
prix int not null, 
quantite_initiale float not null,
disponibilite bool default true ,
id_categorie int not null,
foreign key(id_categorie) references Categories(id_categorie));

3-Puis sur Visual code Studio, 
3-1 J’ai importer mysql.conector avec la commande:  3-2
import mysql.connector qui est le module qui permet à Python de communiquer avec MySQL 
3-2 J’ai créé une variable de connexion nomme maconnexion qui affecte à mysql.connector.connect(
   host="localhost",            la je lui donne le nom du serveur
   user="root",                  le nom de l’utilisateur
   password="adji",              le mot de passe
   database="Brief_Stock_Flash") le nom de la base de donnée

3-2 Puis je vérifie si la connexion est bien établie avec un print
if maconnexion.is_connected():
   print(f"Connecte avec succès à la base de donne {maconnexion.database}")


   
                                                      





 
