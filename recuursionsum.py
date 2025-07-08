def arraytotalsum(a):
    length = len(a)
    if length == 1:
        return a[0]
    return a[0] + arraytotalsum(a[1:])
a = [4,453,533]
print("The sum of the array is: ", arraytotalsum(a))