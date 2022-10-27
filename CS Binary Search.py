l = [1, 2, 3, 4, 5]
targetValue = 5
low = 0
high = len(l) - 1
x = (low + high)/ 2
mid = round(x)
while low <= high:
    if l[mid] == targetValue:
        print(mid)
        break
    elif l[mid] < targetValue:
        low = mid + 1
    elif l[mid] > targetValue:
        high = mid - 1
    x = (low + high)/ 2
    mid = round(x)
print(-1)
