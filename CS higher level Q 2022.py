# Question 16(a)
# Name and School: Alessandro Bellassai

f = open('C:/home//alex//Scaricati//2022 L.89 Higher Level Seed files for Section C//shelley.txt', 'r')
list1 = f.readlines()
if type(list1) == list and len(list1) > 0:
    print('The poem has been read correctly by the program')
f.close()

wordF = str(input('Please enter a word to search for: '))

print('The last line of the poem is: "',list1[-1],'"')

counterSpace = list1.count('\n')
for u in range(counterSpace):
    list1.remove('\n')

countL = len(list1)
countW = 0
countC = 0
for line in list1:
    i = line.split()
    countW = countW + len(i)
    countC = countC + len(line)
    if wordF.isalpha() == True and :
        place = i.index(wordF)
print('The word', wordF, 'was found in line')

print('There are',countL,'lines,',countW,'words and',countC,'characters')
