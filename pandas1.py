import pandas as pd 

data=pd.read_csv("C:/Users/SPTINT-04/Desktop/dataset/iris.csv")
print(data)
print(data.head(5))
print(data.tail(5))
print(data.shape)
print(data.info())
print(data["SepalLengthCm"].head(5))
print(data.count())
print(data.dtypes)

