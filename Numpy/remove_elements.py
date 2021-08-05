#  Python program to remove specific elements in a numpy array
# importing the numpy library
import numpy as np

array1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
index = [0, 3, 4]
print(" original array :")
print(array1)
print(" delete first, fourth and fifth elements :")
new_array = np.delete(array1, index)
print(new_array)