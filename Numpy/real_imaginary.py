"""
Python program to find the real and imaginary parts of an array of complex numbers.
Expected Output:
Original array [ 1.00000000+0.j 0.70710678+0.70710678j]
Real part of the array:
[ 1. 0.70710678]
Imaginary part of the array:
[ 0. 0.70710678]
"""
import numpy as np
array1 = np.sqrt([1+0j])
array2 = np.sqrt([0+1j])
print("Original array:x ", array1)
print("Original array:y ", array2)
print("Real part of the array:")
print(array1.real)
print(array2.real)
print("Imaginary part of the array:")
print(array1.imag)
print(array2.imag)
