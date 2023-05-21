
# ------------------------BUILT IN FUNCTIONS------------------------

# Use the sep argument in print(x, sep='y') to print "Hello --- how are you?"
x = 'Hello'
y = 'how are you?'
print(x, y, sep=' --- ')
# Use int to convert an age input into an int number
age = '18'
print(int(age))
# Use len(x) to find the length of the string and list below
myStr = "Hello"
myList = ["Apple","Orange"]
print(len(myStr))
print(len(myList))
#Use min() to print the minimum value in the list below
myList = [1,2,3,4,5,6,0,7,8,9,10]
print(min(myList))
#Use max() to print the maximum value in the list below
myList = [1,2,3,4,5,6,0,7,8,9,10]
print(max(myList))
#Use sum() to print the sum of the values in the list below
myList = [1,2,3,4,5,6,0,7,8,9,10]
print(sum(myList))
#Use range(n1,n2,n) returns a sequence of numbers from 3 to 20 in steps of 2
for i in range(3,20,2):
    print(i)
#Use abs() to return the absolute value of num
num = -100.20
print(abs(num))
#Use round() to round num to 2 decimal places
num = 20.5245
print(round(num,2))
#Use type() to print the type of each of the following
myStr = "Hello"
decimal = 10.20
myList = [1,2,3,4,5]
print(type(myStr))
print(type(decimal))
print(type(myList))
#Use str(x) to convert PI to a string
pi = 3.14
print(str(pi))
#Use list() to create a list from the string 'abcd'
print(list('abcd'))
n = 75
num = str(n)
print(list(num))
#Use int to converts my_str to an integer
my_str = 20
print(int(my_str))
#Use float to convert wholeNum to a float
wholeNum = 100
print(float(wholeNum))
#Use bool() to convert a number to a Boolean value
h = -1
print(bool(h))
#Use pow() to return 2 to the power of 4
print(pow(2, 2))
#Use chr() to return the string value of the unicode code point 65
print(chr(65))
#Use ord() to return the Unicode code of a single-character string - A
print(ord('A'))


# ------------------------STRINGS------------------------

#Create a string with the words Hello World
string = 'Hello World'
#Print the string
print(string)
# Use string.upper() to convert the string to uppercase
newStr = string.upper()
#print the string and the upper case string
print(newStr)
# Use string.lower() to convert the string to lowercase
newStr = string.lower()
#print the string and the lower case string
print(newStr)
# Use string.count() to count how many times the letter 'o' appers in the string
print(string.count('o'))
# Use string.find() to get the index of the first occurrence of 'o'. Print this index
print(string.find('o'))
# use string.replace(x,y) to replay 'o' with 'a'. Print the new string
print(string.replace('o','a'))
#use string.islower() to test all characters are lowercase
print(string.islower())
#use string.isupper() to test all characters are uppercase
print(string.isupper())
#use string.isalnum() to test if all characters are alphanumeric
print(string.isalnum())
#use string.isalpha() to test if all characters are alphabetic
print(string.isalpha())
#use string.isdigit() to test if all characters are digits
print(string.isdigit())
#use string.index(s) to return the index of the substring 'll'
print(string.index('ll'))
# string.strip(x) to remove the leading and trailing characters
string = "                         Hello world                             "
print(string.strip(' '))

#          -----------PART 2 STRINGS-----------
#initial string to process
string = 'Alessandro'
# Use string[i] to return the first character
# 1st letter
print(string[0])
# Use string[i] to return the character at position 4
# 4th letter
print(string[3])
#Use string[i] to return the last character 
print(string[-1])
# Use string[i:j] to return the subtring Ale
print(string[0:3])
#Use list = [] to create a list with "Apple", "Orange", "Cherry","Tomato"
l = ["Apple", "Orange", "Cherry","Tomato"]
#Use list[i] = x to replace the 3rd item in the list with the value "Grape"
l[2] = 'Grape'
#Use list[i] to return the first item in the list
print(l[0])
# list[i] to return the last item in the list
print(l[-1])
#Use list[i:j] to return a sublist of the first middle two items
print(l[1:3])
# list[i:] to print all the items in the list starting from Grape
print(l[2])
#Use del list[i] to remove the 3rd item in the list
del l[2]
print(l)

# ------------------------LOOPS------------------------

#Use a while loop to print the values from 1 to 5 
x = 1
while x < 6:
    print(x)
    x = x + 1
#use a for <variable> in <list> loop to print the fruits in the list below:
fruits = ["apple", "banana", "cherry"]
for element in fruits:
    print(element)
# Use a for <variable> in range(start,stop,step) loop to print
#all the values from 2 to 30 in steps of 3
for i in range(2,30,3):
    print(i)
    

# ------------------------LOOP CONTROL------------------------

# Write a loop to print the fruits in the list below.
# Use break to finishe loop execution on banana
print("Exit the loop when we get a \"banana\": ")

fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)
    if i == 'banana':
        break
# Use a loop to print the fruits in the list below.
# Use a continue to skip banana
print("\nDo not print banana: ")

fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == 'banana':
        continue
    print(i)
# Use a pass so that the loop below does nothing
print("\nif you for some reason have a for loop with no content, put in the pass statement \nto avoid getting an error.")
for x in [0, 1, 2]:
    pass
    

# ------------------------LISTS------------------------

#Start here and do what is requested in the comments
#Create a list that contains the following:
L = ["Apple", "Tomato", "Orange", "Cherry","Tomato"]
#print the list
print(L)
#use list.append() to append "Grape" to the end of the list
L.append('Grape')
#print the list
print(L)
#create a new list with "Blueberry" and "Blackberry"
newList = ['Blueberry', 'Blackberry']
#print the list
print(newList)
#use list.extend() to append the new list to the old list
L.extend(newList)
#print the updated list
print(L)
#use list.insert() to insert "Apple" at position 3
L.insert(3, 'Apple')
#print the list
print(L)
#use list.remove() to remove the first item whose value is "Apple"
L.remove('Apple')
#print the list
print(L)
#use list.pop() to remove the item at position 2 from the list and
#return its value. Store its value in a variable
item = L.pop(2)
#print the variable and the list
print(item)
#use list.index() to return the position of the first occurrence
#of "Cherry" in the list. Store the position in a variable
cherry = L.index('Cherry')
#print the variable and the list
print(cherry)
#use list.count() to count the number of times "Cherry"
#appears in the list and store it in a variable
count = L.count('Cherry')
#print the number of cherries and the list
print(count)
#use list.sort() to sort the items in the list
L.sort()
#print the list
print(L)
#use sorted() to return a new list with the items  sorted.
#store the new list in a variable
newList = sorted(newList)
#print the list and the new list
print(L)
print(newList)
#use list.reverse() to reverse the list elements
L.reverse()
#print the list
print(L)
#use list.copy() to store a copy of the list in a new variable
copy = L.copy()
#print the list and the new copy
print(L)
print(copy)
#use list.clear() to remove all the items in the list
L.clear()
#print the list
print(L)


# ------------------------ESCAPE CHAR------------------------

#Use tab to tab space words on the screen
words= 'Hello guys'
print('\t'+words)
#Use the newline \n to create a new line in a print statement
print('\n'+ 'more words')
#Use a comment escape \' to quote some text in a print statement
print('Don\'t touch me!')
#Use a comment escape \" to quote some text in a print statement
print("Don\"t you dare touch me!")


# ------------------------CONDITIONAL------------------------

# if <condition> :
#     <code>
# elif <condition> :
#     <code>
# ...
# else:
#     <code>

#Use an if elif conditional check to find the greater, if either of a and b
a = 200
b = 33
if a < b:
    print('A is small :)')
elif a > b:
    print('A is BIG :D')
#Use an if elif conditional check and boolean operators to find
#the largest, if any, of num1, num2, and num3
num1 = 10
num2 = 14
num3 = 12
if num1 > num2 and num1 > num3:
    print(num1, 'is greater')
elif num2 > num1 and num2 > num3:
    print(num2, 'is greater')
elif num3 > num2 and num3 > num1:
    print(num3, 'is greater')
#Use an if <value> in <list> conditional check to append a new
#list to the list each item that contains the letter 'a'
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []
for i in fruits:
    if i.count('a') > 0:
        newList.append(i)
print(newList)
