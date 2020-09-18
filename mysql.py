# -*- coding: utf-8 -*-
import pymysql
import csv

#se connecter à la base de donnée
connection = pymysql.connect(user='dave', host='localhost', password='dave')
cur = connection.cursor()

#definissons une fonction pour ajouter une table à la base de donnée
def ajout():
	cur = connection.cursor()
	#cur.execute("set global local_infile = 1 ")
	#connection.commit()
	#Se connecter à la base de donnée dave
	cur.execute("use dave")
	cur.execute('drop table personne')
	#Créer une table 
	cur.execute ("create table personne (id int PRIMARY KEY, Nom VARCHAR(10),Prenom VARCHAR(15), Localite VARCHAR(15),Facture VARCHAR(10))")
	# enregistrer les valeur dans la base de de bonnées 
	connection.commit()

	#importont un fichier csv dans une table 
	#repertorier le ficher à importer dans le repertoire par défaut. trouver le répertoir à partir de cette commande show variables like 'secure_file_priv' 

	cur.execute("load data  infile '/var/lib/mysql-files/classeur2.csv' into table personne fields terminated by ';' lines terminated by '\r\n' ignore 1 lines ")
	connection.commit()
	cur.execute("select * from personne")
	rows1 = cur.fetchall()
	prinnt(rowws1)

#pour modifier la valeur de la colone d'une table 
def mmodif():
	cur.execute("udapte personne set Facture = 'AAAA' ")
	connection.commit()
	cur.execute("select * from personne")
	rows2 = cur.fetchall()
	print(rows2)

#utilison une boucle pour appler la fonction de notre choix
A = 1
B = 2
c = int(input('entrez 1 pour ajouter une table et 2 pour modifier une tabke'))

if C == A :
	ajout()
elif C == B :
    modif()
else :
	print(veuillez entrez un chiffre compris entre 1 et 2)
    pass