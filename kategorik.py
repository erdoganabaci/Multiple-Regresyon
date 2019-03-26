#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 04:18:20 2018

@author: sadievrenseker
"""

#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#kodlar
#veri yukleme

veriler = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")

print(veriler)

#eksik veriler

from sklearn.preprocessing import Imputer

imputer= Imputer(missing_values='NaN', strategy = 'mean', axis=0 )    

Yas = veriler.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)

#veri on isleme
boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)

x = 10

class insan:
    boy = 180
    def kosmak(self,b):
        return b + 10

ali = insan()
print(ali.boy)
print(ali.kosmak(90))

#iloc[satır,sütun almak için]
ulke = veriler.iloc[:,0:1].values
print(ulke)
#herbir değere sayısal değer koyar
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
#verilerin ülke kolonundan 0. yani tek eleman vardı o da ülkeyi al tekrar ülkenin içine yaz
ulke[:,0] = le.fit_transform(ulke[:,0])
print(ulke)
#ülkeri katogarik hale getiriyor.1 0 a çeviriyor.
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)
print(veriler)
#dataframe çevir
sonuc = pd.DataFrame(data = ulke , index = range(22) , columns = ["fr","tr","us"])
print(sonuc)
sonuc2 = pd.DataFrame(data = Yas , index = range(22) , columns = ["boy","kilo","yas"])
print(sonuc2)
cinsiyet = veriler.iloc[:,-1:]
print(cinsiyet)   
sonuc3 = pd.DataFrame(data = cinsiyet , index = range(22) , columns = ["cinsiyet"] )  
print(sonuc3) 
#colonları indexlerle satır sütun olarak eşleştir.  
s = pd.concat([sonuc,sonuc2] , axis=1)    
print(s) 
s2 = pd.concat([s,cinsiyet],axis=1)  
print(s2)
    
    
    

