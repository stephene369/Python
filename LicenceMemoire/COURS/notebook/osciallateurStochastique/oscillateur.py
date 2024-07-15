# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import floor
import yfinance as yf
import pandas as pd
import seaborn as snb

# %%
amzn = yf.download("AMZN","2010-11-24","2023-05-10")
#amzn.to_csv("AMAZON_2021-11-24_2023-05-10.csv")
#print(len(amzn))
#amzn = pd.read_csv("AMAZON_2021-11-24_2023-05-10.csv")
#amzn = amzn.set_index(amzn["Date"]).drop("Date",axis=1)


# %% [markdown]
# # Oscillateur Stochastique

# %%
#Determinons si le marche est un surachat ou en survente 
prix_bas = amzn['Low'].rolling(14).min()
prix_eleve = amzn['High'].rolling(14).max()
cloture = amzn["Close"]

amzn["%k"] = ((cloture - prix_bas) / (prix_eleve - prix_bas)) * 100
amzn["%d"] = amzn['%k'].rolling(3).mean()

# %% [markdown]
# # Moyenne mobile convergence divergence

# %%
#determination de l'indicateur moyenne mobile convergence divergence

ema_rapide = cloture.ewm(span = 12 , adjust = False).mean()
ema_lente = cloture.ewm(span = 26, adjust = False).mean()

# MACD
macd = pd.DataFrame(ema_rapide - ema_lente).rename(columns = {'Close':'MACD'})

# SIGNALE
ema_macd = macd.ewm(span=9,adjust=False).mean()
signale = pd.DataFrame(ema_macd.rename(columns={"MACD":"Signale"}))

# HISTOGRAMME
histogramme = pd.DataFrame(macd['MACD']-signale['Signale']).rename(columns = {0:"hist"})
histogramme.tail() ;


# %%
amzn['MACD'] = macd
amzn['Signale'] = signale
amzn["Histogramme"] = histogramme


# %%
# strategie de trading
cloture = amzn['Close']
macd = amzn['MACD']
signale_macd = amzn['Signale']
k = amzn['%k']
d = amzn['%d']
stock = 0 

prix_achat = []
prix_vente = []
stoc_macd_signal = []
position = []

signal_achat = []
signal_vente = []

achat_et_vente = []


for i in range(len(cloture)) :

    if k.iloc[i]<30 and d.iloc[i]<30 and macd.iloc[i]<-2 and signale_macd.iloc[i]<-2 :
        signal_achat.append(cloture.iloc[i])
        signal_vente.append(np.nan)
        
        if stock != 1 :
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

    elif k.iloc[i]>30 and d.iloc[i]>30 and macd.iloc[i]>2 and signale_macd.iloc[i]>2 :
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

amzn['achat_vente'] = achat_et_vente



# %%
fig  = plt.figure(figsize=(10,3) , dpi=200) 

axe1 = fig.add_axes([0,1,1,1])
amzn['Close'].plot()
axe1.plot(amzn.index ,prix_achat , marker='^',color='green',markersize=10,label = "Signal d'achat",linewidth=2)
axe1.plot(amzn.index ,prix_vente , marker='v',color='red',markersize=10,label = "Signal de vente",linewidth=2)
plt.legend()

axe2 = fig.add_axes([0,0.5,1,0.5])
amzn['MACD'].plot()
amzn['Signale'].plot()
plt.plot([0,365] , [2,2] , color='green' , linewidth=0.5)
plt.plot([0,365] , [-2,-2] , color='red' , linewidth=0.5)
plt.legend()

axe3 = fig.add_axes([0,0,1,0.5]) 
amzn["%d"].plot(label = "%d")
amzn['%k'].plot(label = '%k')
plt.plot([0,365] , [70,70] , color='green' , linewidth=0.5)
plt.plot([0,365] , [30,30] , color='red' , linewidth=0.5)
plt.legend()

plt.show()

# %% [markdown]
# ## Backtesting

# %%
revenu = 0
depart = 100000
d=depart
nombre = 0
total = 0

for i in range( len( amzn ) ) :
    if amzn['achat_vente'].iloc[i] == 'acheter' :

        nombre = depart/amzn['Close'].iloc[i]
        entrer = nombre*amzn['Close'].iloc[i]

    elif amzn['achat_vente'].iloc[i] == 'vendre' :

        sorti = (nombre*amzn['Close'].iloc[i])
        revenu += sorti-entrer
        depart = sorti
    else :
        pass
poucentage_revenu = revenu/d

# %%
poucentage_revenu


