# Q.2 Questions on Basic NumPy Array:
# a) Reverse the NumPy array: arr = np.array([1, 2, 3, 6, 4, 5])

import numpy as np
arr = np.array([1, 2, 3, 6, 4, 5])
print(f"Given Array : {arr}")
arr=arr[::-1]
print(f"Reverse of the array is : {arr}")
print("\n")


# b) Find the most frequent value and their indice(s) in the following arrays:
# i. x = np.array([1,2,3,4,5,1,2,1,1,1])

x = np.array([1,2,3,4,5,1,2,1,1,1])
print(f"Given Array : {x}")
unique_el,count=np.unique(x, return_counts=True)
print(f"The most frequent value is : {unique_el[np.argmax(count)]}")
indices= np.where(x==unique_el[np.argmax(count)])[0]
print(f"It occurs at indices {indices}")
print("\n")


# ii. y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
print(f"Given Array : {y}")
unique_el,count=np.unique(y, return_counts=True)
print(f"The most frequent value is : {unique_el[np.argmax(count)]}")
indices= np.where(y==unique_el[np.argmax(count)])[0]
print(f"It occurs at indices {indices}")

