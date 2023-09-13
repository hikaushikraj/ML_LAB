# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:24:44 2023

@author: student
"""

def do_binning(ls):
    #import numpy as np
    size=3
    starter=0
    res=[]
    while  starter <len(ls):
        bucket=np.array(ls[starter:size])
        print(bucket)
        mean=np.mean(bucket)
        for i in range(starter,size):
            res.append(mean)
        starter+=3
        size+=3
        print(starter)
        
    return res
        
        
        
    
    
    
    

    
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
    df[item]=do_binning(df[item].to_list())
    print(df[item])
    
df.info()
print(df.head(99))