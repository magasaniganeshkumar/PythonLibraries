# The set difference will return the sorted, unique values in array1 that are not in array2
import numpy as np

# defining two arrays
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70])
# displaying two arrays
print("First array is : ", array1)
print("Second array is : ", array2)
# finding the unique values between two arrays
difference_values = np.setdiff1d(array1, array2)
# printing the unique values from the two arrays
print("Common values between two arrays :", difference_values)
