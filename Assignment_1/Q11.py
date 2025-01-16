# Q.11.1 Write a program to use the math library to calculate the square root of a given number.
import math
num = float(input('Enter the number : '))
if num < 0:
    print('Error : Square root cannot be calculated')
else:
    sq_rt = math.sqrt(num)
    print(f'The square root of {num} : {sq_rt}')

print('\n')
# Q.11.2 Write a program to use the datetime library to print the current date and time.
import datetime
crt_dateTime = datetime.datetime.now()
print('Current Date and time :',crt_dateTime)

print('\n')
# Q.11.3 Write a program to use the os library to list all files in the current directory.
import os
files = os.listdir()
print('Files and directories in the current directory : ')
for i in files:
    print(i)