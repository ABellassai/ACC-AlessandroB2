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

#4 and #5
string = input('Type a string: ')
for ch in string:
    if (ch == 'a' or ch== 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        newString = string.lower()
        print(newString)
       vowels += 1
       counter +=1
       print('There are' len(string)-vowels,'consonants')
#6

