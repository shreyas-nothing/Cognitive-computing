# Q.3 For the given 2-D array arr=np.array([10, 20, 30], [40, 50, 60], [70, 80, 90]), access
# elements using row and column indices as follows:

import numpy as np
arr=np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(f"Given array is : \n {arr}")
print('\n')
# a) Access 1st row, 2nd column

print(f'The element in 1st row, 2nd column is : {arr[0][1]}')
print('\n')

# b) Access 3rd row, 1st column

print(f'The element in 3rd row, 1st column is : {arr[2][0]}')
print('\n')