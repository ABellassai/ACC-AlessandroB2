#1

n = int(input('Give me a fatorial number: '))
def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))

#2

number = int(input('Give me a number: '))
def factorial(number):
    if(number == 1 or number == 0):
        return ('NO')
    else:
        return number + factorial(number-1) + factorial(number-2) 
print(factorial(number))
