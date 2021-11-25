
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

#3
aList = ['a', 'b', 'c', 'd'] 
print(aList)
print("""1. Append an element
2. Insert an element
3. Append a list to the given list
4. Modify an existing element
5. Delete an existing element from its position
6. Delete an existing element with a given value
7. Sort the list in the ascending order
8. Sort the list in descending order
9. Display the list
Please enter an option(1 - 9): """)

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
    sobstitute = input('What do you want to sobstitute ? ')
    aList.insert(insert , sobstitute)
    print(aList)


elif choiceMade == 3:
    print('3. Append a list to the given list')
    print('Current List = [ a, b, c, d] ')
    value1 = str(input('Enter a value: '))
    value2 = str(input('Enter a second value: '))
    value3 = str(input('Enter a third value: '))
    value4 = str(input('Enter one last value: '))
    newList = [value1, value2, value3, value4]
    aList.extend(newList)
    print(aList)


elif choiceMade == 4:
    print('4. Modify an existing element')
    print('Current List = [ a, b, c, d] ')
    modify = int(input('What element would you want to modify? '))
    modifyDone = str(input('What do you want it to become? '))
    aList[modify] = modifyDone
    print(aList)

elif choiceMade == 5:
    print('5. Delete an existing element from its position')
    print('Current List = [ a, b, c, d] ')
    aList.remove("d")
    print('The new list is: ',aList)


elif choiceMade == 6:
    print('6. Delete an existing element with a given value')
    print('Current List = [ a, b, c, d] ')
    deleteElement = int(input('Enter a element to remove: '))
    aList.pop(deleteElement)
    print('The new list is: ', aList)


elif choiceMade == 7:
    print('7. Sort the list in the ascending order')
    print('Current List = [ a, b, c, d] ')
    aList.sort()
    print(aList)

elif choiceMade == 8:
    print('8. Sort the list in descending order')
    print('Current List = [ a, b, c, d] ')
    aList.sort(reverse = True)
    print(aList)

elif choiceMade == 9:
    print('9. Display the list')
    print('Current List = [ a, b, c, d] ')
    print(aList)

elif choiceMade == 0
    exit()
