#Number Game      Q1
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

    

#Credit Card Program     Q2
cardNumber = ""
while type(cardNumber) == str or len(str(cardNumber)) > 16 or len(str(cardNumber)) <= 13:
    try:
        cardNumber = int(input('Enter a valid credit card number which must be between 13 and 16 digits and cannot contain letters or decimals: '))
    except ValueError:
        pass
cardNumber = str(cardNumber)
if cardNumber[:1] == '4':
    print('This is a Visa card')
elif cardNumber[:1] == '5':
    print('This is a Master card')
elif cardNumber[:2] == '37':
    print('This is an American Express card')
elif cardNumber[:1] == '6':
    print('This is a Discover card')
else:
    print('This is not a valid number')
    exit()
    
counter = len(cardNumber)-2
evens = 0
while counter >= 0:
    evenNo = int(cardNumber[counter])*2
    if len(str(evenNo)) > 1:
        evenNo = int(str(evenNo)[0]) + int(str(evenNo)[1])
    evens += evenNo
    counter -=2

counter = len(cardNumber)-1
odds = 0
while counter >= 0:
    odds += int(cardNumber[counter])
    counter -=2

if (evens + odds) % 10 == 0:
    print("This card is valid.")
else:
    print("This card is not valid.")
    
