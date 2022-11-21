# Name and School: Alessandro Bellassai
# (a)

import random

check = input('If you have finished entering peoples details type "END", otherwise press "RETURN": ')
while check != 'END':
    s_name=input("Enter your surname: ") 
    f_name=input("Enter your first name: ")
    age = int(input('Enter your age: '))
    eircode = []
    eirc = input('Enter your Eircode: ')
    for i in eirc:
        eircode.append(i)
    print("Hello", f_name, s_name, ',you are', age, 'years old and your aircode is', eirc)
    if age >= 12 and age <= 49:
        print(f_name,'you will receive the MRNA vaccine')
    elif age > 49:
        print(f_name,'you will receive the ADENO vaccine')
    value = eircode[-1]
    if value.isdigit() == True:
        if int(value) % 2 == 0:
             print('You must attend Eastwood for your vaccine')
        else:
             print('You must attend Northfield for your vaccine')
    l = ['A', 'B', 'C']
    choice = random.choice(l)
    print('You are now enrolled in the trial to receive Super vaccine', choice)
    check = input('If you have finished entering peoples details type "END", otherwise press "RETURN": ')

# (b)
List1 = [4, 5, 9, 8, 10, 17, 99, 77]
sum1 = 0
counter = 0
elements = range(len.List1[])
for i in List1:
    counter +1
    sum1 = + i
mean = sum1 / elements
print(mean)
