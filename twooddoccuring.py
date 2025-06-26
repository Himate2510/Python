def printtwoodd(arr, size):
    xorof2 = arr[0]

    x = 0
    y = 0


    setbit = 0

    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]

    setbit = xorof2 & ~(xorof2 - 1)

    for i in range(size):
        if(arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    print("The two odd occurring elements are: ", x, " and ", y)
arr = []

arr_size = int(input("Enter the size of the array...: "))
for i in range(0,arr_size):
    g = int(input("Enter a element: "))
    arr.append(g)
printtwoodd(arr, arr_size)