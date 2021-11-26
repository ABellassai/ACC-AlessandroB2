#1
# Write a program to open the files and print each line:
# Range, Frequency, Mean, Median, and Mode values for each file

file1 = open("C:/Users/18ABellassai.ACC/Downloads/10Random.txt", "r")
file2 = open("C:/Users/18ABellassai.ACC/Downloads/100Random.txt", "r")
file1.read(100)
file2.read(10)

#The range tells us how spread out a group of numbers are. To calculate the range we subtract the
#smallest number from the largest.


#The frequency is a count of how often each different number appears


#The mean is the average of all the numbers. To calculate the mean, add all the numbers together
#and divide this value by the number of numbers


#The mode is the number which appears most often. If two numbers occur with the same frequency,
#the data is bi-modal, and more than two is multimodal


Example 1:
1,2,3,4,5,6,7,8,9,10,11 – here 6 is the median because it is in the middle of all the numbers ordered
from largest to smallest
1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11 – here 3 is the median because it is in the middle of all
the numbers ordered from largest to smallest
Example 2:
1,2,3,4,5,6,7,8,9,10 - here 5.5 is the median. If we have an even number of numbers, there is no
single “middle number”, so we add the middle two numbers together and divide them by 2
