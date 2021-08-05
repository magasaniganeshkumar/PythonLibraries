"""
Python program to create a null vector of size 10 and
update sixth value to 11. [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] 
Update sixth value to 11
"""   
import numpy as np
null_vector = np.zeros(10)
print(null_vector)
print("Update sixth value to 11 : ")
null_vector[6] = 11
print(null_vector)