# Q.8.1 Write a program to handle division by zero using a try-except block.
try:
    numerator = float(input('Enter the numerator : '))
    denominator = float(input('Enter the denominator : '))
    result = numerator/denominator
    print(f'Result of {numerator}/{denominator} is : {result}')
except ZeroDivisionError:
    print('Error : Division by 0 is not allowed')
except ValueError:
    print('Error : Please enter valid numeric values')


print('\n')
# Q.8.2 Write a program to handle invalid input (e.g., when the user enters a string instead of a number).
try:
    a = float(input('Enter the input : '))
    print(f'Input is {a}')
except ValueError:
    print('Valid input is required')

print('\n')
# Q.8.3 Write a program to demonstrate the use of finally in exception handling.
try:
    numerator = float(input('Enter the numerator : '))
    denominator = float(input('Enter the denominator : '))
    result = numerator/denominator
    print(f'Result of {numerator}/{denominator} is : {result}')
except ZeroDivisionError:
    print('Error : Division by 0 is not allowed')
except ValueError:
    print('Error : Please enter valid numeric values')
finally:
    print('This block is always printed')