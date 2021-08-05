#  Python program to make an array immutable (read-only)
# importing the numpy library
import numpy as np

# creating an array
array1 = np.zeros(10)
# making as immutable array
array1.flags.writeable = False
print(" try to change the value of the first element: ")
# trying to updating the value of the array
array1[0] = 10
