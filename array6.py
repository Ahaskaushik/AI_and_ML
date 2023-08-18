import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr.T)
print(arr.sum())
print(arr.sum(axis=1))
print(arr.max())
print(arr.max(axis=1))
print(arr.min())
print(arr.min(axis=1))
print(arr.cumsum())

