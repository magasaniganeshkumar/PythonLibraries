# Python program to suppresses the use of scientific notation for small numbers in numpy array
# importing the numpy library
import numpy as np

array1 = np.array([1.6e-10, 1.6, 1200, .235])
print(" original array elements :")
print(array1)
print("array value with precision 3 :")
np.set_printoptions(suppress=True)
print(array1)