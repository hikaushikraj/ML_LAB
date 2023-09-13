# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:39:19 2023

@author: student
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:34:53 2023

@author: student
"""
def do_normalisation(ls):
    ls.sort()
    mean=np.mean(ls)
    ls_max=np.max(ls)
    ls_min=np.min(ls)
    max_min_diff=ls_max-ls_min
    for i in range(len(ls)):
        ls[i]=(ls[i]-ls_min)/(max_min_diff)
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
    df[item]=do_normalisation(df[item].to_list())
    print(df[item])
    
df.info()
print(df.head(99))