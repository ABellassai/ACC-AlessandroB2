
#1
number = 0
total = 0
while number < 10:
    total += int(input("Enter Numbers: "))
    number+=1
average = total / number
print("Average of numbers is " + str(average) + "!")

#2
moltiplication = 24
factor = 1
while factor <= 12:
    print(moltiplication, "x", factor, "=", moltiplication * factor)
    factor += 1

#3
while True:
    print('Infinite LOOOOOOOP')

#4
num=""
while type(num)!= int:
    try:
        num = int(input("Enter a number to find its factorial."))
    except ValueError:
        print("This isnt an integer. Please try again.")
        pass

multiplyBy = 1
total = 1
while multiplyBy <= num:
    total = total * multiplyBy
    multiplyBy += 1
    
print(total,"is the factorial of",num)

#5
firstNum = int(input("Enter your first number to have its Greatest Common Factor with another value found."))
secondNum = int(input("Enter your second value to have its Greatest Common Factor with the first value found."))

remainder = int
while remainder != 0:
    mainResult = firstNum // secondNum
    remainder = firstNum % secondNum
    firstNum = secondNum
    secondNum = remainder
print(firstNum,"is the GCF.")

#6
decimalValue = int(input("Please enter a decimal value to be converted to binary."))
binaryAnswer = ""
while decimalValue != 0:
    binaryAnswer = str(decimalValue % 2) + binaryAnswer
    decimalValue //= 2
print("Binary:",binaryAnswer)

