f = open('AlessandroBellassaiChristmasTest2021.txt' ,'w')

#program 1
list1 = [23, 1, 0, -12, 48]
sum1 = 0
for i in list1:
    sum1= sum1+i
f.write(str(sum1)+ '\n')
    
#program 2
list2 = [23, 1, 0, -12, 48]
sum2 = 0
for i in list2:
    if i%2 == 1:
        sum2= sum2+i
f.write(str(sum2)+ '\n')

#program 3
list3 = [23, 1, 0, -12, 48]
counter = 0
for i in list3:
    if i%2 == 0:
     counter = counter+1
f.write(str(counter)+ '\n')

#program 4
list4 = [23, 1, 0, -12, 48]
products = 0
for i in list4:
    i * products+1
f.write(str(products)+ '\n')

#program 5
num = 20
interval = 4
for counter in range(interval, num + 1, interval):
    f.write(str(counter) + '\n')

#program 6
string= 'cat'
times = 0
while times < len(string) :
    f.write(string[times]+ '\n')
    times = times + 1

#program 7
num = 5
result = 0
counter = 0
while counter < 5:
    counter = counter+1
    result= result + counter
f.write(str(result)+ '\n')

#program 8
list8 = [1,2,3,2,5]
value = 2
counter = 0
while counter < len(list8):
    if value == list8[counter]:
        f.write('The value ' + str(value) + ' is at list8[' + str(counter) + ']' + '\n')
    counter = counter+1
    
f.close()
