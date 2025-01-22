
# Q.3 Navigate the DataFrame and do the following task for the table created in question 1:



import pandas as pd

dataset={
"Tid":[1,2,3,4,5,6,7,8,9,10],
"Refund":["yes","no","no","yes","no","no","yes","no","no","no"],
"Marital status":["Single","Married","Single","Married","Divorced","Married","Divorced","Single","Married","Single"],
"Taxable Income":["125K","100K","70k","120k","95k","60k","220k","85k","75k","90k"],
"cheat":["No","No","No","No","Yes","No","No","Yes","No","Yes"]
}

# 1. Select row from index 3 to 7.

df=pd.DataFrame(dataset)
print(df.iloc[3:7])
print(" ")
print(" ")

# 2. Select row from index 4 to 8, and column 2 to 4.

print(df.iloc[4:8,2:4])
print(" ")
print(" ")

# 3. Select all rows with column index 1 to 3 (include index 3 during selection).

print(df.iloc[:,1:4])




