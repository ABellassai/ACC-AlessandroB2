L = [5, 7, 3, 6, 2, 4, 1]

# Bubble Sort Function
def bubbleSort(L, descending = False, dbg = True):
    exchange = True
    n = len(L)
    i = 0
    if dbg:
        file1 = open('log.txt', 'w')
    while (i < n) and  exchange:
        exchange = False
        for j in range(n-i-1): 
            if descending == False:
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j] 
                    exchange = True      
            if descending == True:
                if L[j] < L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j] 
                    exchange = True    
            
        if dbg == True:
            file1.write('Debug Info' + "\n")
            file1.write("BEFORE PASS" + str(i+1) + str(L)+ "\n")
            file1.write(str(L) + "-> "+ "\n")
            file1.write(str(L)+ "\n")
            file1.write("AFTER PASS" + str(i+1) + str(L)+ "\n")
        elif dbg == False:
            ('')
            
        i= i+1
    file1.close()
    return None

# Insertion Sort Function
def insertionSort(L, descending = False):
    marker = 1     
    while (marker < len(L)):
        x= marker
        while (L[x] < L[x - 1] and x > 0):
               tmp = L[x]
               L[x] = L[x - 1]
               L[x - 1] = tmp
               x = x - 1
        marker = marker + 1
        exchange = True      
        if descending == True:
            if L[j] < L[j+1]:
                L[j], L[j+1] = L[j+1], L[j] 
                exchange = True
    return None

# Simple Sort Function
def simpleSort(L, descending = False):
    marker = 0
    while marker < len(L):
        index_of_min = marker
        for j in range(marker+1, len(L)):
            if descending == False:
                if L[index_of_min] > L[j]:
                    index_of_min = j
            temp = L[marker]
            L[marker] = L[index_of_min] 
            L[index_of_min] = temp 
            marker = marker+1
            exchange = True      
            if descending == True:
                if L[index_of_min] < L[j]:
                    L[j], L[j+1] = L[j+1], L[j] 
                    exchange = True
    return None
