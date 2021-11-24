
#1
list1 = []
print(list1) #This is Empty like ME!!!

#2
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list[3] = 3 #stores x with index i
list[5] #retrieves the item with index i
list[-7] #retrieves last i item from list
list[5:9] #retrieves items in the range i to j
list[4:] #retrieves items from i to the end
del list[2] #removes the item with index i
list.append(11) #appends x to the end of the list
list.extend(list1) #appends L to the end of the list
list.insert(13,15) #inserts x at i position
list.remove(6) #removes the first list item whose value is x
list.pop(1) #removes the item at position i and returns its value
print(list.index(10)) #returns the position of the first occurrence of x in a list
list.count(8) #returns the number of times x appears in a list
list.reverse() #reverses list elements
list2 = list.copy(list1) #returns a copy of the list
list.clear() #removes all items from the list
print(list1)

list5 = [3,2,7,9,5]
list5.sort() #sorts items in a list
print(list5) #output [2,3,5,7,9]
list5.sort(reverse = True) # returns a new list with L items sorted 
print(list5) # output [9,7,5,3,2]

choiceMade = int(input())
if choiceMade == 1:
    print('1. Append an element')
    print('Current List = [ a, b, c, d] ')
    userInput = str(input('Enter what you want to add in the list: '))
    aList.append(userInput)
    print('The new list is ',aList)

elif choiceMade == 2:
    print('2. Insert an element')
    print('Current List = [ a, b, c, d] ')
    insert = int(input('Insert an element to replace another element: '))
    sobstitute = int(input('What do you want to sobstitute ? '))
    aList.insert(insert , sobstitute)
    print(aList)


elif choiceMade == 3:
    print('3. Append a list to the given list')
    print('Current List = [ a, b, c, d] ')
    aList.extend(user_list)


elif choiceMade == 4:
    print('1. Append an element')
    print('Current List = [ a, b, c, d] ')
    aList[i] = x


elif choiceMade == 5:
    print('1. Append an element')
    print('Current List = [ a, b, c, d] ')
    del aList[i]


elif choiceMade == 6:
    print('1. Append an element')
    print('Current List = [ a, b, c, d] ')
    aList.pop(i)


elif choiceMade == 7:
    print('1. Append an element')
    print('Current List = [ a, b, c, d] ')
    aList.sort()

elif choiceMade == 8:
    print('1. Append an element')
    print('Current List = [ a, b, c, d] ')
    aList.sort(reverse = True)
    print(aList)

elif choiceMade == 9:
    print('1. Append an element')
    print('Current List = [ a, b, c, d] ')
    print(aList)
