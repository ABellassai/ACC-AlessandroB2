#Program 1
f = open('file.txt', 'r')
p = f.readline()
print(p)
numbers = 0
capitals = 0
words = 1
spaces = 0

for i in p:
    if i.isdigit():
        numbers += 1
print('Numbers:', numbers)

for j in p:
    if j.isupper():
        capitals += 1
print('Capital letters:', capitals)

for k in p:
    if k == ' ':
        words += 1
print('Words:', words)

for l in p:
    spaces = p.count(' ')
print('Spaces:', spaces)

with open('answers.txt', 'w') as Answers:
    Answers.write('Capital Letters = ')
    Answers.write(str(capitals))
    Answers.write('\n')
    Answers.write('No. of Numbers = ')
    Answers.write(str(numbers))
    Answers.write('\n')
    Answers.write('No. of Spaces = ')
    Answers.write(str(spaces))
    Answers.write('\n')
    Answers.write('No. of Words = ')
    Answers.write(str(words))
f.close()

#Program 2
f = open('file2.txt', 'r')
d = f.readline()
print(d)

num = 0
total = 0

#Mean
mean = 0
totalNum = 0
total = sum(float(a) for a in d.split(','))
totalNum = d.count(',') + 1
mean = total // totalNum
    
#Median
L = []
for a in d.split(','):
   L.append(float(a)) 
print(L)
L.sort() = newList


median = 0
#Mode



mode = 0

with open('answers2.txt', 'w') as Answers2:
    Answers2.write('Mean = ')
    Answers2.write(str(mean))
    Answers2.write('\n')
    Answers2.write('Median = ')
    Answers2.write(str(median))
    Answers2.write('\n')
    Answers2.write('Mode = ')
    Answers2.write(str(mode))
f.close()
