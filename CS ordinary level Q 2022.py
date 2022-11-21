# Question 16(a)
# Name and School: Alessandro

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
    print(value)
#     if value.isdigit() == True:
#         if value % 2 == 0:
#             print('You must attend Eastwood for your vaccine')
#         else:
#             print('You must attend Northfield for your vaccine')
    l = ['A', 'B', 'C']
    if import.random(0, 2) = 0
        print('You are now enrolled in the trial to receive Super vaccine A')
    elif:
        print('You are now enrolled in the trial to receive Super vaccine B')
    else:
        print('You are now enrolled in the trial to receive Super vaccine C')

    check = input('If you have finished entering peoples details type "END", otherwise press "RETURN": ')
