
# 1
'''
num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
sum1 = num1 + num2
print(sum1)
difference = num1 - num2
print(difference)
product = num1 * num2
print(product)

# 2
sec = int(input("give me 5 digit number: "))
if sec > 99999 or sec <= 9999:
    print('I said 5 digit number!')
minutes= sec // 60
print(minutes, 'minutes')

# 3
cr1 = str(input('give me 5 characters: '))
cr2 = str(input())
cr3 = str(input())
cr4 = str(input())
cr5 = str(input())

if cr1.isdigit() == True:
    print('I said to type characters!')
if cr2.isdigit() == True:
    print('I said to type characters!')
if cr3.isdigit() == True:
    print('I said to type characters!')
if cr4.isdigit() == True:
    print('I said to type characters!')
if cr5.isdigit() == True:
    print('I said to type characters!')

print(ord(cr1))
print(ord(cr2))
print(ord(cr3))
print(ord(cr4))
print(ord(cr5))

# 4
initialNumber = int(input("Give me a positive number: "))
counter = 1
total = initialNumber
while initialNumber >= 0:
    initialNumber = int(input("Give me another positive number: "))
    counter = counter + 1
    total = total + initialNumber
print(total / counter)
'''
# 5. Write a program to take in 5 numbers and add each one to a list. Then iterate through the
# list using a for loop and add 1 to each number. Print the list at the end to show that each
# number has been increased by 1.
listN = []
n1 = int(input('give me 5 numbers: '))
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
listN.append()
for i in listN:
    

# 6. Write a program to read in the file onTime.txt and split it into a list with a delimiter of space.
# Calculate the frequency of each word, and find the mode (The word/words that
# appears/appear most often).
# Write each word and its frequency to a text file named onTimeAnalysis.txt
# At the end of the file write the mode.
# Use plotly to draw a bar chart of the words in the txt file and their frequency.





