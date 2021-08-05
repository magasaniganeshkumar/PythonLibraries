# Python program to convert a list and tuple into arrays
# importing the numpy library
import numpy as np

# defining an list of elements
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# defining an tuple of elements
tuple1 = ([8, 4, 6], [1, 2, 3])
# converting list to array by using numpy library
list_array = np.asarray(list1)
# converting tuple to array by using numpy library
tuple_array = np.asarray(tuple1)
# printing the arrays
print("list to array is :", list_array)
print("tuple to array is :")
print(tuple_array)
