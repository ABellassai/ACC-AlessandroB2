
#1
number = 0
total = 0
while number < 10:
    total += int(input('Enter Numbers: '))
    number+=1
average = total / number
print('Average of numbers is ' + str(average) + '!')

#2
moltiplication = 24
factor = 1
while factor <= 12:
    print(moltiplication, 'x', factor, '=', moltiplication * factor)
    factor += 1

#3
while True:
    print('Infinite LOOOOOOOP')

#4
n=""
while type(n)!= int:
    try:
        n = int(input('Enter a number to find its factorial: '))
    except ValueError:
        print('This isnt an integer!')
        pass

multiply = 1
total = 1
while multiply <= n:
    total = total * multiply
    multiply += 1
    
print(total,'is the factorial of',n)

#5
firstNumber = int(input('Enter your first number to have its Greatest Common Factor with another value found.'))
secondNumber = int(input('Enter your second value to have its Greatest Common Factor with the first value found.'))

remainder = int
while remainder != 0:
    mainResult = firstNumber // secondNumber
    remainder = firstNumber % secondNumber
    firstNumber = secondNumber
    secondNumber = remainder
print (firstNumber,'is the Greatest Common Factor')

#6
decimalValue = int(input('Enter a decimal value to be converted to binary: '))
binaryValue = ""
while decimalValue != 0:
    binaryValue  = str(decimalValue % 2) + binaryValue 
    decimalValue //= 2
print (binaryValue )
