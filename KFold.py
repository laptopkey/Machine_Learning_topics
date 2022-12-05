from sklearn.datasets import load_breast_cancer

import pandas as pd

from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

#Loading the dataset

#instead of returing array, return DataFrame

data = load_breast_cancer(as_frame= True)

df = data.frame
print(df.head)
print(df.coloumns)
#select all coloums but the last coloumn

X = df.iloc[:, :-1]
print(x)

Y = df.iloc[:,:-1]
print(Y)
#selecting only the last (target) coloumn
#implementing cross validation

'''
Kfold will provide train/test indices to split data in train and test sets.
It will split dataset into K consecutive folds(without shuffling by default).
Each fold is then used a validation set once while the k-1 remaining folds 
'''

k = 5
kf = KFOld(n_split= k , random_state=None )
#This is used for linear classification

model = LogisticRegression(solver='liblinear')

acc_score =[]
print(f.split(x))

for train_index, test_index in kf.split(X)
    X_Train, Y_Test = X.iloc(train_index, :), X_iloc[test_index, :]
    print('K =', train_index, X_Train)
    print('K =', test_index, X_test)
    Y_train, Y_Test = Y[train_index], Y[test_index]

    model.fit(X_Train, Y_train)
    pred_values = model.predict(X_test)

    acc = accuracy_score(pred_values, Y_Test)
    print(acc)
    acc_score.append(acc)

avg_acc_score = sum(acc_score) / k

#print('accuracy of each fold - {}', format(acc_score))
#print('avg accuracy: {}',format(avg_score))
print('accuracy of each fold' , acc_score)