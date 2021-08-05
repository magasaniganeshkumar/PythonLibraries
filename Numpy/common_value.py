# Python program to find common values between two arrays
# importing the numpy library
import numpy as np

# defining two arrays
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])
# displaying two arrays
print("First array is : ", array1)
print("Second array is : ", array2)
# finding the common values between two arrays
common_values = np.intersect1d(array1, array2)
# printing the common values from the two arrays
print("Common values between two arrays :", common_values )