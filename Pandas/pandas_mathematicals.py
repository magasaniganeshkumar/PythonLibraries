"""
Write a Python program to add, subtract, multiple and divide two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
"""
import pandas as pd
data1 = pd.Series([2, 4, 6, 8, 10])
data2 = pd.Series([1, 3, 5, 7, 9])
add = data1 + data2
print("Add two Series:")
print(add)
print("Subtract two Series:")
sub = data1 - data2
print(sub)
print("Multiply two Series:")
multiply = data1 * data2
print(multiply)
print("Divide Series1 by Series2:")
division = data1 / data2
print(division)