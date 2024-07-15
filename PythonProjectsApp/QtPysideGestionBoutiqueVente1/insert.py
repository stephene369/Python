from PySide2.QtWidgets import QLineEdit , QRadioButton , QSpinBox , QLabel
from pandas import DataFrame
from os.path import isfile
from folder import Chemin
from dateheure import dateheure
from pandas import read_csv 
from compute import dropNa , lessValue

def insert( name :QLineEdit,male: QRadioButton , 
    female : QRadioButton ,heure : QLabel , date : QLabel , users : str ) :
# affectation au variable
    nom = name.text()
    if male.isChecked()==True :
        sexe="Homme"
    elif female.isChecked()==True :
        sexe="Femme"
    else :
        sexe = " "
    df=read_csv(Chemin('datab_liste_article'))

    article=list(df['Designation']) 
    nbArticle = list(df['Nombre'])
    prixTotal=list(df['Prix Total'])
    date=date.text()
    heure = dateheure('heure')

    for i in range(len(article)) : 
        name=article[i]
        
        data={"Nom" : [nom] , "Sexe" : [sexe] , "Article" :[article[i]]
        ,"Quantite" : [nbArticle[i]] , "Prix_Total" : [prixTotal[i]] , 
        "Heure"  : [heure]  , "Date" : [date]  , "Utilisateur" : [users]}
        data=DataFrame(data)
        try : 
            df=read_csv(Chemin('datab_aritcle'))
            nbDispo=int(df[df['Designation']==name.capitalize()]['Disponible'])
            df.loc[df['Designation']==name.capitalize(),'Disponible']=(nbDispo-nbArticle[i])
            df.to_csv(Chemin('datab_aritcle'),index=False)
            
        except Exception as e : print(e.args)
        if isfile(Chemin('datab_c')) ==False :
            data.to_csv(Chemin('datab_c') , index=False)
        else :
            data.to_csv(Chemin('datab_c'),mode='a', index=False , header=False)
    
######

def insert_liste_article( articl : QLineEdit , nombre : QSpinBox , 
    prix : QSpinBox ) :
    article=articl.text() 
    nbArticle = nombre.value()
    prixTotal=prix.value()

    data={"Designation" :[article]
        ,"Nombre" : [nbArticle] , "Prix Total" : [prixTotal] }
    data=DataFrame(data)
    if isfile(Chemin('datab_liste_article')) ==False :
        data.to_csv(Chemin('datab_liste_article') , index=False)
    else :
        data.to_csv(Chemin('datab_liste_article'),mode='a', index=False , header=False)
    dropNa(Chemin('datab_liste_article'))


def atcl_insert(designationEd : QLineEdit , prixUni : QSpinBox , dispo : QSpinBox) :
    name = designationEd.text()
    name=name.capitalize()
    prix=prixUni.text()
    designationEd.setText('')
    prixUni.setValue(0)
    nbDispo=dispo.value()
    dispo.setValue(0)
    data={"Designation" : [name] , "PrixUnitaire" : [prix] ,
            "Disponible" :  [nbDispo]}
    data=DataFrame(data)
    if isfile(Chemin('datab_aritcle'))==False :
        data.to_csv(Chemin('datab_aritcle'),index=False)
        dropNa(Chemin('datab_aritcle'))
    else :
        df=read_csv(Chemin('datab_aritcle'))
        list_bool=list(df['Designation']==name)
        if sum(list_bool) > 0 :
            df=df.dropna()
            df.loc[df['Designation']==name,'PrixUnitaire']=prix
            df.loc[df['Designation']==name,'Disponible']=nbDispo
            df.to_csv(Chemin('datab_aritcle'),index=False)
        
        else :
            data.to_csv(Chemin('datab_aritcle') ,mode='a' ,index=False , header=False)
            dropNa(Chemin('datab_aritcle'))
            
####
def cancel_atcl (designationEd : QLineEdit , prixUni : QSpinBox) :
    designationEd.setText("")
    prixUni.setValue(0)
#####
def cancel(male: QRadioButton , 
            female : QRadioButton , articl : QLineEdit , nombre : QSpinBox , 
                prix : QSpinBox) :
    male.setChecked(False)
    female.setChecked(False)
    articl.setText("")
    nombre.setValue(0)
    prix.setValue(0)
    

def addOther(objet : QLineEdit , prix : QSpinBox) :
    try : 
        objet_=objet.text() ; objet.setText('')
        prix_=prix.text() ; prix.setValue(0)
        data={"Objet" : [objet_] , "Prix" : [prix_],
            "Date" : dateheure(x='date') ,"Heure" : dateheure(x="heure")}
        data=DataFrame(data)
        if not isfile(Chemin('datab_other')) :
            data.to_csv(Chemin('datab_other'),index=False)
        else :
            data.to_csv(Chemin('datab_other'),index=False,mode='a',header=False)        
        dropNa(Chemin('datab_other'))
    except Exception as e : print(e)


