# Q5. Create a 2-D Array of three rows and four columns, named ucs420_<Shreyas>>
# with following values – 10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 20, 35. 

import numpy as np

ucs420_Shreyas = np.array([
    [10, 20, 30, 40], 
    [50, 60, 70, 80], 
    [90, 15, 20, 35]
])
print(f"Original 2D Array (ucs420_Shreyas):\n{ucs420_Shreyas}\n")

# Compute the mean,median, max, min, unique elements. 

print(f"Mean of array: {np.mean(ucs420_Shreyas)}\n")
print(f"Median of array: {np.median(ucs420_Shreyas)}\n")
print(f"Maximum value: {np.max(ucs420_Shreyas)}\n")
print(f"Minimum value: {np.min(ucs420_Shreyas)}\n")
print(f"Unique elements in the array: {np.unique(ucs420_Shreyas)}\n")

# Reshape the array to four rows and three columns and name it as reshaped_ ucs420_<Shreyas>>. 

reshaped_ucs420_Shreyas = ucs420_Shreyas.reshape(4, 3)
print(f"Reshaped Array (4x3):\n{reshaped_ucs420_Shreyas}\n")

# Resize the array to two rows and three columns and name it as resized_ ucs420_<Shreyas>>.

resized_ucs420_Shreyas = np.resize(ucs420_Shreyas, (2, 3))
print(f"Resized Array (2x3):\n{resized_ucs420_Shreyas}\n")