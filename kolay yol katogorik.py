# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:32:57 2019

@author: Erdo
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#kodlar
#veri yukleme

data = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")

print(data)

boykiloyas = data[["boy","kilo","yas"]]

mask_tr = data['ulke'] == 'tr'


mask_fr = data['ulke'] == 'fr'

mask_us = data['ulke'] == 'us'

ulkeler = pd.concat([mask_fr,mask_tr,mask_us],axis = 1)

ulkeler.columns = ['fr','tr','us']

ulkeler['fr'] = ulkeler['fr'].map({True:1,False:0})

ulkeler['tr'] = ulkeler['tr'].map({True:1,False:0})

ulkeler['us'] = ulkeler['us'].map({True:1,False:0})

sonuc=pd.concat([ulkeler,boykiloyas], axis = 1)

print(sonuc)