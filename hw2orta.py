# -*- coding: utf-8 -*-
# Created By Erdo
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data3 = pd.read_csv('train.csv')

#print lot  GarageYrBlt","MasVnrArea eksik değerler ortalama ile tamamla
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values=np.nan , strategy = "mean")
degisen = data3[["LotFrontage","GarageYrBlt","MasVnrArea"]]
data3[["LotFrontage","GarageYrBlt","MasVnrArea"]] = imputer.fit_transform(degisen)
print(degisen)

#Change Value to binary all semantic value.(tüm sözelleri al sayısala çevir.)
TransformBinary = data3[["MSZoning","Street"]]
TransformBinary1 = data3.iloc[:,7:17]
TransformBinary2 = data3.iloc[:,21:26]
TransformBinary3 = data3.iloc[:,27:34]
TransformBinary4 = data3["BsmtFinType2"]
TransformBinary5 = data3.iloc[:,39:43]
#TransformBinary6 = data3.iloc[:,53:54]
TransformBinary6 = data3[["KitchenQual","Functional","FireplaceQu","GarageType","GarageFinish"]]
TransformBinary7 = data3.iloc[:,63:66]
TransformBinary8 = data3.iloc[:,72:75] #sonlardaki data anlamsız PoolQC silebilirsin 3 tanesini
TransformBinary9 = data3.iloc[:,78:80]

#delete unnecessary data en son tekrar sil birleştirdikten sonra şuan lazım değil ************
#deleted_column = data3.drop(['Alley',"MasVnrType"],1) *************
#verileri dönüştür sözelleri sayısala 1 2 3 gibi dönüştür
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()


#önce birleştir sonra binary çevir = Selected all value to binary #verileri dönüştür sözelleri sayısala 1 2 3 gibi dönüştür
semantic_value = pd.concat([TransformBinary,TransformBinary1,TransformBinary2,TransformBinary3,TransformBinary4,TransformBinary5,TransformBinary6,TransformBinary7,TransformBinary8,TransformBinary9],axis = 1)
df_encoded = semantic_value.astype(str).apply(le.fit_transform)
print(df_encoded)

#Seperate data wtih binary and numerical value exept nan values
numerical_value = data3.drop(semantic_value ,1)

join_semantic_numerical = pd.concat([df_encoded,numerical_value],axis = 1)
#Remove NA and unnesesary value 
delete_unnecessary_data = join_semantic_numerical.iloc[:,73:78]
delete_unnecessary_data1 = join_semantic_numerical[['Alley']]
join_delete_unnecessary_data = pd.concat([delete_unnecessary_data,delete_unnecessary_data1],axis = 1)
#remove  unnecessary item  from join_semantic_numerical
removed_unnecessary_data = join_semantic_numerical.drop(join_delete_unnecessary_data ,1)
#ready data to calculate rss multiple lineer regression
data_ready = removed_unnecessary_data

#verilerin egitim ve test icin bolunmesi
from sklearn.cross_validation import train_test_split

Train_Data = data_ready.iloc[:,:74]
#get last value = salesprice
Train_SalePrice = data_ready.iloc[:,-1]
x_train, x_test,y_train,y_test = train_test_split(Train_Data,Train_SalePrice,test_size=0.33, random_state=0)

#predict value with library

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
#makine öğrendi
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)






