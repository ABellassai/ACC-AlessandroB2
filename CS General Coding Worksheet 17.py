# 1. Write a program that prints ‘Hello World’ to the screen
print('Hello World')

# 2. Write a program that asks the user for their name and greets them with their name
name = input('Enter your name: ')
if name.isalpha() == True:
    print('Welcome', name)
else:
    print('Put your real name')

# 3. Modify the previous program such that only the users Alice and Bob are greeted with their names
newName = input('Enter your name: ')
if newName.isdigit() == True:
    print('Put your real name!')
elif newName == 'Bob':
    print('Welcome Bob')
elif newName == 'Alice':
    print('Welcome Alice')
elif newName != 'Alice' or 'Bob':
    print('Hello Stranger')

# 4. Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
number = int(input('Give me a number: '))
def recursive(n):
    if n == 1:
        return n
    else:
        return n + recursive(n - 1)
print(recursive(number))

# 5. Modify the previous program such that only multiples of three or five are considered in the
# sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
number = int(input('Give me a number: '))
def recursive(n):
    if n == 1:
        return n
    else:
        return n + recursive(n - 1)
print(recursive(number))

# 6. Write a program that asks the user for a number n and gives them the possibility to choose
#between computing the sum and computing the product of 1,…,n.
number2 = int(input('Give me a number: '))
choice = int(input('Pick either - 1 for sum or 2 for factorial: '))
if choice != 1 and choice != 2:
    print('Pick one or two I said')
elif choice == 1:
    def sum1(n):
        if n == 1:
            return n
        else:
            return n + sum1(n - 1)
    print(sum1(number2 ))
elif choice == 2:
    def factorial(n):
        if n == 1:
            return n
        else:
            return n * factorial(n - 1)    
    print(factorial(number2 ))

# 7. Write a program that prints a multiplication table for numbers up to 12.
multiplication = int(input('Give me a number to multiply: '))
factor = 1
while factor <= 12:
    print(multiplication, 'x', factor, '=', multiplication * factor)
    factor += 1

# 8. Write a program that prints all prime numbers between 1 and 100
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
num = '' 
print()

# 9. Write a guessing game where the user has to guess a secret number. After every guess the
# program tells the user whether their number was too large or too small. At the end the number of tries
# needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

import math
import random
integerA = int(input('Enter a number: '))
integerB = int(input('Enter another number: '))
while (integerA == integerB):
    print('The two integers cannot be equal!')
    integerA = int(input('Enter a lower number: '))
    integerB = int(input('Enter a higher number: '))
if (integerA > integerB):
    oldB = integerB
    integerB = integerA
    integerA = oldB
randomChoice = random.randint (integerA, integerB)

minNumberGuesses = (round(math.log(integerB-integerA + 1, 2)))
print('You have ',minNumberGuesses,'guesses')
answer = input('Guess the number the system generated: ')
minNumberGuesses -= 1
while answer != str(randomChoice) and minNumberGuesses > 0:
    if answer > str(randomChoice):
        answer = input('Too high, try again')
    elif answer < str(randomChoice):
        answer = input('Too low, try again')
    minNumberGuesses -=1

if answer == str(randomChoice):
    print('Correct, your number was ' + str(randomChoice))
else:
    print('You are out of guesses looser AHAHAHAHA!')
    print('The number the computer picked was',randomChoice)
    
# 10. Write a program that prints the next 20 leap years
year=2022
for i in range(0, 20):
    print(year + i*4)
