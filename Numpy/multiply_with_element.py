#  Python program to create an array of (3, 4) shape, multiply every element value by 3 and display the new array
# importing the numpy library
import numpy as np

array1 = np.arange(12).reshape(3, 4)
print("before array elements : ")
print(array1)
for element in np.nditer(array1, op_flags=['readwrite']):
    element[...] = 3 * element
print(" new array elements :")
print(array1)