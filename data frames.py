import pandas as pd

raw_data = {'first_name':['rupali','rakshita','sangeeta'],'last_name':['sharma','kapoor','rana'],'roll_no':['001','002','003'],'test1':[7,8,6],'test2':[44,66,52]}

print(raw_data)
print(type(raw_data))
print(raw_data.keys())
print(raw_data.values())
print(raw_data.items())

Df0 = pd.DataFrame()
print(Df0)
Df1 = pd.DataFrame(raw_data)
print(Df1)

Df1 = pd.DataFrame(raw_Data)
print(Df1)

Df1['Class'] = 'BCA'
print(Df1)

#Add a new column after data frame is created
#df1[<column name>] = [<value>]

Df1['Total'] = Df1['test1'] + Df1['test2']
print(Df1)

print(Df1.columns)

Df2 = Df1.drop.duplicates(subset=['first_name'])
print(Df2)

import matplotlib.pyplot as plt

print(Df2['first_name'])

X = Df2.first_name
Y = Df2.total

plt.scatter(X , Y)

plt.show()



