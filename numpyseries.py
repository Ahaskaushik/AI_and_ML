import numpy as np
import pandas as pd
print("series constant values \n")
s=pd.Series(4,index=[1,2,3,4])

print("Index as nan\n")
i=pd.Index([2,1,1 ,np.nan,3])
print(i.value_counts())

print("Array as series= \n")
a=np.array([21,34,54,65,45])
s=pd.Series(a)
print(a)
print(s)

