# Question 16(a)
# Name and School: Alessandro Bellassai

cardNum=7200828282828210
cardNum = int(input('Welcome to CardCheck. Enter your card number: '))
print(cardNum)
strCardNum = str(cardNum)

expiryDate = int(input('Enter the card expiry date e.g 11/26 should be entered as 1126: '))
expiryDateStr = str(expiryDate)
expiryDateSum = int(expiryDateStr[-4]) + int(expiryDateStr[-3]) + int(expiryDateStr[-2]) + int(expiryDateStr[-1])
digit = int(strCardNum[0:2])
MultipliedNum = expiryDateSum * digit
CVVnumber = MultipliedNum - int(strCardNum[9])

while len(strCardNum) != 16:
    cardNum = int(input('That is incorrect, please try again: '))
    strCardNum = str(cardNum)

if strCardNum[0] == '7':
    print('This is a ZincCard')
elif strCardNum[0] == '8':
    print('This is a WinCard')
print(CVVnumber)
print('Card number',strCardNum[0:4]+'-'+strCardNum[4:8]+'-'+strCardNum[8:12]+'-'+strCardNum[12:16],'and it is valid')
