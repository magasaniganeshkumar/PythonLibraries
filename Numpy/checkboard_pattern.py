# Python program to create a 8x8 matrix and fill it with a checkerboard pattern

import numpy as np
array1 = np.zeros((8, 8), dtype=int)
array1[1::2, ::2] = 1
array1[::2, 1::2] = 1
print(array1)