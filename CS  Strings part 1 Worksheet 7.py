
import time
string = 'Hello There Bob'

# Use the len method to print the length of the string
lengthOfString = len(string)
print (lengthOfString)
time.sleep(1)
# Print the first character of the string
print (string[0])
time.sleep(1)
# Print the fifth character of the string
print (string[4])
time.sleep(1)
# Print the last character of the string
print (string[14])
time.sleep(1)
# Run the following three loops and notice the difference in output:
for ch in string:
 print(ch)

time.sleep(1)

for ch in range(0,len(string)):
 print(string[ch])

time.sleep(1)

for ch in range(0,len(string)):
 print(ch)

time.sleep(2)

print(string.upper())   #returns uppercase string
print(string.lower())   #returns lowercase string
print(string.count(b))  #counts how many times b appears
print(string.find(b))   #position of the first occurrence of b
print(string.replace(b,l)) #replaces b with l
print(string.islower()) #returns True if all characters are lowercase
print(string.isupper()) #returns True if all characters are uppercase
print(string.isalnum()) #returns True if all characters are alphanumeric
print(string.isalpha()) #returns True if all characters are alphabetic
print(string.isdigit()) #returns True if all characters are digits
print(string.strip(b))  #returns a string with leading and trailing characters removed

Write a program to check if a string is a palindrome or not. (A string is called palindrome if it
reads same backwards as forward. For example, Noon is a palindrome.)


string1 = input('Give me a word and I will check if it is palindrome: ')
checkString = string1.lower()
for i in range (len(checkString))
