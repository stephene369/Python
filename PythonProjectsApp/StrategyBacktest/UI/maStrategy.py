from UI.lib import *

class maStrategy:
    def __init__(self , df:DataFrame=None ,
        r : int=0 , 
        l : int = 0,
        col:str=None) -> None:
        
        self.df = df
        self.r = r 
        self.l = l 
        self.col = col
        
    def strategy(self) :
        self.df.insert(loc=0,
            column="MA_R",
            value=self.df[self.col].rolling(self.r).mean() )
        self.df.insert(loc=1,
            column="MA_L",
            value=self.df[self.col].rolling(self.l).mean() )
        self.df = self.df.dropna()
        self.condition = [
            self.df["MA_R"]>self.df["MA_L"] ,
            self.df["MA_R"]<self.df["MA_L"]]
        
        self.choix = [1,0]
        
        self.signal_achat = []
        self.signal_vente = []
        self.condition = []
        stock = 0 # permet d'eviter d'acheter quand on pas de stock au debut
        
        self.date_1 = self.df.index[0]
        for date in self.df.index :
            if self.df["MA_R"].loc[date] > self.df["MA_L"].loc[date] :
                self.condition.append(1)
            else :
                self.condition.append(0)
            
            if( self.df["MA_R"].loc[date] > self.df["MA_L"].loc[date] ) and (self.df["MA_R"].loc[self.date_1] < self.df["MA_L"].loc[self.date_1]) and stock == 0:
                self.signal_achat.append(self.df[self.col].loc[date])
                stock = 1

            else :
                self.signal_achat.append(np.nan)

            
            if( self.df["MA_R"].loc[date] < self.df["MA_L"].loc[date] ) and (self.df["MA_R"].loc[self.date_1] > self.df["MA_L"].loc[self.date_1]) and (stock == 1):
                self.signal_vente.append(self.df[self.col].loc[date])
                stock = 0
            else :
                self.signal_vente.append(np.nan)
                
            self.date_1 = date

        self.df.insert(loc=0,column="Position",value=self.condition)
            
        self.achat_vente = []
        stock = 0
        for i in range( len(self.df) ) :
            if self.signal_achat[i] > 0 and stock != 1:
                self.achat_vente.append('acheter')
                stock = 1
                
            elif self.signal_vente[i] > 0 and stock != 0 :
                self.achat_vente.append('vendre' )
                stock=0
            else :
                self.achat_vente.append(np.nan)

        self.df.insert(loc=0,column="achat_vente",value=self.achat_vente)

        benefice = 0
        depart = 1000
        d = depart
        nombre = 0
        total = 0
        self.positive = 0 
        self.negative = 0
        self.total = 0
        
        for i in range( len( self.df ) ) :
            if self.df['achat_vente'].iloc[i] == 'acheter' :
                nombre = depart/self.df[self.col].iloc[i]
                entrer = nombre*self.df[self.col].iloc[i]
                

            elif self.df['achat_vente'].iloc[i] == 'vendre' :

                sorti = (nombre*self.df[self.col].iloc[i])
                benefice += sorti-entrer
                total += sorti
                depart = sorti
                
                if sorti>0 : self.positive+=1
                if sorti<0 : self.negative+=1
                
                
            else :
                pass
        self.total = self.positive+self.negative
        self.pourcentage_revenu = round(100*(benefice/d),3)
        return self.pourcentage_revenu 

    