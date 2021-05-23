import pandas as pd

data=pd.read_csv("ETHUSD_Bitfinex_D_historical.csv")

print(data.info())
print("===========")

missingdata=data.isnull()

new_data=data.dropna(axis=1)
print(data.shape,new_data.shape)

print("===========")

new_datameta=data.drop_duplicates()
print(data.shape,new_datameta.shape)

print("=====--=====")