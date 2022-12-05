import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt 
from sklearn.datasets import make_classification


X, y = make_classification(100, 2,n_informative = 2, n_redundant = 0, weights=[0.5,0.5], random_state= 0)

#print(X)
#print(y)

''' 
print(y.shape)
arr = np.array(y)
print(np.where(y == 0))
print(np.where(y ==1))
'''

Clf = svm.SVC(kernel='linear', random_state= 0 )
Clf.fit(X,y)
#print('Support vectors', Clf.support_vectors_)
#print('number', len(Clf.support_vectors_))

#get the seperating hyperplane

print('coef', Clf.coef_)

w = Clf.coef_[0] 
print(w.shape)
print('w is ')
print(w)

#print(Clf.coef_[1])

a = -w[0] / w[1]
print('a is', a)

#Return evenly spaced numbers overa a specified interveral 

xx = np.linspace(-5, 5)
print(xx)
#if there are 2 classses it returns the constrants in decision function 
print('x.intercept', Clf.intercept_[0])
print('clf intercept', Clf.intercept_)

print(Clf.intercept_[0])
print(Clf.intercept_)

yy = a * xx - (Clf.intercept_[0]) / w[1]

print('Points along the hyperplane', yy)
print('Point along the hyper plane', len(yy))
print(yy)

DeciFunc = Clf.decision_function(Clf.support_vectors_)

b = Clf.support_vectors_[0]
print('Shape of support vector', Clf.support_vectors_.shape)
print('Support Vectors down', b)

print(b[1])
print(b[0])

yy_down = a*xx - (b[1]- a * b[0])
print('YY down', yy_down)

b = Clf.support_vectors_[1]
print('support Vectors up', b)

yy_up = a * xx - (b[1] - a *b[0])
print(yy_up)

from mlxtend.plotting import plot_decision_regions
plot_decision_regions(X, y, clf = Clf)

#plot the line , points and nearest vectors to hyperplane
plt.scatter(Clf.support_vectors_[:, 0], Clf.support_vectors_[:, -1], s = 100, facecolors = 'none')


plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')

plt.show()







