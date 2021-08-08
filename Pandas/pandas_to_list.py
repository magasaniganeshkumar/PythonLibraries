# Python program to convert a Panda module Series to Python list and it's type.
# importing  pandas library
import pandas as pd
data = pd.Series([2, 4, 6, 8, 10])
print("Pandas series is : ")
print(data)
print("pandas type is :", (type(data)))
list1 = data.tolist()
print(" python list is :", list1)
print("List type is :", (type(list1)))