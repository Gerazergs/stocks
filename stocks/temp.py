# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import yfinance as yf

import pandas as pd

datos = pd.read_csv('SPY500.csv')
print(datos.size)

df2 = pd.DataFrame()
year = '2020'
yearend = '2018'
month = '-11-'
day = '26'
# =============================================================================
# for i in range(0,3):#datos.size):
#     print(datos['stocks'].loc[i])
# 
#     df1 = yf.Ticker(datos['stocks'].loc[i])
#     df = df1.history(start= yearend+month+day, end= year+month+day, interval="1d")
#     
#     #yf.download("AMZN AAPL GOOG", start= yearend+month+day, end= year+month+day, interval="1d", group_by='tickers')
#     
#     #print(type(df1))
#     #df2 = pd.concat(df2,df1[])
#     temp = pd.DataFrame.from_dict(df1, orient="index")
#     print (temp.keys())
# =============================================================================
    
tickers_list = ["aapl", "goog", "amzn", "BAC", "BA"] # example list
tickers_data= {} # empty dictionary

df = pd.DataFrame()
df2 = pd.DataFrame()



for i in datos['stocks'].values.tolist():
    try:
        ticker_object = yf.Ticker(i)
        #convert info() output from dictionary to dataframe
        a =  ticker_object.history(start= yearend+month+day, end= year+month+day, interval="1d")
        temp = pd.DataFrame.from_dict(a)
    
        df[i] = temp['Close']
    except Exception as e:
        print(e)
   
print(df.head())
df.to_csv('spy500_descarga.csv')
   
   