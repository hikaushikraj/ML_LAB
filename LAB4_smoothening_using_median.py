# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:34:53 2023

@author: student
"""

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
    #print(df[item].info())
df.info()
print(df.head())