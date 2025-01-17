
# 4.Consider the following sets representing scores of two teams:
# A = {34, 56, 78, 90} and B = {78, 45, 90, 23} . Perform the following operations:

A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# i. Find the unique scores achieved by both teams (union).

print("the unique scores achieved by both teams are : ")
print(A|B)
print(" ")

# ii. Identify the scores that are common to both teams (intersection).

print("the common scores achieved by both teams are : ")
print(A&B)
print(" ")

# iii. Find the scores that are exclusive to each team (symmetric difference).

print("the scores that are exclusive to each team : ")
print(A^B)
print(" ")

# iv. Check if the scores of team A are a subset of team B, and if team B's scores
# are a superset of team A.

print("Check if the scores of team A are a subset of team B")
print(A.issubset(B))
print("Check if team B's scores are a superset of team A")
print(B.issuperset(A))
print(" ")

# v. Remove a specific score X (input by the user) from set A if it exists. If not, print
# a message saying it is not present.

rem_val=int(input("Enter the value to be removed : "))
if rem_val in A:
    A.remove(rem_val)
    print('Value removed')
    print(A)
elif rem_val in B:
    B.remove(rem_val)
    print('Value removed')
    print(B)
else :
    print(f'{rem_val} is not present in the set A or')
    


