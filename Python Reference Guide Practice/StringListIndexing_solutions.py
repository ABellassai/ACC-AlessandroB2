#initial string to process
my_str = "Hello World"

# Use string[i] to return the first character
# 1st letter
print("First character: ",my_str[0])

# Use string[i] to return the character at position 4
# 4th letter
print("Fourth character: ",my_str[3])

#Use string[i] to return the last character 
print("Last character: ",my_str[-1])
print("Last character: ",my_str[len(my_str)-1])

# Use string[i:j] to return the subtring Hello
print("Characters in range 0:5: ",my_str[0:5])

#Use list = [] to create an empty list
list = []

#Use list = [] to create a list with "Apple", "Orange", "Cherry","Tomato"
list = ["Apple", "Orange", "Cherry","Tomato"]

#Use list[i] = x to replace the 3rd item in the list with the value "Grape"
print(list) # original list
list[2] = "Grape"
print(list) # updated list

#Use list[i] to return the first item in the list
print(list[0])

# list[i] to return the last item in the list
print(list[-1])
print(list[len(list)-1])

#Use list[i:j] to return a sublist of the first middle two items
print(list[1:3])

# list[i:] to print all the items in the list starting from Grape
print(list[2:])

#Use del list[i] to remove the 3rd item in the list
del list[2]
print(list)