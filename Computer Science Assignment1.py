#1
firstNumber = int(input('Number 1:'));
secondNumber = int(input('Number 2:'));
if firstNumber > secondNumber:
    print (firstNumber, ',', secondNumber);
else:
    print(secondNumber, ',', firstNumber);

#2
ageNumber = int(input('Insert your age:'));
if ageNumber >= 18:
    print ('You are elegible for voting');
else:
    print ('You are not elegible for voting');

#3
number1 = int(input('Number 1:'));
if number1 % 2 == 0:
    print (number1, ' is even');
else:
    print (number1, ' is odd');

#4
number2 = int(input('Number 2:'));
if number2 % 7 ==0:
    print (number2, ' is divisible of 7');
else:
    print (number2, ' is not divisible of 7');

#5
number3 = int(input('Number 3:'));
if number3 % 5 ==0:
    print ('Hello');
else:
    print ('Bye');

#6
electricityBillUnit = int(input('electricity Bill Unit: '));
if electricityBillUnit <= 100:
    print ('It is free');
if 100 < electricityBillUnit <= 200:
    hundredUnit = (electricityBillUnit - 100) * 0.05;
    print ('You have to pay ', hundredUnit, '$');
if electricityBillUnit > 200:
    hundredUnit = 100 * 0.05;
    twoHundredUnit = (electricityBillUnit - 200) * 0.10;
    totalUnit = hundredUnit + twoHundredUnit;
    print ('You have to pay ', totalUnit, '$');

#7
number4 = int(input('Number 4:'));
last_digit = number4 % 10;
print (last_digit);

#8
number5 = int(input('Number 5:'));
last_digit2 = number5 % 10;
if last_digit2 % 3 == 0:
    print (last_digit2, 'is divisible by 3');
else:
    print (last_digit2, 'is not divisible by 3');

#9
number6 = int(input('Number 6:'));
if number6 == 1:
    print ('Monday');
if number6 == 2:
    print ('Tuesday');
if number6 == 3:
    print ('Wednesday');
if number6 == 4:
    print ('Thursday');
if number6 == 5:
    print ('Friday');
if number6 == 6:
    print ('Saturday');
if number6 == 7:
    print ('Sunday');      

#10
cTemperature = float(input('Temperature in ºC: '));
fTemperature = 9 / 5 * cTemperature + 32;
fTemperature = round(fTemperature, 2);
print (fTemperature, 'ºF');

#11
day = int(input('Day: '));
month = int(input('Month: '));
year = int(input('Year: '));

date = (day+((13*(month+1))/5)+year+(year/4)-(year/100)+(year/400)) % 7;
print (date);
