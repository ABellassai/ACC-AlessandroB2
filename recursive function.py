
n = int(input('Enter a number: '))

# 1. 
def addOddNumber(n):
    if n == 0:
        return 0
    else:
        return ((2*n -1) + addOddNumber(n-1))

# 2
def reciprocal(n):
    if n == 0:
        return 0
    else:
        return ((1/n) + reciprocal(n-1))

# 3
def pieSum(n):
    if n == 0:
        return 0
    else:
        return (4/(2*n -1)*(-1**n) + pieSum(n-1))






print(addOddNumber(n))
print(reciprocal(n))
print(pieSum(n))
print(addOddNumber(n))
