import numpy as np
import matplotlib.pyplot as plt

#To create hypothetical data with user defined number features and classe
#we use make classification

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import BernoulliNB

#np.random.seed = seed (1000)

noOfSamples = 300

#Create Dataset

X, Y = make_classification(n_samples=noOfSamples, n_features=2, \
                           n_informative=2, n_redundant=0)

print (X)
print (Y)
print (X.shape)

Colors = ['r', 'c']
plt.scatter(X[ :, 0], X[:, 1], c=Y)
plt.show()

X_Tain, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size =0.3)

print (X_Train,"X_Train=",len(X_Train))

print(Y_Train ,"Y_Train = ", len(Y_Train))

print(X_Test, "X_Test =", len(X_Test))

print(Y_Test, "Y_Test =", len(Y_Test))

Bnb = BernoulliNB(binarize=0.0)
Bnb.fit(X_Tain, Y_Train)
print("Training Score = ",Bnb.fit(X_Train, Y_Train))

print("Testing Score = ", Bnb.score(X_Test, Y_Test))