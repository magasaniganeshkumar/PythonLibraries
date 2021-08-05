#  Python program to convert a NumPy array into Python list structure
# importing the numpy library
import numpy as np

array1 = np.arange(6).reshape(3, 2)
print(" the numpy array is :")
print(array1)
print("array to list")
list1 = array1.tolist()
print(" the list is :")
print(list1)