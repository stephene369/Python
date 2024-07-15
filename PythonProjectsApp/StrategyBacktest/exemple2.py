import matplotlib.pyplot as plt
import pandas as pd

name = "data/BRVM-Agriculture.csv"
name = "data/BRVM-Public-Services.csv"
df = pd.read_csv(name)[1:20]

df["Ouv."]=df["Ouv."].apply(lambda x: str(x).replace(",","") )
df

df['num'] = df[' Plus Haut'].apply(lambda x : len(x) )

df.dtypes
df
