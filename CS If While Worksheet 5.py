#Number Game      Q1
import math
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
    print('The number the computer picked was',randomChoice)

    
#Credit Card Program     Q2
cardNum = ""
while type(cardNum) == str or len(str(cardNum)) > 16 or len(str(cardNum)) <= 13:
    try:
        cardNum = int(input("Please enter a valid credit card number. This number must be between 13 and 16 digits and contain no letters or decimals."))
    except ValueError:
        pass
cardNum = str(cardNum)
if cardNum[:1] == "4":
    print("This is a Visa card.")
elif cardNum[:1] == "5":
    print("This is a Master card")
elif cardNum[:2] == "37":
    print("This is an American Express card.")
elif cardNum[:1] == "6":
    print("This is a Discover card.")
else:
    print("This not a valid number.")
    exit()
    
counter = len(cardNum)-2
evens = 0
while counter >= 0:
    evenNo = int(cardNum[counter])*2
    if len(str(evenNo)) > 1:
        evenNo = int(str(evenNo)[0]) + int(str(evenNo)[1])
    evens += evenNo
    counter -=2

counter = len(cardNum)-1
odds = 0
while counter >= 0:
    odds += int(cardNum[counter])
    counter -=2
    

if (evens + odds) % 10 == 0:
    print("This card is valid.")
else:
    print("This card is not valid.")


