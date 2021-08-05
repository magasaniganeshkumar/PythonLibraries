# Python program to append values to the end of an array

# importing the numpy library
import numpy as np
# defining an array of elements
array1 = [10, 20, 30]
# printing original array
print("array is :", array1)
# adding the values to the end of array
array1 = np.append(array1, [[40, 50, 60], [70, 80, 90]])
# printing the after  append the values to array
print("After append values to the end of the array is :")
print(array1)