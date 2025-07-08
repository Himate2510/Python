def MaxElementArray(a):
    length = len(a)
    if length == 1:
        return a[0]
    
    return max(a[0], MaxElementArray(a[1:]))
a = [4, 453, 533, 1, 2]
print("The maximum element in the array is: ", MaxElementArray(a))