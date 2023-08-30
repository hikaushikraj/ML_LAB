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
#import random
import numpy as np
from sklearn.model_selection  import *

#create datset
np.random.seed(100)
array=np.random.randint(0,9,size=(20,5))


df = pd.DataFrame(array)
print(df)


print(np.shape(df))
print(df.shape)
print(df.describe())
print(df.values)
print(df.head())
print(df.groupby(0))
df=df.drop(0,axis='columns')
print(df)
print('*'*50)
'''
4. Read a csv file using pandas and do the following'''
data=pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',names=['Sepal_length','Sepal_width','Petal_length','Petal_width','Species'])

data.to_csv('iris')

'''a. Print the information about the data'''
print(data.info())
'''b. Print the statistical information such as mean, standard deviation'''
print(data.describe())
'''c. Print the data types of each column'''
print(data.dtypes)
'''d. Breakdown of the data by class variable'''
grp_data = data.groupby('Species')
print(grp_data)
print('Group 1 Iris_setosa :  ',grp_data.get_group('Iris-setosa').head(3),sep='\n',end='\n\n')
print('Group 2 Iris_virginica :  ',grp_data.get_group('Iris-virginica').head(3),sep='\n',end='\n\n')
print('Group 3 Iris_versicolor :  ',grp_data.get_group('Iris-versicolor').head(3),sep='\n')

'''e. Importing the data, Splitting the data into training/ test sets'''
X_train, X_test, y_train, y_test = train_test_split(data.drop(data.columns[-1],axis=1),data['Species'], test_size=0.2, random_state=100)
print('X Trainig data size :  ',len(X_train),end='\n\n')
print('Y Trainig data size :  ',len(y_train),end='\n\n')
print('X Testing data size :  ',len(X_test),end='\n\n')
print('Y Testing data size :  ',len(y_test),end='\n\n')
print(X_train.head())
'''
f. Check the functions mentioned in question 3.

5. Write a python program that applies the following loop statements: if, if else, elif, while, for.
6. Write a user defined function program for performing a task.'''
