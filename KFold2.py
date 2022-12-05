











X = df.iloc[:, :-1]
print(x)
Y = df.iloc[:, :-1]
print(Y)

k = 5
kf = KFold(n_splits=k, random_state=None)
model = LogisticRegression(solver='liblinear')

'''
"Cross_val_score" splits the data into say 5 folds. 
Then for each fold it fits the data on 4 folds and scores the 5th fold. 
The it gives you the 5 scores from which you can calculte a mean and variance for the score.
you crossval to tune parameters and get an estimate of th score .
'''

result  = cross_val_score(model, X, Y, cv=kf)
print(result)
print("avg accuracy: {}".format)