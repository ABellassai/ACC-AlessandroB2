#1
myList = [1,2,3,4,5,6,7]

def myListsum(aList):
    if len(aList) == 1:
        return aList[0]
    else:
        return aList[0] + myListsum(aList[1:])

print(myListsum(myList))

#2
def sum1(a):
    if a < 10:
        return a
    else:
        return a % 10 + sum1(a//10)
n = 1234567

print(sum1(n))
