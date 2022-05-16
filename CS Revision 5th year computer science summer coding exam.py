#Program 1
f = open('file.txt', 'r')
p = f.read(100)
print(p)
list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num = p.count(list)
print(num)
f.close()
#Program 2 