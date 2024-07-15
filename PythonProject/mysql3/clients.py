import sqlite3
from datetime import datetime
import pandas as pd
import os

# connexion
connexion=sqlite3.connect("client.db")

# curseur
curseur=connexion.cursor()

# creating data base
curseur.execute('''CREATE TABLE IF NOT EXISTS clients(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,nom VARCHAR,nbproduits INTEGER,date VARCHAR , heure VARCHAR )''') 
# curseur.execute('''CREATE TABLE IF NOT EXISTS clients(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,nom VARCHAR,nbproduits INTEGER,date VARCHAR , heure VARCHAR )''')

df=pd.read_sql_query("SELECT * FROM clients " , connexion)

# get date and time
heuredate=datetime.now()
date=heuredate.strftime('%d/%m/%Y') ; date
heure=heuredate.strftime('%H:%M') ; heure


table=[('amos',12 , heure , date )]

nom='nom'

for tabl in table :
    curseur.execute(f'INSERT INTO clients( {nom} ,nbproduits,heure,date) VALUES(?,?,?,?) ',tabl)

curseur.execute('SELECT id,nom,nbproduits,heure,date FROM clients')
for resultats in curseur:
    print(resultats)


# export in csv
curseur.execute('SELECT nom,nbproduits,heure,date FROM clients')
df=pd.DataFrame(curseur.fetchall(),columns=['nom','nbProduits','heure','date'])



#creating file or add row
if os.path.exists('clients_db.csv') == False :
    df.to_csv('clients_db.csv',index=False)
else :
    df.to_csv('clients_db.csv',mode='a',index=False,header=False)
    

df.to_csv('clients_db.csv',mode='a',index=False,header=False)


connexion.commit()


curseur.execute('DROP TABLE IF EXISTS clients')
