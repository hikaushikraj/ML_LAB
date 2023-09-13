# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:09:28 2023

@author: student
"""

def do_standardisation(ls):
    ls.sort()
    mean=np.mean(ls)
    dev=np.std(ls)
    
    for i in range(len(ls)):
        ls[i]=(ls[i]-mean)/dev
    return ls

    
import pandas as pd
import numpy as np
df=pd.read_csv('dataset.csv')
print(df.info())
df_drop_null=df.dropna()
print(df_drop_null.info())
columns=df.columns[1:]
print(columns)
print(df.head())

for item in columns:
    df[item].fillna(np.nanmedian(df[item]),inplace=True)
    print(df[item])
    df[item]=do_standardisation(df[item].to_list())
    print(df[item])
    
df.info()
print(df.head(99))