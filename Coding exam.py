#Coding Exam
L =[23,1,0,-12,48, 15, 9, 20, -11, 42,7, -5, 13]

# Program 1: Write a program to print the sum of every second number in thelistL
addition = sum(L[1:2]+L[3:4]+L[5:6]+L[7:8]+L[9:10]+L[11:12]+L[13:0])
print(addition)

# Program 2: Write a program to print the product of all the numbers in thelistL
def myListsum(aList):
    if len(aList) == 1:
        return aList[0]
    else:
        return aList[0] * myListsum(aList[1:])
print(myListsum(L))

# Program 3: Write a program to print every number between 0 and 10000 inclusive
for i in range (0, 10001):
    print(i)
    
# Program 4: Write a program to print all the characters in the string ‘Code Happy’ on a separate line
string= 'CodeHappy'
for i in string:
    print(i, sep='\n')

# Program 5: Write a program to take in the length and width of a rectangle and print its area
a = float(input('Give me the width of a rectangle:'))
b = float(input('Give me the length of a rectangle:'))
if a <= 0 or b <=0:
    print('Give me positive measurements')
else:
    print(a*b)

# Program 6: Write a program that repeatedly asks the user to enter some text
# and only stops if the user enters the character ‘z’ or ‘Z’
sentence = ''
while sentence != 'z':
    sentence = input('write what you like: ').lower()

# Program 7: Write a program to open a file called ‘CS04022022.txt’
# and print the poem below to the file before closing it–the lines should be as below, not in one long line in the file
f = open('CS04022022.txt', 'w')
f.write('Leunig – How To Get There')
f.write('\n')
f.write('\n')
f.write('Go to the end of the path until you get to the gate.')
f.write('\n')
f.write('Go through the gate and head straight out towards the horizon.')
f.write('\n')
f.write('Keep going towards the horizon.')
f.write('\n')
f.write('Sit down and have a rest every now and again,')
f.write('\n')
f.write('But keep on going, just keep on with it.')
f.write('\n')
f.write('Keep on going as far as you can.')
f.write('\n')
f.write('That is how you get there.')
f.close() 
