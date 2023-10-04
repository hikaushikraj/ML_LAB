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
import sklearn

df=pd.read_csv('ai4i2020.csv')
df_=pd.DataFrame()
for item in ['Product ID','Air temperature [K]','Process temperature [K]','Rotational speed [rpm]','Torque [Nm]','Tool wear [min]']:
    df_[item]=df[item]

#print(df_)


for item in ['Air temperature [K]','Process temperature [K]','Rotational speed [rpm]','Torque [Nm]','Tool wear [min]']:
    df_[item].fillna(np.nanmedian(df_[item]),inplace=True)
    
    df_[item]=do_normalisation(df_[item].to_list())
Type=[]
for i in range(len(df_)):
    Type.append(df_['Product ID'][i][0])
df_['Product ID']=Type

mapping={'L':1,'M':2,'H':0}

df_['Product ID']=df_['Product ID'].map(mapping)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5,p=1)
X = df_.drop('Product ID', axis=1)
y = df_['Product ID']

from sklearn.model_selection import train_test_split
X_train, X_test,y_train, y_test = train_test_split(X,y ,
                                   random_state=104, 
                                   test_size=0.25, 
                                   shuffle=True)

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix, ConfusionMatrixDisplay

bayes=GaussianNB()

bayes.fit(X_train,y_train)
y_pred=bayes.predict(X_test)
Accuracy =accuracy_score(y_test,y_pred)
print(Accuracy)


cm=confusion_matrix(y_test, y_pred)
print(cm)
import matplotlib.pyplot as plt
disp=ConfusionMatrixDisplay(cm)
disp.plot()
plt.show()
