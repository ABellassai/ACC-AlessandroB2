#1
num = input("Input a number to recieve the sum of its digits.")
length = int(len(num))
answer = 0
while length > 0:
    answer += int(num[(length-1)])
    length -=1

print(answer)
#2
num = 100
while num <= 500:
    first = num %10
    second = ((num - first)%100)/10
    third = (num - (num%100))/100
    if (first**3) + (second**3) + (third**3) == num:
        print(num)
    num += 1
    
#3
number = input("Enter a number to be reversed.")
answer = ""
lengthCounter = len(number)
while lengthCounter > 0:
    answer += number[-1]
    number = number[0:len(number)-1]
    lengthCounter -=1
    
print(answer)

#4
number = -1
while number < 0:
    try:
        reply = int(input("Please enter a positive number."))
        if reply > 0:
            number = reply
        else:
            print("This number isnt positive.")
    except ValueError:
        print("This isnt a number.")
        pass
        
print(number,"is a positive number.")
