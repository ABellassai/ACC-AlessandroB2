
#1
for i in range (11):
    print(i)

#2
for i in range(10,21,2):
    print(i,end = " ")
    
#3
for i in range (10, 0, -1):
    if (i % 2 == 0):
        print(i)

#4
for i in range (11):
        print(i, 'squared is:', i*i, ', and cubed is:', i*i*i)

#5 and #6
length = int(input('How many rows do you want?'))
for i in range(length + 1):
    for j in range(i):
        print('*',end=' ')
    print()

#7
listNummbers = []
for i in range(5):
    listNummbers.append(int(input('Give me a number: ')))
answer = 1    
for j in listNummbers:
    answer *= j
print(answer)    
        
