import mysql.connector
maconnexion= mysql.connector.connect(
    host="localhost",
    user="root",
    password="adji",
    database="Brief_Stock_Flash"
)
if maconnexion.is_connected():
    print(f"Connecte avec succes a la base de donne {maconnexion.database}")
    print("---------------------------------------------------------------")

def menu():
    print("1-Ajouter un produit")
    print("2-Lister les produits en stock")
    print("3-Mettre a jour le stock ")
    print("4-Rechercher un produit")
    print("5-Supprimer un produit")
    print("6-Dashboard")
    print("7-Quitter")
    print("---------------------------------------------------------------")



def Ajout_Produit(nom,prix,quantite_initiale,id_categorie):
    cursor=maconnexion.cursor()
    query=""" insert into Produits(nom,prix,quantite_initiale,id_categorie) values (%s,%s,%s,%s)"""
    cursor.execute(query,(nom,prix,quantite_initiale,id_categorie))
    maconnexion.commit()
    print(f"le produit{nom} ajoute avec succes ")
    print("---------------------------------------------------------------")
    cursor.close()


def Liste_Produit():
     cursor=maconnexion.cursor()
     query=""" Select p.nom,p.prix,p.quantite_initiale,c.nom from Produits as p join Categories as c on p.id_categorie=c.id_categorie group by p.nom,p.prix,p.quantite_initiale,c.nom"""
     cursor.execute(query)
     for maligne in cursor.fetchall():
          print(maligne)
          print("---------------------------------------------------------------")
          cursor.close()

# def Mise_A_Jour_Stock(nom,quantite_initiale):
#      cursor=maconnexion.cursor()
#      update=[]    
#      if quantite_initiale:
#         update.append(f"quantite_initiale='{quantite_initiale}'")
#         if update:
#             query=f"""Update Produits set {',' .join(update)}"""
#             cursor.execute(query)
#             maconnexion.commit()
#             print(f"la quantite {nom} est mise a jour avec succes") 
#             print("---------------------------------------------------------------")
#             cursor.close()



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


def Supprime_Produit():
    nom=input(f"Quelle Produit Voulez-vous supprimer: ").strip()
    print("---------------------------------------------------------------")
    cursor=maconnexion.cursor()
    query="""Delete from Produits where nom=%s"""
    cursor.execute(query,(nom,))
    maconnexion.commit()
    print(f"Le produit {nom} est supprime avec succes")
    print("---------------------------------------------------------------")
    cursor.close()

def menu_dashboard():
    print("1-Afficher le produit le plus cher")
    print("2-Valeur totale financiere de tout le stock")
    print("3-Nombre de produits par categories")
    print("---------------------------------------------------------------")

def Produit_plus_Cher():  
     cursor=maconnexion.cursor()
     query="""Select Max(prix)as Prix_Max From Produits """
     cursor.execute(query)
     for malign in cursor.fetchall():
          print(malign)
          print("---------------------------------------------------------------")  
          cursor.close()

def Valeur_Totale_Stock():
     cursor=maconnexion.cursor()
     query="""Select sum(prix * quantite_initiale) as prixTotal from Produits """
     cursor.execute(query)
     for maligne in cursor.fetchall():
          print(maligne)
          print("---------------------------------------------------------------")
          cursor.close()

def Nombre_Produits_Par_Categories():
     cursor=maconnexion.cursor()
     query="""select  count(p.id_produit),c.nom from Categories as c 
     join Produits as p on p.id_categorie=c.id_categorie group by c.nom  """
     cursor.execute(query)
     for maligne in cursor.fetchall():
          print(maligne)
          print("---------------------------------------------------------------")
          cursor.close()

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

def main():
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
                                quantite_initiale=float(input("Quelle est la quantite restante: "))
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