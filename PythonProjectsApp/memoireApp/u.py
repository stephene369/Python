import matplotlib.pyplot as plt

from pandas import read_csv


df=read_csv("data/AMAZON.csv" , index_col="Date")

import numpy as np

idex = np.linspace(1 , len(df) , 10 )
idex = [ int(i) for i in idex ]

df.iloc[1].values


idex


plt.figure(figsize=(18,8))
plt.plot(df.index, df["Close"].values )
plt.xticks([])

plt.savefig("images/AMAZON.png")



import matplotlib.pyplot as plt
 
# Creating data
year = ['2010', '2002', '2004', '2006', '208']
production = [25, 15, 35, 30, 10]
 
# Plotting barchart
plt.bar(year, production)
 
# Saving the figure.
plt.savefig("output.jpg")
 
list(df['Close'].values)