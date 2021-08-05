"""
Python program to create an array which looks like below array. Expected Output:
[[ 0. 0. 0.]
[ 1. 0. 0.]
[ 1. 1. 0.]
[ 1. 1. 1.]]

"""
# importing the numpy library
import numpy as np
array1 = np.tri(4, 3, 1)
print(array1)