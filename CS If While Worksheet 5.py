#Number Game
import random
integerA = int(input('Enter a number: '))
integerB = int(input('Enter another number: '))
while (integerA == integerB):
    print('The two integers cannot be equal!')
    integerA = int(input('Enter a lower number: '))
    integerB = int(input('Enter a higher number: '))
if (integerA < integerB):
     randomChoice = random.randint (integerA, integerB)
else:
     randomChoice = random.randint (integerB, integerA)

minNumberGuesses = (round(math.log(integerB-integerA+1,2)))
#The -1 accounts for the first guess.
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

#Credit Card Program
