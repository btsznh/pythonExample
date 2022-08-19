import pandas as pd
import numpy as np
pd.options.display.float_format = '{:.0f}'.format

df = pd.read_csv('C:\\Users\\barat\\Desktop\\python examples\\airlines.csv')
# Getting shape of the df
df.shape

# Printing Number of columns
print('Number of columns :', df.shape[0])
print('isnull', df.isnull().sum())
