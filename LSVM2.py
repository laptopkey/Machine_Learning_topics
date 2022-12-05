from turtle import pd
from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt 

#212 records - Maliganth.
#357 recored - begine

Data = load_breast_cancer
#print(Data.feature_names)
#print(Data.target_names)

X = Data.data
Y = Data.target 

#print(X)
#print(Y)

print('Class label', np.unique(Y))

X_Train, X_Test , Y_Train, Y_Test = train_test_split(X,Y, random_state = 50, test_size = 0.25)

Cls = svm.SVC(kernel = 'linear')
Cls.fit(X_Train, Y_Train)

#Present in sklearn.metrics 

Y_Predict_Train = Cls.predict(X_Train)
print('Accuracy Score on Training Data with SVM', accuracy_score(y_true, y_pred = Y_Predict_Train))

Y_Predict_Test = Cls.predict(X_Test)
print('Accuracy Score on Test Data with SVM', accurancy_score(y_true = Y_Test, y_pred = Y_Predict_Test))
      
    
