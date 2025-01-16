# Q.5.1 Create a list of 5 numbers. Write a program to find the largest and smallest numbers in the list.
list1 = [1,2,3,4,5]
print('Smallest number in the list : ' + str(min(list1)))
print('Largest number in the list : ' + str(max(list1)))

print('\n')
# Q.5.2 Create a dictionary with at least 3 key-value pairs. Write a program to retrieve the value of a given key.
dict = {1:'One',2:'Two',3:'Three'}
print(dict[2])

print('\n')
# Q.5.3 Write a program to sort a list of numbers in ascending and descending order.
list2 = [23,45,12,31,87,35]
list2.sort()
print(list2)
print('\n')
list2.reverse()
print(list2)

print('\n')
# Q.5.4 Write a program to merge two dictionaries into one.
dict1 = {1:'One',2:'Two',3:'Three'}
dict2 = {4:'Four',5:'Five'}
dict1.update(dict2)
print(dict1)