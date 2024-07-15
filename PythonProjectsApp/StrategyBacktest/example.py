
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

df = pd.read_csv("BRVM-Financials.csv")[860:1060]
fig, ax = plt.subplots()
print(fig.get_figheight(),
fig.get_figwidth())

fig.set_figwidth(12)
fig.set_figheight(6)
#fig.set_dpi(400)

X = df["Date"].values
Y1 = df["Close"].values
Y2 = df["Close"].rolling(10).mean()
Y3 = df["Close"].rolling(20).mean()

df.set_index("Date")

condition = []
signal_achat = []
signal_vente = []
date_1 = df.index[0]
stock = 0 # permet d'eviter d'acheter quand on pas de stock au debut

for date in df.index :
    if Y2.loc[date] > Y3.loc[date] :
        condition.append(1)
    else :
        condition.append(0)
    
    if( Y2.loc[date] > Y3.loc[date] ) and (Y2.loc[date_1] < Y3.loc[date_1]) and stock == 0:
        signal_achat.append(df["Close"].loc[date])
        stock = 1

    else :
        signal_achat.append(np.nan)

    
    if( Y2.loc[date] < Y3.loc[date] ) and (Y2.loc[date_1] > Y3.loc[date_1]) and (stock == 1):
        signal_vente.append(df["Close"].loc[date])
        stock = 0
    else :
        signal_vente.append(np.nan)
        
    date_1 = date

resistance = [[],[]]
support = [[],[]]
j=0
for i in range(0, len(df) ,30) :
    try :
        
        max_ = df[j:i]['Close'].max()
        min_ = df[j:i]['Close'].min()

        date = df[j:i][df[j:i]['Close']==max_]["Date"].iloc[0]
        date_ = df[j:i][df[j:i]['Close']==min_]["Date"].iloc[0]

        resistance[0].append(date)
        resistance[1].append(max_)

        support[0].append(date_)
        support[1].append(min_)

        j=i

    except Exception as e: print(e)
    
print(resistance)


line1 = ax.plot(X , Y1,linewidth=1)[0]
line2 = ax.plot(X , Y2,linewidth=1)[0]
line3 = ax.plot(X , Y2,linewidth=1)[0]

Y4 = signal_achat ; Y5 = signal_vente
line4 = ax.plot(X , Y4,marker='^',color='green',linewidth=1.5)[0]
line5 = ax.plot(X , Y5,marker='v',color='red',linewidth=1.5)[0]

X6 = resistance[0] ; Y6 = resistance[1]
X7 = support[0] ; Y7 = support[1]
line6 = ax.plot(X6 , Y6 , marker='^',markersize=3,linewidth=0.5)[0]
line7= ax.plot(X7 , Y7 , marker='v',markersize=3,linewidth=0.5)[0]

ax.set(xlim=[0, len(X)] , ylim=[min(Y1), max(Y1)])
ax.legend()
def update(frame) :
    x = X[:frame] ; x6 = X6[:frame] ; x7 = X7[:frame]
    y = Y1[:frame] ; y2 = Y2[:frame] ; y3 = Y3[:frame] 
    y4 = Y4[:frame] ; y5 = Y5[:frame]
    y6 = Y6[:frame]
    y7 = Y7[:frame]
    
    line1.set_xdata(x) ; line2.set_xdata(x) ; line3.set_xdata(x)
    line1.set_ydata(y) ; line2.set_ydata(y2) ; line3.set_ydata(y3)
    
    line4.set_xdata(x) ; line4.set_ydata(y4)
    line5.set_xdata(x) ; line5.set_ydata(y5)
    
    
    ax.set_xticks([] , [])
    ax.set_yticks([], [])

ani = animation.FuncAnimation(fig=fig,func=update,frames=200,interval=40)
plt.show()
#ani.save(filename="image/MAanimation.gif", writer="pillow")
ani.save(filename="image/MAanimation.mp4", writer="ffmpeg")