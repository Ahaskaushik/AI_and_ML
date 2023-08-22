import pandas as pd
import numpy as np
data = pd.read_csv("C:/Users/SPTINT-04/Desktop/titanic11_12.csv",index_col="Name")
print(data)
print("\n")
print(data.info())
print("\n")
print(data.shape)
print("\n")
print(data[['Age','Survived']])
print("\n")
print(data.loc[data['Age']>50])
print("\n")
print(data['Age'])
print("\n")
print(data.loc['Giglio, Mr. Victor'])
print("\n")
print(data.iloc[1:25,1:5])

