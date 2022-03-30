import math

# Program 1
num1 = float(input('Give me a decimal number: '))
num2 = float(input('Give me another decimal number: '))

average = (num1 + num2)/2
print(average)

firstDivision = num1 / num2
secondDivision = num2 / num1
print(firstDivision)
print(secondDivision)

power = num1 ** num2
print(power)


# Program 2
def Volume():
    height = float(input('Give me the height of your cylinder: '))
    radious = float(input('Give me the radious of your cylinder: '))
    volumeOfCylinder = math.pi * (radious**2) * height
    return volumeOfCylinder
print(Volume())


# Program 3
string1 = str(input('Give me a string: '))
string2 = str(input('Give me another string: '))
def str_comp(string1, string2):
    if string1 == string2:
        return ('The 2 strings are the same')
    else:
        return('The 2 strings are NOT the same')
print(str_comp(string1, string2))


# Program 4
number = float(input('Give me a number: '))
counter = 0
while counter < number:
    counter = counter + 1
    if counter % 2 == 1:
        print(counter)


# Program 5
f=open('Readme.txt', 'r')
read = f.readline()
vowelCounter = 0
while read != '':
    for vowel in read:
        if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' or vowel == 'A' or vowel == 'E' or vowel == 'I' or vowel == 'O' or vowel == 'U':
            vowelCounter = vowelCounter + 1 
    print(vowelCounter)
    read = f.readline()
f.close()


# Program 6
n = int(input('Give me a limit number: '))
def function(n):
    if n == 1:
        return n
    else:
        return n + function(n-1)
print(function(n))
        
    



