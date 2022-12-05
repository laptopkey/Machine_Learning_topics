import pandas as pd
from sklearn.linear_model import Perceptron

weights = [-0.1,0.2065364014000007]
Df1 = pd.read_excel('D:\CLG\SEM III\hons\PLA 1.xlsx')

X = Df1.iloc[:,0:2]

Y = Df1.iloc[:,-1]

clf = Perceptron(max_iter= 100, verbose = 0, random_state = 2017, fit_intercept= True, eta0= 0.002)

clf.fit(X,Y)
print('Prediction:', str(clf.predict(X)))
print('Actual:', Y)
print('Accuracy:' , str(clf.score(X,Y)*100),"%")
print('No of iterations', clf.n_iter_)
print('X1 weight:', clf.coef_[0,0])
print('X2 weight:',clf.coef_[0,1]
      