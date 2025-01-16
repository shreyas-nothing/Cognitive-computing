import sys
# Q.10.1 Write a program to accept two numbers as command-line arguments, add them, and print the result.
if len(sys.argv) != 3:
    print('Enter 2 numbers as an argument : ')
else:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = num1 + num2
        print(f'Result is {result}')
    except ValueError:
        print('Pls provide a valid input')

print('\n')
# Q.10.2 Write a program to accept a string as a command-line argument and print its length.
if len(sys.argv) != 2:
    print('Enter 1 string : ')
else:
    input_str = sys.argv[1]
    print('The length of the string is :',len(input_str))