#Number Game
import random
integerA = int(input('Enter a low number: '))
integerB = int(input('Enter a higher number: '))
while (integerA == integerB):
    print('The two integers cannot be equal!')
    integerA = int(input('Enter a low number: '))
    integerB = int(input('Enter a higher number: '))
        while (integerA == integerB):
    randomChoice = random.randint (integerA, integerB)
    randomChoice = random.randint (integerB, integerA)
else:
    print('The two integers cannot be equal!')
print(randomChoice)




#Credit Card Program