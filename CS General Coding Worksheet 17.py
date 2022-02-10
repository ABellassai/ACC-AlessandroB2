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


# 6. Write a program that asks the user for a number n and gives them the possibility to choose
# between computing the sum and computing the product of 1,…,n.


# 7. Write a program that prints a multiplication table for numbers up to 12.


# 8. Write a program that prints all prime numbers between 1 and 100


# 9. Write a guessing game where the user has to guess a secret number. After every guess the
# program tells the user whether their number was too large or too small. At the end the number of tries
# needed should be printed. It counts only as one try if they input the same number multiple times consecutively.


# 10. Write a program that prints the next 20 leap years.

