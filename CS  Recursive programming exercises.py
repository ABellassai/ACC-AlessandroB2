#1
n = int(input('Give me a fatorial number: '))
def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))

#2
number = 9
def series(number):
    if(number <= 1):
        return 1
    else:
        return series(number-1) + series(number-2)
print('series: ')
for i in range (number):
        print(series(i))

#3
num = int(input('Give me a number: '))
powerNum = int(input('Give me a power: ')) 
def power(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return num**powerNum
print(power(num))
