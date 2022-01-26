#Insertion Sort

#1 Initialise an unsorted list
theList = [5, 7, 3, 6, 2]
#2 Initialise a marker
marker = 1
#3 Traverse through all the list items
while (marker < len(theList)):
    # 4, Insert the selected item into its correct position
    x = marker
    while (theList[x] < theList[x - 1] and x > 0):
           tmp = theList[x]
           theList[x] = theList[x - 1]
           theList[x - 1] = tmp
           x = x - 1
    # 6, Advance the marker to th right by 1 position
    marker = marker + 1
print('Sorted list is: ', theList)