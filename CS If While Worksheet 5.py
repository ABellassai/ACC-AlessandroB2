#Number Game
import random
integerA = int(input('Enter a number: '))
integerB = int(input('Enter another number: '))
while (integerA == integerB):
    print('The two integers cannot be equal!')
    integerA = int(input('Enter a low number: '))
    integerB = int(input('Enter a higher number: '))
if (integerA < integerB):
     randomChoice = random.randint (integerA, integerB)
else:
     randomChoice = random.randint (integerB, integerA)

print(randomChoice)




#Credit Card Program
