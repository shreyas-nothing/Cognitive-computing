# 1.Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and perform the following operations:

T=(45, 89.5, 76, 45.4, 89, 92, 58, 45)

# i. Identify the highest score and its index in the tuple.

print(f"The highest score is {max(T)}")
print(f"The index of highest score is {T.index(max(T))}")
print(" ")

# ii. Find the lowest score and count how many times it appears.

print(f"The lowest score is {min(T)}")
print(f"The no of times lowest score scored is {T.count(min(T))}")
print(" ")

# iii. Reverse the tuple and return it as a list.

print("Tupple as a list")
print(f"{list(T[::-1])}")
print(" ")

# iv. Check if a specific score 76 (input by the user) is present in the tuple and print its first occurrence index, or a message saying it’s not present.

if 76 in T:
    print(f"It is present in the tupple and it's index is {T.index(76)}")
else:
    print("It is not present in the tupple")
print(" ")

