# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#kodlar
#veri yukleme

data = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")
data2 = pd.read_csv('eksikveriler.csv')

data3 = pd.read_csv('train.csv')
print(data)
print(data2)
#print(data3)
#eksik veriler


#çalışan eksik değerler
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values=np.nan , strategy = "mean" )
yas = data2.iloc[:,3:4].values
data2["yas"] = imputer.fit_transform(yas)
print(data2)
#print lot eksik değerler
imputer1 = Imputer(missing_values=np.nan , strategy = "mean")
Lot = data3.iloc[:,3:4].values
degisen = data3["LotFrontage"]
print("---Değişim Öncesi--")
print(data3["LotFrontage"])
data3["LotFrontage"] = imputer.fit_transform(Lot)
print("Değişim Sonrası")
print(data3["LotFrontage"])

boykiloyas = data[["boy","kilo","yas"]]
#içinde tr var mı ?
mask_tr = data["ulke"] == "tr" 
print(mask_tr)
mask_fr = data['ulke'] == 'fr'

mask_us = data['ulke'] == 'us'
ulkeler = pd.concat([mask_fr,mask_tr,mask_us],axis = 1)
ulkeler.columns=["fr","tr","us"]
print(ulkeler)
ulkeler["fr"] = ulkeler["fr"].map({True:1,False : 0})
print(ulkeler["fr"])
ulkeler["tr"] = ulkeler["tr"].map({True:1,False : 0})
ulkeler["us"] = ulkeler["us"].map({True:1,False : 0})

sonuc = pd.concat([ulkeler,boykiloyas],axis = 1)
print(sonuc)