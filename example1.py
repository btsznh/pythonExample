import unicodecsv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from scipy import stats
from scipy.stats import norm

pd.options.display.float_format = '{:.0f}'.format



flights = pd.read_csv('airlines.csv')
x=flights.describe()
print(x)

corrMat=flights.corr()
f,ax = plt.subplots(figsize=(12,9))
sns.heatmap(corrMat, vmax=.8, square=True)
plt.show()



print("imported all")

