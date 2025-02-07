

import numpy as np
import matplotlib.pyplot as plt

# Q.1 For the array gfg = np.matrix([4, 1, 9; 12, 3, 1; 4, 5, 6]), Find
gfg = np.matrix([[4, 1, 9], [12, 3, 1], [4, 5, 6]])

# i. Sum of all elements
sum_all_elements = np.sum(gfg)
print("Sum of all elements:", sum_all_elements)

# ii. Sum of all elements row-wise
sum_row_wise = np.sum(gfg, axis=1)
print("Sum of all elements row-wise:", sum_row_wise)

# iii. Sum of all elements column-wise
sum_column_wise = np.sum(gfg, axis=0)
print("Sum of all elements column-wise:", sum_column_wise)

import numpy as np
import matplotlib.pyplot as plt

# Q.2 (a) For the array: array = np.array([10, 52, 62, 16, 16, 54, 453]), find
array = np.array([10, 52, 62, 16, 16, 54, 453])

# i. Sorted array
sorted_array = np.sort(array)
print("Sorted array:", sorted_array)

# ii. Indices of sorted array
sorted_indices = np.argsort(array)
print("Indices of sorted array:", sorted_indices)

# iii. 4 smallest elements
smallest_elements = np.partition(array, 4)[:4]
print("4 smallest elements:", smallest_elements)

# iv. 5 largest elements
largest_elements = np.partition(array, -5)[-5:]
print("5 largest elements:", largest_elements)

import numpy as np
import matplotlib.pyplot as plt

# Q.2 (b) For the array: array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0]), find
array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])

# i. Integer elements only
integer_elements = array[array == array.astype(int)]
print("Integer elements only:", integer_elements)

# ii. Float elements only
float_elements = array[array != array.astype(int)]
print("Float elements only:", float_elements)

import numpy as np
import matplotlib.pyplot as plt

# Q.3 You are given a weekly sales dataset and need to perform various operations using NumPy broadcasting.

# a) Generate your unique sales dataset
# Let's assume your initials are "A B" → ASCII sum = 65 + 66 = 131
X = 131
sales = np.array([X, X + 50, X + 100, X + 150, X + 200])
print("Sales array:", sales)

# b) Compute your personalized tax rate as ((X % 5) + 5) / 100
tax_rate = ((X % 5) + 5) / 100
print("Tax rate:", tax_rate)

# Use broadcasting to apply this tax rate to each sales value
taxed_sales = sales * (1 + tax_rate)
print("Taxed sales:", taxed_sales)

# c) Adjust sales based on discount
# If sales < X+100, apply a 5% discount
# If sales >= X+100, apply a 10% discount
discounted_sales = np.where(sales < X + 100, sales * 0.95, sales * 0.90)
print("Discounted sales:", discounted_sales)

# d) Expand sales data for multiple weeks
# Create a 3×5 matrix representing three weeks of sales by stacking sales three times using broadcasting
weekly_sales = np.vstack([sales, sales, sales])
print("Weekly sales (3 weeks):", weekly_sales)

# Increase sales by 2% per week using element-wise broadcasting
weekly_sales_increased = weekly_sales * (1 + 0.02) ** np.arange(3)[:, np.newaxis]
print("Weekly sales increased by 2% per week:", weekly_sales_increased)

import numpy as np
import matplotlib.pyplot as plt

# Q4. Generate x values using np.linspace() from -10 to 10 with 100 points
x = np.linspace(-10, 10, 100)

# Use each function from the list below and compute y values using NumPy
# Y = x^2
y1 = x ** 2

# Y = sin(x)
y2 = np.sin(x)

# Y = e^x
y3 = np.exp(x)

# Y = log(|x| + 1)
y4 = np.log(np.abs(x) + 1)

# Plot the chosen function using Matplotlib
plt.figure(figsize=(10, 6))

# Plot Y = x^2
plt.plot(x, y1, label="Y = x^2")

# Add title, labels, and grid for clarity
plt.title("Plot of Y = x^2")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.legend()
plt.show()