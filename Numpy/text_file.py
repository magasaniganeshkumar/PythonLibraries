# Python program to save a NumPy array to a text file
# importing the numpy library
import numpy as np

# creating an array
list1 = [10, 20, 30, 40, 50, 60]
array1 = np.array(list1)
# printing the array
print(" the array is : ", array1)
#  saving array in text file
file = open("numpy_array.txt", "w+")
# converting into string ans assigning to variable
content = str(array1)
# writing content in file
file.write(content)
# closing the file
file.close()