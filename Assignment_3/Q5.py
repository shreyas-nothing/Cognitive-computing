#Q.5 From the csv file (uploaded in the Q.4) delete row 4, and delete column 3. Display the result.

import pandas as pd



df=pd.read_csv("C:/Users/shrey/Desktop/Tempo/archive/Iris.csv")

f=df.drop(index=4,columns=df.columns[2])


print(f)
