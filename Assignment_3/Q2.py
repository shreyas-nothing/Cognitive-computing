
# Q.2 From the above table that you have created, locate row 0, 4, 7 and 8 using DataFrame.


import pandas as pd

dataset={
"Tid":[1,2,3,4,5,6,7,8,9,10],
"Refund":["yes","no","no","yes","no","no","yes","no","no","no"],
"Marital status":["Single","Married","Single","Married","Divorced","Married","Divorced","Single","Married","Single"],
"Taxable Income":["125K","100K","70k","120k","95k","60k","220k","85k","75k","90k"],
"cheat":["No","No","No","No","Yes","No","No","Yes","No","Yes"]
}

df=pd.DataFrame(dataset)



print(df.loc[[0,4,7,8]])


