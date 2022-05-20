#Program 2
f = open('RandomMusings.txt', 'r')
p = f.read()

#Words
word = 0
words = p.split()
for k in words:
    word =+ 1
    print('Words:', words)

#Lines
lines = len(p.split('\n'))
print('Lines:', lines)

#Consonants
consonants = 0

#Letters
letters = 0

for k in p:
    if k == ' ':
        letters += 1
print('Letters:', letters)

with open('RandomValues.txt', 'w') as Answers:
    Answers.write('No. of Words = ')
    Answers.write(str(words))
    Answers.write('\n')
    Answers.write('No. of lines = ')
    Answers.write(str(lines))
    Answers.write('\n')
    Answers.write('No. of consonants = ')
    Answers.write(str(consonants))
    Answers.write('\n')
    Answers.write('Average No. of letters  = ')
    Answers.write(str(letters))
    
Answers.close()