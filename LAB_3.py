# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:34:19 2023

@author: kaush
"""

import pandas as pd
import numpy as np
data=pd.read_csv('iris_csv.csv')
data.columns=['Sepal_length','Sepal_width','Petal_length','Petal_width','Species']

def calc_mean(ls):
    total=0
    count=0
    for item in ls:
        if item != None and type(item) in [float,int]:
            total+=item
            count+=1
    return total/count
def calc_median(ls):
   
    #ls=ls.tolist()
   
    ls.sort()
    l=len(ls)
    if l%2==0:
        return (ls[(l//2-1)]+ls[l//2])/2
    else:
        return ls[l//2]
def calc_mode(ls):
    #ls=ls.tolist()
    frequency={}
    set_ls=set(ls)
    for item in set_ls:
        frequency[item]=ls.count(item)
    count=max(frequency.values())
    
    mode=[]
    for key in frequency.keys():
        if frequency[key]==count:
            mode.append(key)
    return mode

def calc_range(ls):
    ls.sort()
    return ls[-1]-ls[0]

def calc_quantile(ls):
    ls.sort()
    l=len(ls)
    if (l+1)%4==0:
        q1=(l+1)/4
        q1_val=ls[q1-1]
        q2=(l+1)/2
        q2_val=ls[q2-1]
    else:
        q1=(l+1)//4
        q1_val=(ls[q1-1]+ls[q1])/2
        q2=(l+1)//2
        q2_val=(ls[q2-1]+ls[q2])/2
    if ((l+1)*3)%4==0:
        q3=(l+1)*3/4
        q3_val=ls[q3-1]
    else:
        q3=(l+1)*3//4
        q3_val=(ls[q3-1]+ls[q3])/2
    iqr=q3_val-q1_val
    
    return {'q1':q1_val,'q2':q2_val,'q3':q3_val,'iqr':iqr}
    
columns=data.columns     
for item in columns:
    ls=data[item]
    if np.dtype(data[item]) in [float,int]:
                ls=ls.tolist()
                print('CENTRAL TENDENCY')
                print('Mean: '+item,calc_mean(ls))
                print('Median: '+item,calc_median(ls))
                print('Mode: '+item,*calc_mode(ls))
                print('#'*50)
                print('DATA DISPERSION')
                print('Range: '+item,calc_range(ls))
                print('Quartiles ',calc_quantile(ls))
import matplotlib.pyplot as plt
plt.figure(figsize = (10, 7))
data.boxplot()
plt.scatter(data.Sepal_length,data.Sepal_width)
plt.xlabel("Sepal_length")
plt.ylabel("Sepal_width")
plt.scatter(data.Sepal_length,data.Petal_length)
plt.scatter(data.Sepal_width,data.Petal_width)
plt.scatter(data.Petal_length,data.Petal_width)


class_size={'A':30,'B':25,'C':45}
data=[]
for class_label,num_sample in class_size.items():
   for i in range(num_sample):
       row=[]
       f1=np.random.randint(0,50)
       f2=np.random.randint(0,50)
       f3=np.random.randint(0,50)
       row=[f1,f2,f3,class_label]
       data.append(row)
dataset=pd.DataFrame(data,columns=['f1','f2','f3','class'])
#print(dataset)
columns=dataset.columns
#print(columns)     
for item in columns:
    #print(np.dtype(dataset[item]))
    ls=dataset[item]
   # print(ls)
    if np.dtype(dataset[item]) in [float,'int64']:
                print('hi')
                ls=ls.tolist()
                print('CENTRAL TENDENCY')
                print('Mean: '+item,calc_mean(ls))
                print('Median: '+item,calc_median(ls))
                print('Mode: '+item,*calc_mode(ls))
                print('#'*50)
                print('DATA DISPERSION')
                print('Range: '+item,calc_range(ls))
                print('Quartiles ',calc_quantile(ls)

                
                
                

                

    
        

        
