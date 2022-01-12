#Bubble List - V1
A = [20, 50, 70, 10, 40]
print('Initial list: ', A)

for k in range(len(A)): #5
    for y in range(len(A) - 1): #4
        if A[y] > A[y + 1]:
            temp = A[y]
            A[y] = A[y + 1]
            A[y + 1] = temp   
print('Sorted list: ', A)

#Bubble List - V2
B = [2, 5, 7, 10, 4]
print('Initial list: ', B)

exchange = True
i = 0
while (i < len(B)) and (exchange == True):
    exchange = False
    for b in range(len(B) - 1):
        if B[b] > B[b + 1]:
            temp = B[b + 1]
            B[b + 1] = B[b]
            B[b] = temp
            exchange = True
    i = i + 1
print('Sorted list: ', B)
