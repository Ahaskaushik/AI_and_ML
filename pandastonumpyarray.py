import pandas as pd
import numpy as np
a=pd.Series([10,2,3,6,78,12])
b=pd.Series([10,6,9,4,2,7,21])
print(a)
print(b)
unio=pd.Series(np.union1d(a, b))
print("Union of 2 arrays = \n",unio)
interset=pd.Series(np.intersect1d(a, b))
print("Intersect of 2 arrays is =\n",interset)
notcomm=unio[~unio.isin (interset)]
print("not common of 2 arrays = \n ",notcomm)

