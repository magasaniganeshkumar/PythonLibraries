# programme to  add a border around an existing array
import numpy as np
array1 = np.ones((3, 3))
print("Original array is :")
print(array1)
border_zero = np.pad(array1, pad_width=1, mode='constant', constant_values=0)
print("0 on the border and 1 inside in the array")
print(border_zero)