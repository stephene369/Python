import pandas as pd
import numpy as np
import print_color
from tqdm import tqdm
q=1
NAME =['BRVM-Agriculture','BRVM-Public-Services']
for name in NAME :
    print(name+'\n\n\n')
    boab = pd.read_csv(f"../data/{name}.csv",index_col="Date")
    boab = boab.iloc[-730:]

    print(boab.head(3))
    df = pd.DataFrame()
    rapideList = []
    lenteList = []
    signalList = []
    benef = []
    transaction = [[],[]]
    iditify = []
    id_ = 0
    niv = []
    val = []
    pourcentage_benefice=0

    resutlat = { "Negative": [] , "Positive" : [], "Null" : []}
    for rapide_ in tqdm(range(10,26)) :
        for lente_ in tqdm(range(20,41) ):
            if (lente_)>=(rapide_+10) :
                for signal in range(8,11):
                    for niveau in range(12,15) : 
                        for v in range(3) :
                            q = v
                            boab = pd.read_csv(f"../data/{name}.csv",index_col="Date")
                            boab = boab.iloc[-365*2:-365]
                            id_+=1
                            iditify.append(id_)
                            niv.append(niveau)
                            rapideList.append(rapide_)
                            lenteList.append(lente_)
                            signalList.append(signal)
                            val.append(q)
                            
                            positif = 0
                            negatif = 0
                            prix_bas = boab['Low'].rolling(niveau).min()
                            prix_eleve = boab['High'].rolling(niveau).max()
                            cloture = boab["Close"]

                            boab["%k"] = ((cloture - prix_bas) / (prix_eleve - prix_bas)) * 100
                            boab["%d"] = boab['%k'].rolling(3).mean()

                            #determination de l'indicateur moyenne mobile convergence divergence
                            ema_rapide = cloture.ewm(span = rapide_ , adjust = False).mean()
                            ema_lente = cloture.ewm(span = lente_, adjust = False).mean()
                            # MACD
                            macd = pd.DataFrame(ema_rapide - ema_lente).rename(columns = {'Close':'MACD'})

                            # SIGNALE
                            ema_macd = macd.ewm(span=signal,adjust=False).mean()
                            signale = pd.DataFrame(ema_macd.rename(columns={"MACD":"Signale"}))

                            # HISTOGRAMME
                            histogramme = pd.DataFrame(macd['MACD']-signale['Signale']).rename(columns = {0:"hist"})


                            boab = boab.assign(MACD= macd)
                            boab = boab.assign(Signale= signale)
                            boab = boab.assign(Histogramme=histogramme)

                            # strategie de trading
                            cloture = boab['Close']
                            macd = boab['MACD']
                            signale_macd = boab['Signale']
                            k = boab['%k']
                            d = boab['%d']
                            stock = 0 

                            prix_achat = []
                            prix_vente = []
                            stoc_macd_signal = []
                            position = []

                            signal_achat = []
                            signal_vente = []
                            achat_et_vente = []

                            for i in range(len(cloture)) :

                                if k.iloc[i]<30 and d.iloc[i]<30 and macd.iloc[i]<-q and signale_macd.iloc[i]<-q :
                                    signal_achat.append(cloture.iloc[i])
                                    signal_vente.append(np.nan)
                                    
                                    if stock != 1 and cloture.iloc[i]>0 :
                                        achat_et_vente.append("acheter")
                                        prix_achat.append( cloture.iloc[i] )
                                        prix_vente.append( np.nan )
                                        stock = 1
                                        stoc_macd_signal.append(0)
                                        position.append(1)

                                    else :
                                        achat_et_vente.append(np.nan)
                                        prix_achat.append(np.nan)
                                        prix_vente.append(np.nan)
                                        stoc_macd_signal.append(0)
                                        position.append(1)

                                elif k.iloc[i]>70 and d.iloc[i]>70 and macd.iloc[i]>q and signale_macd.iloc[i]>q :
                                    signal_vente.append(cloture.iloc[i])
                                    signal_achat.append(np.nan)

                                    if stock != -1 and stock != 0 :
                                        achat_et_vente.append("vendre")
                                        prix_vente.append( cloture.iloc[i] )
                                        prix_achat.append( np.nan )
                                        stock = -1
                                        stoc_macd_signal.append(stock)
                                        position.append(0)
                                    
                                    else :
                                        achat_et_vente.append(np.nan)
                                        prix_achat.append(np.nan)
                                        prix_vente.append(np.nan)
                                        stoc_macd_signal.append(0)
                                        position.append(0)
                                
                                else :
                                    achat_et_vente.append(np.nan)
                                    signal_achat.append(np.nan)
                                    signal_vente.append(np.nan)

                                    prix_achat.append( np.nan )
                                    prix_vente.append( np.nan )
                                    stoc_macd_signal.append(0)
                                    
                                    if stock == 0 :
                                        position.append(0)
                                    
                                    else :
                                        position.append(position[i-1])

                            boab = boab.assign(achat_vente =achat_et_vente)


                            benefice_total = 0
                            depart = 1000
                            d=depart
                            nombre = 0
                            total = 0

                            for i in range( len( boab ) ) :
                                if boab['achat_vente'].iloc[i] == 'acheter' :

                                    nombre = depart/boab['Close'].iloc[i]
                                    entrer = nombre*boab['Close'].iloc[i]
                                    
                                elif boab['achat_vente'].iloc[i] == 'vendre' :
                                    sorti = (nombre*boab['Close'].iloc[i])
                                    benefice_total += sorti-entrer
                                    depart = sorti
                                    if (sorti-entrer) <= 0 : negatif+=1
                                    else : positif +=1
                            
                            
                            pourcentage_benefice = round(100*(benefice_total/d),3)
                            benef.append(pourcentage_benefice)
                            transaction[0].append(positif)
                            transaction[1].append(negatif)

                            
                """ if pourcentage_benefice > 0.0:
                    print(rapide_,end="    ")
                    print_color.print(f" {pourcentage_benefice}  id = {id_}" , color = 'green')
                    
                                #print_color.print(f"{ope}: {r}-{l}-{s}-{low}-{hight} ",
                                        #tag_color='red',color='white',end="\n ")"""
    df["rapide"] = rapideList
    df["Lente"] = lenteList
    df["signale"] = signalList
    df["valid"] = val
    df["benefice"] = benef
    df["positive"] = transaction[0]
    df["negative"] = transaction[1]
    df['niveau'] = niv
    df["id"] = iditify
    df.to_csv(f"../test/MACD_{name}_train.csv")
    for var in [df,rapideList , lenteList , signalList, transaction , benef , iditify,niv] : del(var)
    


