# ========================================================================================================================
import mysql.connector
import bcrypt

maconnexion= mysql.connector.connect(
    host="localhost",
    user="root",
    password="adji",
    database="SECURE_Brief_Stock_Flash"
)
if maconnexion.is_connected():
    print(f"Connecte avec succes a la base de donne {maconnexion.database}")
    print("---------------------------------------------------------------")

#==========================================================================================================================


def Inscription():
    
    nom = input ("Donnez votre nom: ")
    prenom= input("Donnez votre prenom: ")
    adresse = input("Donnez votre adresse: ")
    telephone = input("Donnez votre numero: ")
    email = input("Donnez votre email: ")
    password= input("Donnez votre mot de passe: ").encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
    if bcrypt.checkpw(password, hashed):
        print("Felicitations Vous etes bien inscrit")
        cursor=maconnexion.cursor()
        query="""Insert into Utilisateurs(nom,prenom,adresse,telephone,email,password) values (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,(nom,prenom,adresse,telephone,email,hashed))
        maconnexion.commit()    
        connect()
    else:
        print("Inscription Refusee")
           
    

def connect():
  
  while True:
        print("Veuillez vous authentifier")
        email = input("Email : ")
        password = input("Mot de passe : ").encode()
   
        cursor=maconnexion.cursor()
        query="""Select u.nom, u.prenom, u.email,u.password from Utilisateurs as u 
        where email=%s """
        cursor.execute(query,(email,))
        ma = cursor.fetchone()
        if ma is None:
            print("Email incorrect")
            print("---------------------------------------------------------------")
        else:
            nom,prenom,email,hashed=ma


            if bcrypt.checkpw(password, hashed.encode() ):
                print(f"Connexion Reussie, Bienvenue {nom} {prenom}")
                print("---------------------------------------------------------------")
                break
            else:
                print("Mot de passe incorrect")
                print("---------------------------------------------------------------")

        cursor.close()


def Interface_user():
     while True:
        print("Bonjour, Bienvenue Veuillez vous connecter ou vous inscrire")
        print("---------------------------------------------------------------")
        print("1-Pour se connecter") 
        print("2-Pour s'inscrire ") 
        choix=input("Donnez votre choix") 
        if choix=="1":
           connect()
           break
        if choix=="2":
            Inscription()
            
            break
        
        else:
             print("Choix inconnue")
        


def menu():
    print("1-Ajouter un produit")
    print("2-Lister les produits en stock")
    print("3-Mettre a jour le stock ")
    print("4-Rechercher un produit")
    print("5-Supprimer un produit")
    print("6-Dashboard")
    print("7-Quitter")
    print("---------------------------------------------------------------")

#==========================================================================================================================


def Ajout_Produit(nom,prix,quantite_initiale,id_categorie):

    cursor=maconnexion.cursor()

    query=""" insert into Produits(nom,prix,quantite_initiale,id_categorie) values (%s,%s,%s,%s)"""

    cursor.execute(query,(nom,prix,quantite_initiale,id_categorie))

    maconnexion.commit()

    print(f"le produit {nom} ajoute avec succes ")
    print("---------------------------------------------------------------")
    cursor.close()

#==========================================================================================================================


def Liste_Produit():
     cursor=maconnexion.cursor()

     query=""" Select p.nom,p.prix,p.quantite_initiale,c.nom from Produits as p join Categories as c on 
     p.id_categorie=c.id_categorie group by p.nom,p.prix,p.quantite_initiale,c.nom"""

     cursor.execute(query)

     for maligne in cursor.fetchall():
          print(maligne)
          print("---------------------------------------------------------------")
          cursor.close()

#==========================================================================================================================


def Mise_A_Jour_Stock(nom, quantite_initiale):
    cursor = maconnexion.cursor()

    # Vérifier si le produit existe
    cursor.execute(
        "SELECT * FROM Produits WHERE nom = %s",
        (nom,)
    )
    produit = cursor.fetchone()

    if produit is None:
        print("------------------------------------")
        print(f"Le produit '{nom}' n'existe pas.")
        print("------------------------------------")
        cursor.close()
        return

    # Mise à jour si le produit existe
    cursor.execute(
        "UPDATE Produits SET quantite_initiale = %s WHERE nom = %s",
        (quantite_initiale, nom)
    )

    maconnexion.commit()
    print("------------------------------------")
    print(f"La quantité du produit '{nom}' a été mise à jour avec succès")
    print("------------------------------------")

    cursor.close()

#==========================================================================================================================


def Recherche_Produit():
     nom=input(f"Quelle produit voulez-vous rechercher:").strip()
     print("---------------------------------------------------------------")

     cursor=maconnexion.cursor()

     query="""Select * from Produits where nom= %s"""

     cursor.execute(query,(nom,))

     resultat= cursor.fetchall()

     if not resultat :
          print(f"Le produit{nom} n'est pas enregestre dans les produits")
          print("---------------------------------------------------------------")

     else:     
        for maligne in resultat:
            print(maligne)
            print("---------------------------------------------------------------")
            cursor.close()

#==========================================================================================================================


def Supprime_Produit():
    while True:
        nom=input(f"Quelle Produit Voulez-vous supprimer: ").strip()
        print("---------------------------------------------------------------")

        cursor=maconnexion.cursor()

        requete="""Select * from Produits where nom=%s"""

        cursor.execute(requete,(nom,))

        mavariable=cursor.fetchall()
        
        if not mavariable  :
            print("le produit n'existe pas")
            print("-------------------------------------------------------------------")
            break

        else:     
            query="""Delete from Produits where nom=%s"""

            cursor.execute(query,(nom,))

            maconnexion.commit()

            print(f"Le produit {nom} est supprime avec succes")
            print("---------------------------------------------------------------")

            cursor.close()
            break

#==========================================================================================================================

def menu_dashboard():
    print("1-Afficher le produit le plus cher")
    print("2-Valeur totale financiere de tout le stock")
    print("3-Nombre de produits par categories")
    print("---------------------------------------------------------------")

#==========================================================================================================================


def Produit_plus_Cher():
     nom=0
     cursor=maconnexion.cursor()

     query="""Select nom,Max(prix)as Prix_Max From Produits where nom = %s """

     cursor.execute(query,(nom,))

     maligne = cursor.fetchone()
     nom=maligne[1]
     print(maligne)
     print("---------------------------------------------------------------")  
     cursor.close()          

#==========================================================================================================================


def Valeur_Totale_Stock():
     
     cursor=maconnexion.cursor()

     query="""Select sum(prix * quantite_initiale) as prixTotal from Produits """

     cursor.execute(query)

     for maligne in cursor.fetchall():
          
          print(maligne)
          print("---------------------------------------------------------------")
          cursor.close()

#==========================================================================================================================

def Nombre_Produits_Par_Categories():
     
     cursor=maconnexion.cursor()

     query="""select  count(p.id_produit),c.nom from Categories as c 
     join Produits as p on p.id_categorie=c.id_categorie group by c.nom  """

     cursor.execute(query)

     for maligne in cursor.fetchall():
          
          print(maligne)
          print("---------------------------------------------------------------")
          cursor.close()

#==========================================================================================================================


def dashboard():
     
     menu_dashboard()

     print("---------------------------------------------------------------")
     choixdashboard=(input("Donnez votre choix: ")).strip()

     if choixdashboard=="1":
          print("---------------------------------------------------------------")  
          print("Le produit le plus cher est :")
          Produit_plus_Cher( )
          print("---------------------------------------------------------------")

     elif choixdashboard=="2":
          print("---------------------------------------------------------------") 
          print(f"La valeur totale financiere de tout le stock est :") 
          Valeur_Totale_Stock() 
          print("---------------------------------------------------------------")  

     elif choixdashboard=="3":       
          print("---------------------------------------------------------------") 
          print("Le Nombre de produits par categories est :")
          Nombre_Produits_Par_Categories()
          print("---------------------------------------------------------------")

     else:
          print("choix inconnu retour au menu")
          print("---------------------------------------------------------------")


#==========================================================================================================================







def main():
        Interface_user()
        
        

        while True:
             try:
    
                menu()
                choixmenu=int(input("Donnez votre choix: "))
                if choixmenu==1:
                    
                    nom=input("Quel est le nom du produit: ").strip()
                    while True:
                        
                            if nom.isdigit():
                                print("---------------------------------------------------------------")
                                print("Le nom du produit ne doit pas etre un chiffre")
                                print("---------------------------------------------------------------")
                                break
                            else: 
                                prix= int(input("Quel est le prix unitaire en Franc CFA: "))
                                quantite_initiale=float(input("La quantite stockee"))
                                id_categorie= int(input("Quelle est sa categorie: "))
                                Ajout_Produit(nom,prix,quantite_initiale,id_categorie)
                                break           
                                        

                    
                elif choixmenu==2:    
                    print("Voici la liste des Produits")
                    Liste_Produit()

                                
                elif choixmenu==3:
                    Liste_Produit()
                    nom=input(f"Quelle est le nom du produit a mettre a jour: ").strip()
                    while True:
                            if nom.isdigit():
                                print("---------------------------------------------------------------")
                                print("Le nom du produit ne doit pas etre un chiffre")
                                print("---------------------------------------------------------------")
                                break
                            else: 
                                quantite_initiale=float(input("Quelle est la quantite : "))
                                Mise_A_Jour_Stock(nom,quantite_initiale)
                                break


                       
                elif choixmenu==4:
                    Recherche_Produit()


                elif choixmenu==5:
                    Supprime_Produit()  


                elif choixmenu==6:
                     dashboard()


                elif choixmenu==7:
                     print("Au revoir")
                     print("Fin du programme")
                     print("---------------------------------------------------------------") 
                     break   
                else:
                     print("Veillez choisir entre 1  et 6 pour continuer ou 7 pour quitter")   
                     print("---------------------------------------------------------------")  
             except ValueError as e:
                  print(f"Erreur {e} Donnez une bonne valeur")   
                  print("---------------------------------------------------------------")
             
main()            
maconnexion.close()