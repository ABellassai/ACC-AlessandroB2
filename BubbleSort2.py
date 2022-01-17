myList= [5, 7, 3, 6, 2, 4, 1]

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
