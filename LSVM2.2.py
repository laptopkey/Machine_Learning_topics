from sklearn.datasets import make_classification
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score

# Data = load_breast_cancer()

# X = Data.data
# Y = Data.target

# X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y,random_state=50, test_size=9)

# Cls = svm.SVC(kernel="linear")
# Cls.fit(X_Train,Y_Train)

# Y_Predict_Train = Cls.predict(X_Train)

# print(accuracy_score(y_true = Y_Train, y_pred = Y_Predict_Train))


# Y_Predict_Test = Cls.predict(X_Test)

# print(accuracy_score(y_true = Y_Test, y_pred = Y_Predict_Test))



X, y = make_classification(100, 2,n_informative = 2, n_redundant = 0, weights=[0.5,0.5], random_state= 0)

# print(X)
# print(Y)

Clf = svm.SVC(kernel="linear", random_state=0)
Clf.fit(X,y)

# print(f"Support Vectors: {Clf.support_vectors_}")
# print(f"Numbers: {len(Clf.support_vectors_)}")

print(Clf.coef_)

w = Clf.coef_[0]
print(w)
print(w.shape)
a = -w[0]/w[1]
print('a is ',a)

xx= np.linspace(-5,5)
print(xx)
print('x intercept', Clf.intercept_[0])
print('clf intercept', Clf.intercept_)

print(Clf.intercept_[0])
print(Clf.intercept_)


yy = a+xx-(Clf.intercept_[0])/w[1]
print('Points along the hyperplane', yy)
print('Points along the hyperplane', len(yy))
plt.plot(xx,yy)
plt.show()

print(yy)