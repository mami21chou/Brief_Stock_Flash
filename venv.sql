
CREATE DATABASE SECURE_Brief_Stock_Flash;
use SECURE_Brief_Stock_Flash;

CREATE TABLE Categories(
id_categorie int primary key auto_increment,
nom varchar(100) not null
);

insert into Categories(nom) values
("Fruit"),
("Legume"),
("Boisson"),
("Pate");
select * from Categories;

CREATE TABLE Produits(
id_produit int primary key auto_increment , 
nom varchar(100) not null, 
prix int not null, 
quantite_initiale float not null,
disponibilite bool default true ,
id_categorie int not null,
foreign key(id_categorie) references Categories(id_categorie));

select * from Produits;

select p.nom, count(p.id_produit),c.nom from Produits as p 
join Categories as c on p.id_categorie=c.id_categorie group by p.nom,c.nom ;

select p.nom, sum(c.id_categorie),c.nom from Produits as p 
     join Categories as c on p.id_categorie=c.id_categorie group by p.nom,c.nom ;
     
select  count(p.id_produit),c.nom from Categories as c 
     join Produits as p on p.id_categorie=c.id_categorie group by c.nom ;    
     
     
     
CREATE TABLE Utilisateurs(
id_user int primary key auto_increment,
nom varchar(100) not null,
prenom varchar(100) not null,
adresse varchar(100) not null,
telephone varchar(100) not null unique,
email varchar(100) not null unique,
password varchar(100) not null unique,
type varchar(100) default "user");  

insert into Utilisateurs(nom,prenom,adresse,telephone,email,password,type)values
('Sambe','Adji','Diourbel','776543233','adji@gmail.com','1234','user'),
('Sow','Aissata','Pikine','773213233','sow@gmail.com','1111', 'admin'),
('Lom','Adji','Keur Massar','783343233','lom@gmail.com','3333','user');

select * from Utilisateurs;

select * from Utilisateurs where type='admin';
