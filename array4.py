import numpy as np
arr = np.array([[2,3,4],[5,6,7]])
print("Sum of the array is =",arr.sum())
print("Array maximum is =",arr.max())
print("Array minimum is=",arr.min())
print(arr.min(axis=1))
print(arr.max(axis=1))
print(arr.cumsum(axis=1))
print(arr.mean(axis=1))

