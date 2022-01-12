#Bubble List - V1
L = [20, 50, 70, 10, 40]
print('Initial list: ', L)

for k in range(len(L)): #5
    for y in range(len(L) - 1): #4
        if L[y] > L[y + 1]:
            temp = L[y]
            L[y] = L[y + 1]
            L[y + 1] = temp
            
print('Sorted list: ', L)

#Bubble List - V2
Z = [2, 5, 7, 10, 4]
print('Initial list: ', Z)

exchange = True
i = 0

while (i < len(Z)) and (exchange == True):
    exchange = False
    for c in range(len(Z) - 1):
        if Z[c] > Z[c + 1]:
            temp = Z[c + 1]
            Z[c + 1] = Z[c]
            Z[c] = temp
            exchange = True
    i = i + 1

print('Sorted list: ', Z)
