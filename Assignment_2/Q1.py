
# 1.Create a List L defined as [10, 20, 30, 40, 50, 60, 70, 80] and perform the following operations:

L=[10, 20, 30, 40, 50, 60, 70, 80]

# i. Add 200 and 300 to L .

print("After adding 200 , 300 to list")
L.extend([200,300])
print(L)
print(" ")

# ii. Remove 10 and 30 from L .

L.remove(10)
L.remove(30)
print("After removing 10, 30 from list")
print(L)
print(" ")

# iii. Sort L in ascending order.

L.sort()
print("After sorting the list in ascending order")
print(L)
print(" ")

# iv. Sort L in descending order.
L.sort(reverse=True)
print("After sorting the list in descending order")
print(L)
print(" ")

