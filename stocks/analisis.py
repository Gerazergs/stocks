# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:47:23 2020

@author: Gera-pc
"""

import pandas as pd
import numpy as np


datos = pd.read_csv('SPY500_descarga.csv')
df = pd.read_csv('SPY500.csv')

lista2 = df['stocks'].values.tolist()

df = pd.DataFrame()
df2 = pd.DataFrame()
x=0
datos = datos.sort_index(ascending=False)

for i in lista2:
    
    datos[i+'-W']=  datos[i].shift(1)
   
    datos[i] = np.log(datos[i+'-W']/datos[i])
    datos= datos.drop([i+'-W'], axis=1)
    
    x+=1
    if x==10:
        break


datos = datos.drop(datos.iloc[:,0].count()-1, axis =0)
datos = datos.reset_index()
datos = datos.drop('index', axis=1)
#print(datos)
#print(datos.head(10))
rendimiento = datos.mean()*256
#print(rendimiento)
std = datos.std()
riesgo = std * np.sqrt(datos.count())
coeficiente_variacion = riesgo/rendimiento
#print(riesgo)
#print(coeficiente_variacion)

df_nuevo = pd.DataFrame()
df_nuevo = pd.concat([rendimiento,riesgo,coeficiente_variacion], axis =1)
df_nuevo.columns =['rendimento','riesgo','coeficiente_variacion']
print(df_nuevo.head())
