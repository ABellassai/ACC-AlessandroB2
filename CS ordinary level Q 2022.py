# Question 16(a)
# Name and School: Alessandro

s_name=input("Enter your surname: ") 
f_name=input("Enter your first name: ")
age = int(input('Enter your age: '))
eircode = []
eirc = input('Enter your Eircode: ')
for i in eirc:
    eircode = eircode.append(i)
print("Hello", f_name, s_name, 'You are', age, 'years old')
if age >= 12 and age <= 49:
    print(f_name,'you will receive the MRNA vaccine')
elif age > 49:
    print(f_name,'you will receive the ADENO vaccine')
print('Your Earcode is', eirc)
if eircode[-1] % 2 == 0:
    print('You must attend Eastwood for your vaccine')
else:
    print('You must attend Northfield for your vaccine')