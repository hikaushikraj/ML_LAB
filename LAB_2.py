# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 16:09:45 2023

@author: kaush
"""

'''1. Create a python list, update the list.'''
ls=[5,4,'fg','k',5]
ls[2]=57
print(ls)

'''2. Create a python tuple, a sub-tuple from it. Compare list and tuple and
 note the inference.'''
tp=(1,2,7,9,13,15,'kl')
sub_tp=tp[3:]
print(sub_tp)

#Inference:- tuples are immutable and are fast to access
'''
3. Create a data set having 20 samples and five features. Check the below functions.
 Shape
 Describe
 Values
 Head
 Groupby
 drop a column'''

import pandas as pd
import random
import numpy as np

#create datset
Dataset=[]
for row in range(20):
    x=[]
    for col in range(5):
        x.append(random.random())
    Dataset.append(x)
print(Dataset)
df=pd.DataFrame(Dataset)
print(df.describe())
print(np.shape(df))
print(df.values)
print(df.head())
print(df.groupby(0).sum(0))
df=df.drop(0,axis='columns')
print(df)
print('*'*50)

'''
4. Read a csv file using pandas and do the following'''
data=pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

data.to_csv('iris')

'''a. Print the information about the data'''
print(data)
'''b. Print the statistical information such as mean, standard deviation'''
print(data.describe())
'''c. Print the data types of each column'''
print(data.dtypes)
'''d. Breakdown of the data by class variable'''

'''e. Importing the data, Splitting the data into training/ test sets
f. Check the functions mentioned in question 3.
5. Write a python program that applies the following loop statements: if, if else, elif, while, for.
6. Write a user defined function program for performing a task.'''
