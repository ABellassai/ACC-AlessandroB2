# Question 16(b)
# Examination Number: Alessandro Bellassai
 
# For this question it is useful to understand ... 
# 1. randint(a, b) returns a random integer N such that a<=N<=b. 
# 2. s.append(x) appends the element x to the end of list s.

from random import *
bmi_values = []
heights = [] # an empty list of heights
weights = [] # an empty list of weights
num = int(input('Enter the number of pairs of values you wish to generate: '))
# Loop to build up the lists with random values
for count in range(10):
    # a random integer between 150 and 210
    heights.append(randint(150, 210))
    # a random integer between 50 and 130
    weights.append(randint(50, 130)) 
print('heights:',heights[0:num])
print('weights:',weights[0:num])
# Display the lists
counter = 0
while counter < num:
    values = weights[counter] / (pow(heights[counter],2)) * 10000
    bmi_values.append(round(values, 1))
    counter = counter + 1
print('BMI values: ', bmi_values)

