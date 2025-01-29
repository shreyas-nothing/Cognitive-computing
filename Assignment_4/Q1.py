#  Q.1 Write a program to create a NumPy 1D-array with 5 elements and perform basic
# operations like:

import numpy as np

a=np.array([1,2,3,4,5])
print("Original Array:")
print(a)
print('\n\n')

# a) Addition of 2 in all the element

print("Array after adding 2 to all elements:")
a=a+2
print(a)
print('\n\n')


# b) Multiply 3 with all the elements

print("Array after multiplying all elements by 3:")
a=a*3
print(a)
print('\n\n')

# c) Divide every element by 2

print("Array after dividing all elements by 2:")
a=a/2
print(a)