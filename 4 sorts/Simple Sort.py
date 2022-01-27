# Simple (Selection) Sort
# 1. Initialise an unsorted list
aList = [9, 6, 10, 4, 8, 5, 7]

# 2. Initialise a marker
marker = 0

# 3. Traverse through all list items
while marker < len(aList):

    # 4. Find the minimum item to the right of the marker
    index_of_min = marker
    for j in range(marker+1, len(aList)):
        if aList[index_of_min] > aList[j]:
            index_of_min = j
            
    # 5. Exchange the smallest item with the item at the marker
    temp = aList[marker] # save the item at the marker
    aList[marker] = aList[index_of_min] # copy 1
    aList[index_of_min] = temp # copy 2
    
    # 6. Advance the marker to the right by 1 position
    marker = marker+1
# 7. Stop
print(aList)


import sys allows us to access the systems library 
#sys.argv [] is a list that contains the command line arguments 
#sys.argv [0) will return the name of the program- this is alays the first argument
#sys.argv [1] will return the first argument after the proran name 
#sys.argv [2] will return the second argument after the program name and so on for sys.argv [3] ... 
          
#since sys.argv is a list we can iterate through it ir we wish 
print ("This is the name of the program:", sys.argv [0]) 
print ("Number of elements including the name of the program:", len (sys.argv)) 
print ("Number of elements excluding the name of the program: ", (len (sys.argv) -1)) 
print ("Argument List: ", str (sys.argv))
