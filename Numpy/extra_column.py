# Python program to how to add an extra column to an numpy array
# importing the numpy library
import numpy as np

array1 = np.array([[10, 20, 30], [40, 50, 60]])
array2 = np.array([[100], [200]])
print(np.append(array1, array2, axis=1))