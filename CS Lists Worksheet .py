#1
list1 = []
print(list1) #This is Empty like ME!!!

#2

list = [1,2,3,4,5,6,7,8,9,10]
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
list.clear() #removes all items from the list
list.index(7) #returns the position of the first occurrence of x in a list
list.count(8) #returns the number of times x appears in a list
list.reverse() #reverses list elements
list.copy(list1) #returns a copy of the list
print(list1)

#3
list2=["a", "b", "c", "d"]
print(list2)
print("""1. Append an element
2. Insert an element
3. Append a list to the given list
4. Modify an existing element
5. Delete an existing element from its position
6. Delete an existing element with a given value
7. Sort the list in the ascending order
8. Sort the list in descending order
9. Display the list.""")
