# Python program to create a 2d array with 1 on the border and 0 inside.

import numpy as np
array1 = np.ones((5,5))
print("Original array:")
print(array1)
array1[1:-1,1:-1] = 0
print("1 on the border and 0 inside in the array")
print(array1)