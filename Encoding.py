# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:19:59 2023

@author: kaush
"""

import pandas as pd

# Create a DataFrame with categorical data
df = pd.DataFrame({'color': ['red', 'green', 'blue','red','yellow','green','blue','green']
                   ,
                   'day':['tue','wed','thu','mon','fri','sat','sun','tue']})

# One-hot encode the categorical data
encoded_df = pd.get_dummies(df, columns=['color'])

# Print the encoded DataFrame

label_encoding=df.copy()
label_encoding['encoded_color']=df['color'].astype('category').cat.codes

#label_encoding=label_encoding.iloc[:,-1::-1]




ordinal_mapping={'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6,'sun':7}
ordinal_encoding=df.copy()
ordinal_encoding['encoded_day']=df['day'].map(ordinal_mapping)

print('#'*5,'ORIGINAL_DATAFRAME','#'*5)
print(df)
print('#'*5,'OneHotEncoded_DATAFRAME','#'*5)
print(encoded_df)
print('#'*5,'LabelEncoded_DATAFRAME','#'*5)
print(label_encoding)
print('#'*5,'OrdinalEncoded_DATAFRAME','#'*5)
print(ordinal_encoding)
