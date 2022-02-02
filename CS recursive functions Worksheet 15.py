myList = [1,2,3,4,5,6,7]

def myListsum(aList):
    if len(aList) == 1:
        return aList[0]
    else:
        return aList[0] + myListsum(aList[1:])

print(myListsum(myList))

#Write a Python program using recursion to get the sum of the integer 1235467

def sum(a):
    if a < 10:
        return a
    else:
        return a // + sum %()

print(sum())


