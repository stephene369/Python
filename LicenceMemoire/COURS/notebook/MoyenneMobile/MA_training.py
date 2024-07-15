import pandas as pd
import numpy as np
import pandas as pd
import print_color
import json
from tqdm import tqdm

# creation de de colonne de moyenne mobile
#NAME = ['BRVM-Public-Services']
NAME = ['BRVM-Agriculture','BRVM-Public-Services']

for name in NAME :

    BRVM = pd.read_csv(f"../data/{name}.csv",index_col="Date")
    resultat = {"Null" : [] ,"Negative":[] , "Positive":[]}
    
    df = pd.DataFrame()
    rapide = []
    lente = []
    benef = []
    id_ = []
    i =0
    
    transaction = [[],[]]
    print(BRVM.head())

    for r in tqdm(range(20,61) ):
        for l in tqdm(range(30,101)) :
            transaction_positive = 0
            transaction_negative = 0

            i+=1
            rapide.append(r)
            lente.append(l)
            id_.append(i)
            boab = BRVM[["Close"]].iloc[-365*3:-365*2]

            
            boab.insert (loc=1,column="MA10",value=boab["Close"].rolling(r).mean() ) #10
            # moyenne mobile lente / long terme
            boab.insert (loc=1,column="MA50",value=boab["Close"].rolling(l).mean() ) #10

            boab = boab.dropna() ;

            # creation de la liste position
            condition = [boab["MA10"]>boab["MA50"] , boab["MA10"]<boab["MA50"]]
            # creation d'une liste choix de deux element
            choix = [1,0]
            # # # #
            boab['P'] = np.select(condition, choix)

            condition = []
            signal_achat = []
            signal_vente = []
            date_1 = boab.index[0]
            stock = 0 # permet d'eviter d'acheter quand on pas de stock au debut

            for date in boab.index :
                if boab["MA10"].loc[date] > boab["MA50"].loc[date] :
                    condition.append(1)
                else :
                    condition.append(0)
                
                if( boab["MA10"].loc[date] > boab["MA50"].loc[date] ) and (boab["MA10"].loc[date_1] < boab["MA50"].loc[date_1]) and stock == 0:
                    signal_achat.append(boab["Close"].loc[date])
                    stock = 1

                else :
                    signal_achat.append(np.nan)

                
                if( boab["MA10"].loc[date] < boab["MA50"].loc[date] ) and (boab["MA10"].loc[date_1] > boab["MA50"].loc[date_1]) and (stock == 1):
                    signal_vente.append(boab["Close"].loc[date])
                    stock = 0
                else :
                    signal_vente.append(np.nan)
                    
                date_1 = date

            boab["Position"] = condition
                    
            #for i in range(len(boab)-1 , 0 , -1 ) :
            #    if signal_achat[i] > 0 :
            #        signal_achat[i] = np.nan
            #        break
                    

            achat_vente = []
            stock = 0
            for i in range( len(boab) ) :
                if signal_achat[i] > 0 and stock != 1:
                    achat_vente.append('acheter')
                    stock = 1
                    
                elif signal_vente[i] > 0 and stock != 0 :
                    achat_vente.append('vendre' )
                    stock=0
                else :
                    achat_vente.append(np.nan)

            boab['achat_vente'] = achat_vente


            benefice = 0
            depart = 1000
            d = depart
            nombre = 0
            total = 0

            for i in range( len( boab ) ) :
                if boab['achat_vente'].iloc[i] == 'acheter' :
                    nombre = depart/boab['Close'].iloc[i]
                    entrer = nombre*boab['Close'].iloc[i]
                    

                elif boab['achat_vente'].iloc[i] == 'vendre' :

                    sorti = (nombre*boab['Close'].iloc[i])
                    benefice += sorti-entrer
                    if sorti-entrer <= 0 : transaction_negative+=1
                    else : transaction_positive+=1
                    
                    total += sorti
                    depart = sorti
                else :
                    
                    pass

            pourcentage_revenu = round(100*(benefice/d),3)
            benef.append(pourcentage_revenu)
            if pourcentage_revenu > 0.0:
                resultat["Positive"].append(
                        { 
                            "Periode Rapide" : r ,
                                "Periode Lente" : l ,
                                "Pourcentage " :f"{pourcentage_revenu} %"} 
                )

            elif pourcentage_revenu < 0.0:
                resultat["Negative"].append(
                        { 
                            "Periode Rapide" : r ,
                                "Periode Lente" : l ,
                                "Pourcentage " :f"{pourcentage_revenu} %" } )
            else :
                resultat["Null"].append(
                        { 
                                "Periode Rapide" : r ,
                                "Periode Lente" : l ,
                                "Pourcentage " :f"{pourcentage_revenu} %" } )
            transaction[0].append(transaction_positive)
            transaction[1].append(transaction_negative)

    df["lente"] = lente
    df["rapide"] = rapide
    df['benef'] = benef
    df["id"] = id_
    df["positive"] = transaction[0]
    df["negative"] = transaction[1]

    df.to_csv(f"../test/MA_{name}_train.csv")
    with open(f"../test/MA_{name}_train.json","w") as j :
        liste = json.dumps(resultat,indent=4)
        j.write(liste)
        j.close()
                
            
