# Python program to Compare two arrays
# importing the numpy library
import numpy as np

array1 = np.array([1, 2])
array2 = np.array([4, 5])
print("first array :", array1)
print("second array :", array2)
print("array1 > array2")
print(np.greater(array1, array2))
print("array1 >= array2")
print(np.greater_equal(array1, array2))
print("array1 < array2")
print(np.less(array1, array2))
print("array1 <= array2")
print(np.less_equal(array1, array2))