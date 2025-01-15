# Q.3.1 Write a Python program to check if a number is positive, negative, or zero using an if-else statement.
a = int(input('Enter a number : '))
if a>0:
    print('Positive number')
elif a<0:
    print('Negative number')
else:
    print('It is 0')

print('\n')
# Q.3.2 Write a program to check if a given number is odd or even.
x = int(input('Enter a number : '))
if x%2==0:
    print('It is even number')
else:
    print('It is odd number')