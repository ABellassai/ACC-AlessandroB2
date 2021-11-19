#1
print('''Python
Programming
is
great
fun! :)
Pablo''')

#2
string = input('type whatever you like: ')
sumOfCharacters = 0
for character in string:
    if character.isdigit() == True:
        sumOfCharacters = sumOfCharacters + int(character)
        print (sumOfCharacters)

#3
string = input('Type a string: ')
spaces = string.replace(' ', '-')
print(spaces)

#4
string = input('Type a string: ')
for ch in string:
    if (ch == 'a' or ch== 'e' or ch == 'I' or ch == 'o' or ch == 'u'):
        newString = string.lower()
        print(newString)

#5


#6

