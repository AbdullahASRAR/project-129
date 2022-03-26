import csv
import pandas as pd
df=pd.read_csv('dwarf_stars.csv')
df=df.dropna()
df["Radius"]=0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"]=0.000954538*df["Mass"]

df.to_csv('connverted_stars.csv')
