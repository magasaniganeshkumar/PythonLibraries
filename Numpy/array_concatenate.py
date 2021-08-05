# Python program to concatenate two 2-dimensional arrays
# importing the numpy library
import numpy as np

# defining two arrays
array1 = np.array([[0, 1, 3], [5, 7, 9]])
array2 = np.array([[0, 2, 4], [6, 8, 10]])
print("first array : ")
print(array1)
print("second array : " )
print(array2)
# concatenating the two arrays
array3 = np.concatenate((array1, array2), 1)
print(" after concatenation : ")
print(array3)