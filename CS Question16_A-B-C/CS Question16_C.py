# Question 16(c) 
# Examination Number: Alessandro Bellassai

bmi_values = [24, 19, 33, 35, 27, 18, 15, 33, 35, 23, 32, 23]
counter = 0
obeseNum = 0

for i in bmi_values:
    if i >= 30:
        obeseNum = obeseNum + 1
    counter = counter +1  

print('Obese:',obeseNum)
    
def find_nth_largest(n, list_of_values): 
    for k in range(len(list_of_values)): 
        for y in range(len(list_of_values) - 1):
            if list_of_values[y] < list_of_values[y + 1]:
                temp = list_of_values[y]
                list_of_values[y] = list_of_values[y + 1]
                list_of_values[y + 1] = temp
                
    return list_of_values[n]
num = int(input('Enter the nth value you wish to find: '))    
list_of_values = find_nth_largest(num, bmi_values)
print(list_of_values)
