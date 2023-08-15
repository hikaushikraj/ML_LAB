# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#1. Generate a sample with 10 features.
import random
sample=[]
for item in range(10):
    sample.append(random.random())
print(sample)

#2. Create a dataset of size 10x10
Dataset=[]
for row in range(10):
    x=[]
    for col in range(10):
        x.append(random.random())
    Dataset.append(x)
#3. Identify the function for identifying array’s total number of elements
print(len(Dataset[0]))
        
'''4. Create a random integer sample vector of dimension 100, 
where all the elements are less than or equal to 50. Using the array indexing
 concept, retrieve the vector’s last and second last elements.'''
vector=[]
for i in range(100):
     vector.append(random.randint(-50,50))
print(vector)     
print(vector[-1:-3:-1])

'''5. Create a random sample matrix, A, of dimension 5x5 and extract the subarray,
 B of size 2x2, from the bottom left corner of A.'''
 
matrix=[]
for row in range(5):
    x=[]
    for col in range(5):
        x.append(random.randint(0,9))
    matrix.append(x)
print(matrix)

#req_matrix=2x2 n being order of matrix
res_matrix=[]
for row in range(len(matrix)-2,len(matrix)): #In left most row starts from (len(row)-req_row,n-1)
    x=[]
    for col in range(2):
        x.append(matrix[row][col])           #In left most column are from (0,req_col-1)
    res_matrix.append(x)
print(res_matrix)

'''6. Convert a random sample 10x10 matrix into a 20x5 matrix'''
'''Let's assume that first 10 rows and 5 columns reamin as is and column
 from 6 to 10 go below the first 10 to form the 20x5 matrix'''
 
new_dataset=[[] for x in range(20)] #creating twenty empty rows 
#print(new_dataset)
for i in range(len(Dataset)):
        new_dataset[i]=Dataset[i][0:5] #assigning index i with 1st 5 elements in row
        #print(new_dataset[i])
        new_dataset[10+i]=Dataset[i][5:len(Dataset)]  #assigning index 10+i with next 5 elements
print(new_dataset)  

'''7. Split the feature array X = [34, 67, 42, 37, 88, 50, 77, 94, 34, 74] 
into three other matrices. The splitting points are 37 and 94.'''

X = [34, 67, 42, 37, 88, 50, 77, 94, 34, 74]
break_point=[37,94]
res=[]
partition=[]
for item in X:
  partition.append(item)
  if item in break_point:
          res.append(partition)
          partition=[]
          break_point.remove(item)
res.append(partition)
print(res)

'''8. Create a sample sequence of 20 evenly spaced numbers between 10 and 20.'''
start=10
stop=20
total=20
d=(stop-start)/(total-1)
sample_sequence=[start+d*i for i in range(20)]    
print(sample_sequence)

'''9. How do you compute the cumulative sum and cumulative product 
of elements in an array?'''
print(sum(sample_sequence))

prod=1
for item in sample_sequence:
    prod*=item
print(prod)

'''10. Obtain the statistical measures of a randomly defined dataset.'''
print(vector)
l=len(vector)
print(l)
print('mean_vector= ',sum(vector)/l)
vector.sort()
print(vector)
print('median_vector is ',sum(vector[l//2:len(vector)//2+2]))

frequency={}
set_vector=set(vector)
for item in set_vector:
    frequency[item]=vector.count(item)
count=max(frequency.values())
print(count)
mode=[]
for key in frequency.keys():
    if frequency[key]==count:
        mode.append(key)
print(mode)
#print(vector.count())
