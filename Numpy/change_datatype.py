# Python program to change the data type of an array
# importing the numpy library
import numpy as np
array1 = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(array1)
print("the data type of an array is :")
print(array1.dtype)
# changing the data type of int_array
array2 = array1.astype(float)
print(" the new data type of the array2 is :")
print(array2)
print(array2.dtype)
