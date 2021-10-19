
#1
number = input('Sum of number digits: ')
length = int(len(number))
answer = 0
while length > 0:
    answer += int(number[(length-1)])
    length -=1
print (answer)

#2
number2 = 100
while number2 <= 500:
    first = number2 %10
    second = ((number2 - first)%100)/10
    third = (number2 - (number2%100))/100
    if (first**3) + (second**3) + (third**3) == number2:
        print(number2)
    number2 += 1
    
#3
number3 = input('Enter a number to be reversed: ')
answer = ""
lengthCounter = len(number3)
while lengthCounter > 0:
    answer += number3[-1]
    number3 = number3[0:len(number3)-1]
    lengthCounter -=1
print(answer)

#4
number4 = -1
while number < 0:
    try:
        reply = int(input('Enter a positive number: '))
        if reply > 0:
            number4 = reply
        else:
            print('This number is not positive!')
    except ValueError:
        print('This isnt a number!')
        pass 
print(number4,'is a positive number')
