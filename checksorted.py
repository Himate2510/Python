def checksorted(a):
    length = len(a)
    if length == 1 or length == 0:
        return True
    return a[0] <= a[1] and checksorted(a[1:])

a = [1, 2, 3, 4, 5, 1, 6]

if checksorted(a):
    print("The list is sorted")
else:
    print("The list is not sorted")