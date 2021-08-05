# Python program to create a contiguous flattened array
# importing the numpy library
import numpy as np

# defining an 2D array
array1 = np.array([[10, 20, 30], [20, 40, 50]])
# displaying the 2D array
print(" the array is :", array1)
flattened_array = np.ravel(array1)
print(flattened_array)