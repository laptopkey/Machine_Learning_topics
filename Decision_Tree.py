from sklearn.metrics import accuracy_score
Y_Actual = [0,1, 2, 3, 4, 4]
Y_Pred = [0, 2, 1, 3, 4, 3]

print('Accuracy score', accuracy_score(Y_Actual, Y_Pred))

print('No of correct predictions', accuracy_score(Y_Actual, Y_Pred, normalize = False))
