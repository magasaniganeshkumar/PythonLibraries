# python programme to set exclusive-or of two arrays, unique values that are in only one (not both) of the input arrays
# importing the numpy library
import numpy as np

array1 = np.array([0, 10, 20, 40, 60, 80])
print(" array1 : ", array1)
array2 = np.array([10, 30, 40, 50, 70])
print("array2 :", array2)
print(" unique values that are in only one (not both) of the arrays: ")
print(np.setxor1d(array1, array2))
