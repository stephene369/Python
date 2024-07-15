import pandas as pd
import numpy as np
import print_color
from tqdm import tqdm


class OS_MACD :
    def __init__(self,df, rapide,lente,niveau,
            signal,close,low,hight):
        q=0
        self.df = df

        positif = 0
        negatif = 0
        prix_bas = self.df[low].rolling(niveau).min()
        prix_eleve = self.df[hight].rolling(niveau).max()
        cloture = self.df[close]

        self.df["%k"] = ((cloture - prix_bas) / (prix_eleve - prix_bas)) * 100
        self.df["%d"] = self.df['%k'].rolling(3).mean()

        #determination de l'indicateur moyenne mobile convergence divergence
        ema_rapide = cloture.ewm(span = rapide , adjust = False).mean()
        ema_lente = cloture.ewm(span = lente, adjust = False).mean()
        # MACD
        macd = pd.DataFrame(ema_rapide - ema_lente).rename(columns = {close:'MACD'})

        # SIGNALE
        ema_macd = macd.ewm(span=signal,adjust=False).mean()
        signale = pd.DataFrame(ema_macd.rename(columns={"MACD":"Signale"}))

        # HISTOGRAMME
        histogramme = pd.DataFrame(macd['MACD']-signale['Signale']).rename(columns = {0:"hist"})


        self.df = self.df.assign(MACD= macd)
        self.df = self.df.assign(Signale= signale)
        self.df = self.df.assign(Histogramme=histogramme)

        # strategie de trading
        cloture = self.df[close]
        macd = self.df['MACD']
        signale_macd = self.df['Signale']
        k = self.df['%k']
        d = self.df['%d']
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

        self.df = self.df.assign(achat_vente =achat_et_vente)


        benefice_total = 0
        depart = 1000
        d=depart
        nombre = 0
        total = 0

        for i in range( len( self.df ) ) :
            if self.df['achat_vente'].iloc[i] == 'acheter' :

                nombre = depart/self.df[close].iloc[i]
                entrer = nombre*self.df[close].iloc[i]
                
            elif self.df['achat_vente'].iloc[i] == 'vendre' :
                sorti = (nombre*self.df[close].iloc[i])
                benefice_total += sorti-entrer
                depart = sorti
                if (sorti-entrer) <= 0 : negatif+=1
                else : positif +=1
        
        self.positive  = positif
        self.negative = negatif
        self.pourcentage_benefice = round(100*(benefice_total/d),3)

