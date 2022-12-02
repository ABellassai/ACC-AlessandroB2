# Question 16(c) 
# Examination Number: Alessandro Bellassai

bmi_values = [24, 19, 33, 35, 27, 18, 15, 33, 35, 23, 32, 23]
counter = 0
obeseNum = 0

for k in range(len(bmi_values)): 
    for y in range(len(bmi_values) - 1):
        if bmi_values[y] < bmi_values[y + 1]:
            temp = bmi_values[y]
            bmi_values[y] = bmi_values[y + 1]
            bmi_values[y + 1] = temp
            
for i in bmi_values:
    if i >= 30:
        obeseNum = obeseNum + 1
    counter = counter +1  

print('Obese:',obeseNum)
print('Largest number:', bmi_values[0])
print('Second largest number:', bmi_values[1])

