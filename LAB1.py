# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
#Qu4estion 1,2,3
dataset=[]
for j in range(10):
    sample=[]
    for i in range(10):
        sample.append(random.random())
    print(sample)
    dataset.append(sample)
print(dataset)

print('Row Count ',len(dataset))

#Question 4
sample_vector=[]
for i in range(100):
    sample_vector.append((random.randint(-156132156135,50)))
print(sample_vector)

print(sample_vector[-1:-3:-1])

#Question 5
A=[]
for j in range(5):
    sample=[]
    for i in range(5):
        sample.append(random.randint(0,9))
    print(sample)
    A.append(sample)
print(A)

#fetch leftmost nxn matrix from the given matrix of NxN
Rows=[3,4]    #N+1-n to N-1
columns=[0,1] #0 to n
sub_matrix=[]
for length of rangeA:
    
    

#convert a random sample matrix of nxn into 2nxn/2

#7
x = [34, 67, 42, 37, 88, 50, 77, 94, 34, 74]
break_point=[37,94]
for item in break_point:
    coll=[]
    for ele in x:
        if ele!=x:
            coll.append(ele)
        else:
            continue
#8
sample=[]
start=10
finish=20
total=20
step=(finish-start)/total
print(step)
x=start
while x<20:
    
    sample.append(x)
    x=x+step
    
print(sample)

#9 Sum and product of array elements
arr_sum=0

arr_prod=1
for item in sample:
    arr_sum+=item
    arr_prod*=item
    
print('Sum is ',arr_sum)
print('Prod is ',arr_prod)

#10 Statistical measures
print('mean is ',arr_sum/20)
print('median is ',sum([sample[int(total/2)],sample[(int(total/2+1))]]))

            
    
    




    


