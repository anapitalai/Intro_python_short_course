##pip install scikit-learn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model as lm

#Linear Regression is simply fitting a straight line to the data, a best fit line.

#read file csv
df=pd.read_csv('sales.csv')

#plot the data

plt.xlabel('sales')
plt.ylabel('productivity')
plt.scatter(df.sales,df.productivity,color="red",marker="+")
plt.show()


