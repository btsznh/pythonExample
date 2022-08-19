import pandas as pd
import numpy as np
# data ={
#         'state': ['tn','delhi','UP','JK'],
#         'capital':['chennai','barath','naren','therla']
# }
# df = pd.DataFrame(data)
# print(df)
random_data = np.random.randint (50,2000,size=(100,3))
df = pd.DataFrame(random_data, columns=['Col1','Col2','Col3'])
# print("head", df.head())
# print("tail", df.tail())
# df.to_csv('RandomNumber.csv')
head = df.head()
tail = df.tail()
# print(head['Col1'].mean())
print(df.describe())