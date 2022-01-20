#Program 1
myList = [5, 7, 3, 6, 2, 4, 1]

#Bubble Sort Function
def bubbleSort(L, descending = False, dbg = True):
   # print("INPUT (initial list): ", L)
    exchange = True
    n = len(L)
    i = 0
    while (i< n) and  exchange:
       # print("BEFORE PASS %d: %s " %(i+1, L))
        exchange = False
        for j in range(n-i-1):
            #print("%s " %L, end="-> ")
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j] 
                exchange = True 
            #print("%s " %L)
            
        #print("AFTER PASS %d: %s " %(i+1, L))
        i= i+1
    return(L) #("OUTPUT (sorted list): ", L)
result = bubbleSort(myList)
print(result)

#Insertion Sort Function
def insertionSort(L):
    marker = 1     
    while (marker < len(L)):
        x= marker
        while (L[x] < L[x - 1] and x > 0):
               tmp = L[x]
               L[x] = L[x - 1]
               L[x - 1] = tmp
               x = x - 1
        marker = marker + 1
    return(L)
result = insertionSort(myList)
print(result)

#Program 2
myList2 = [9, 2, 3, 1, 5, 6, 7, 3, 4, 5]
sortSelection = int(input('Type 1 for Bubblem sort or 2 for Insertion sort: '))

if sortSelection == 1:
    result = bubbleSort(myList2)
    print(result)

elif sortSelection == 2:
    result = insertionSort(myList2)
    print(result)
    
elif sortSelection != 1 or 2:
    print('Give either 1 or 2')
