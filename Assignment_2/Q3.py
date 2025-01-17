# Q.WAP to create a list of 100 random numbers between 100 and 900. Count and print the:
# (i) All odd numbers
# (ii) All even numbers
# (iii) All prime numbers

import random

numbers = []
for _ in range(100):
    numbers.append(random.randint(100,900))

odd_num = []
even_num = []
prime_num = []

for i in numbers:
    if i%2==0:
        even_num.append(i)
    else:
        odd_num.append(i)

    if i>1:
        is_prime = True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime = False
                break
        if is_prime:
            prime_num.append(i)

print(f'\nGenerated numbers are : {numbers}')
print('\n')

print(f'\nTotal odd numbers : {len(odd_num)}')
print('\nOdd numbers : ')
for odd in odd_num:
    print(odd,end = " ")
print('\n')

print(f'\nTotal even numbers : {len(even_num)}')
print('\nEven numbers : ')
for even in even_num:
    print(even,end = " ")
print('\n')

print(f'\nTotal prime numbers : {len(prime_num)}')
print(f'\nPrime numbers : ')
for prime in prime_num:
    print(prime,end = " ")
print('\n')