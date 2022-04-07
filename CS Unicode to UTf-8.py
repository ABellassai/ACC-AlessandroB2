#Program 1
# Write a python program to encode a Unicode code point value as UTF-8
o = chr(int('1010000', 2))
print (o)

value = 0
if value == 10:
    value == A
elif value == 11:
    value == B
elif value == 12:
    value == C
elif value == 13:
    value == D
elif value == 14:
    value == E
elif value == 15:
    value == F


value = 0
if value =='A':
    value == 10
elif value == 'B':
    value == 11
elif value == 'C':
    value == 12
elif value == 'D':
    value == 13
elif value == 'E':
    value == 14
elif value == 'F':
    value == 15


s = 'U+0x41'
#if s contains 'U+' or '0x' or 'U+0x':
    
uniVariable = input('Give me and hexodecimal value: U+0x')
listHexodecimal = []
for i in uniVariable:
    if i == '0':
        listHexodecimal.append('0000')
    if i == '1':
        listHexodecimal.append('0001')
    if i == '2':
        listHexodecimal.append('0010')
    if i == '3':
        listHexodecimal.append('0011')
    if i == '4':
        listHexodecimal.append('0100')
    if i == '5':
        listHexodecimal.append('0101')
    if i == '6':
        listHexodecimal.append('0110')
    if i == '7':
        listHexodecimal.append('0111')
    if i == '8':
        listHexodecimal.append('1000')
    if i == '9':
        listHexodecimal.append('1001')
    if i == 'A':
        listHexodecimal.append('1010')
    if i == 'B':
        listHexodecimal.append('1011')
    if i == 'C':
        listHexodecimal.append('1100')
    if i == 'D':
        listHexodecimal.append('1101')
    if i == 'E':
        listHexodecimal.append('1110')
    if i == 'F':
        listHexodecimal.append('1111')
print(listHexodecimal)


['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
listBinary = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
   
    
#Program 2
# Write a second program which decodes UTF-8 values to their Unicode code point and print
# the character at that code point
c = ord('P')
print (c)


binaryValues = input('Give me any binary value: ').split(' ')
listBinary = []
for j in binaryValues:
    if j == '0000':
        listBinary.append(0)
    if j == '0001':
        listBinary.append(1)
    if j == '0010':
        listBinary.append(2)
    if j == '0011':
        listBinary.append(3)
    if j == '0100':
        listBinary.append(4)
    if j == '0101':
        listBinary.append(5)
    if j == '0110':
        listBinary.append(6)
    if j == '0111':
        listBinary.append(7)
    if j == '1000':
        listBinary.append(8)
    if j == '1001':
        listBinary.append(9)
    if j == '1010':
        listBinary.append('A')
    if j == '1011':
        listBinary.append('B')
    if j == '1100':
        listBinary.append('C')
    if j == '1101':
        listBinary.append('D')
    if j == '1110':
        listBinary.append('E')
    if j == '1111':
        listBinary.append('F')
print(listBinary)

