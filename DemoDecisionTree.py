import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.matrics import accurancy_score

Data = load_iris()
print ('Classes to predict', Data.target_names)
print ('Features', Data.feature_names)

X = Data.data
Y = Data.target

X_Train, X_Test, Y_Train, Y_Test = train.split(X,Y, random_state=50,test_size=0.25)

print(X_Train)
print(Y_Train)
Clf = DecisionTreeClassfier()
print('criteria :', Clf.criterion)
Clf.fit(X_Train)