# Write a program to open the files and print each line:
# Range, Frequency, Mean, Median, and Mode values for each file

file1 = open("C:/Users/18ABellassai.ACC/Downloads/10Random.txt", "r")
file2 = open("C:/Users/18ABellassai.ACC/Downloads/100Random.txt", "r")
'''
print(file1.read())
print(file2.read())
'''
#The range tells us how spread out a group of numbers are. To calculate the range we subtract the
#smallest number from the largest

list1 = file1.read()
'''
final_list = []
for item in list1.split():
    final_list.append(int(item))
print(final_list)
final_list.sort()
print(final_list[-1] - final_list[0])
'''
list2 = file2.read()
'''
final_List2 = []
for item2 in list2.split():
    final_List2.append(int(item2))
print(final_List2)
final_List2.sort()
print(final_List2[-1] - final_List2[0])

print('\n')
'''
# The frequency is a count of how often each different number appears
frequency1 = {}
for item in list1:
   if item in frequency1:
      frequency1[item] += 1
   else:
      frequency1[item] = 1
print('List 10 Frequency', frequency1)

'''\/ *www.tutorialspoint.com* \/'''

frequency2 = {}
for item in list2:
   if item in frequency2:
      frequency2[item] += 1
   else:
      frequency2[item] = 1
print('List 100 Frequency', frequency2)

'''^^ *www.tutorialspoint.com* ^^'''

print('\n')

# The mean is the average of all the numbers. To calculate the mean, add all the numbers together and divide this value by the number of numbers
sumOflist1 = sum(list1)
sumOflist2 = sum(list2)

meanlist1 = sumOflist1 / 10
meanlist2 = sumOflist2 / 100
print('Mean of 10: ', meanlist1)
print('Mean of 100: ', meanlist2)

print('\n')

# The mode is the number which appears most often. If two numbers occur with the same frequency, the data is bi-modal, and more than two is multimodal
'''\/ * https://stackabuse.com/ * \/'''
import statistics
modeOFList1 = statistics.mode(list1)
print('Mode of 10: ', modeOFList1)
modeOFList2 = statistics.mode(list2)
print('Mode of 100: ', modeOFList2)
'''^^ * https://stackabuse.com/ * ^^'''

print('\n')

# The median is the number that is in the middle if you were to order all the numbers from largest to smallest.
medianOFList1 = statistics.median(list1)
print('Median of 10: ', medianOFList1)
medianOFList2 = statistics.median(list2)
print('Median of 100 : ', medianOFList2)

'''
Example 1:
1,2,3,4,5,6,7,8,9,10,11 – here 6 is the median because it is in the middle of all the numbers ordered
from largest to smallest
1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11 – here 3 is the median because it is in the middle of all
the numbers ordered from largest to smallest
Example 2:
1,2,3,4,5,6,7,8,9,10 - here 5.5 is the median. If we have an even number of numbers, there is no
single “middle number”, so we add the middle two numbers together and divide them by 2
'''
