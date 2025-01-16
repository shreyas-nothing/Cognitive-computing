# Q.6.1 Write a program to count the number of vowels in a given string.
a = 'abgjheihdu'
vowels = 'aeiouAEIOU'
count = 0
for i in a:
    if i in vowels:
        count += 1
print(count)

print('\n')
# Q.6.2 Write a program to reverse a string and print it.
x = 'Sukhman'
reversed = x[::-1]
print(reversed)

print('\n')
# Q.6.3 Write a program to check if a string is a palindrome.
b = 'Ara'
b = b.lower()
c = b[::-1]
if c==b:
    print('It is palindrome')
else:
    print('Not a palindrome')