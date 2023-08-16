import numpy as np
arr = np.array([[1,2,3],
                [4,5,6]])
print("Array is of type: ", type(arr))
print("No of dimension : ", arr.ndim)
print("Size of array : ",arr.size)
print("Array store element of type : ",arr.dtype)
print("Array shape is= ",arr.shape)
newarr = arr.reshape(3, 2)
print("Array reshaped is= \n",newarr)

