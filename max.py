def minElement(a,size):
    temp = a[0]
    for i in range(1, size):
        temp = min(temp, a[i])
    return temp
def maxElement(a,size):
    temp = a[0]
    for i in range(1, size):
        temp = max(temp, a[i])
    return temp

a = [8, 2, 9, 3, 12, 16]
size = len(a)
print("Minimum element is:", minElement(a, size))
print("Maximum element is:", maxElement(a, size))