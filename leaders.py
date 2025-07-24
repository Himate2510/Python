def leaders(a, a_size):
    currentmax = a[a_size-1]
    print(currentmax)

    for i in range(a_size-2, -1, -1):
        if currentmax < a[i]:
            print(a[i])
            currentmax = a[i]

a = [16, 17, 4, 3, 5, 2]
a_size = len(a)
leaders(a, a_size)