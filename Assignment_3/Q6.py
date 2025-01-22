import pandas as pd

employees = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

df=pd.DataFrame(employees)

# a) Shape (number of rows and columns) of the DataFrame.

print("The shape of the data frame is : ")
print(df.shape)
print(" ")
print(" ")

# b) Summary of the DataFrame that includes the data types and non-null counts for
# each column.

print("The Summary of the data frame is : ")
print(df.info())
print(" ")
print(" ")

# c) Generate descriptive statistics.

print("The descriptive statistics of the data frame is : ")
print(df.describe())
print(" ")
print(" ")

# d) Display the first 5 rows and last 3 rows of the dataset.

print("Displaying the first 5 rows and last 3 rows of the dataset : ")
print(df.iloc[5:-3])
print(" ")
print(" ")

# e) Calculate the following statistics from the dataset:

# i. The average salary of employees.

print("The average salary of employees is :")
print(df["Salary"].mean())
print(" ")
print(" ")

# ii. The total bonus paid to all employees.

print("The total bonus paid to all employees : ")
print(df["Bonus"].sum())
print(" ")
print(" ")

# iii. The youngest employee's age.

print("The youngest employee's age : ")
print(df["Age"].min())
print(" ")
print(" ")
# iv. The highest performance rating.

print("The highest performance rating : ")
print(df["Rating"].max())
print(" ")
print(" ")
# f) Sort the DataFrame by the Salary column in descending order.

print("Sort the DataFrame by the Salary column in descending order : ")
print(df.sort_values(by="Salary", ascending=False))
print(" ")
print(" ")

# g) Add a new column that categorizes employees based on their performance rating:
# i. Excellent for ratings >= 4.5
# ii. Good for ratings >= 4.0 but < 4.5
# iii. Average for ratings < 4.0

df["Performance"] = pd.cut(
df["Rating"],
bins=[0, 4.0, 4.5, 5],
labels=["Average", "Good", "Excellent"])
print(" ")
print(" ")
# h) Identify missing values in the DataFrame.

print(df.isnull().sum())
print(" ")
print(" ")
# i) Rename the Employee_ID column to ID.

print("Rename the Employee_ID column to ID")
df.rename(columns={"Employee_ID": "ID"},inplace=True)
print(" ")
print(" ")
# j) Find all employees who:

# i. Have more than 5 years of experience.

exp = df[(df["Years_of_Experience"] > 5)]
print("\nEmployees with >5 years experience:\n",exp)
print(" ")
print(" ")
# ii. Belong to the IT department.

it = df[(df["Department"] == "IT")]
print("\nEmployees in IT:\n",it)
print(" ")
print(" ")
# k) Modify the dataset by adding a new column, Tax, which deducts 10% of the  Salary.

df["Tax"] = ((df["Salary"])-(df["Salary"] * 0.10))
print("\nAdded Tax column:\n",df)
print(" ")
print(" ")
# l) Save the modified DataFrame (with added columns) to a new CSV file.

df.to_csv("employees.csv",index=False)
print("\nModified dataset saved to 'employees.csv'.")
print(" ")
print(" ")
