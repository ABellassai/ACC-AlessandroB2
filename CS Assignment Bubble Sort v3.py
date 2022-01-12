# Bubble Sort v3
# 1. Initialise an unsortedlist
L = [5, 7, 3, 6, 2, 4, 1]
print("INPUT (initial list): ", L)
exchange = True
n = len(L)
i = 0
# 2. Traverse across every element as long as there are exchangeswhile (i< n) and  exchange:
while (i< n) and  exchange:
    print("BEFORE PASS %d: %s " %(i+1, L))
    exchange = False

# 3. Compare all unsorted adjacent elements
    for j in range(n-i-1):
    
# 4. if the elements are out of order, then swap them
        print("%s " %L, end="-> ")
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j] # Canonical swap!
            exchange = True # we've done an exchange!

        print("%s " %L)
        
    print("AFTER PASS %d: %s " %(i+1, L))
    i= i+1 # increment the loop counter
print("OUTPUT (sorted list): ", L)

'''As an exercise you might consider modifying the code so that it computes the following:
1 the number comparisons on each pass
2 the total number of exchanges on each pass
3 the total number of comparisons
4 the total number of exchanges'''

