def Maxsubarray(a, a_size):
    max = -999999999999
    cmax = 0
    for i in range(0, a_size):
        cmax = cmax + a[i]
        if max < cmax:
            max = cmax
        if cmax < 0:
            cmax = 0
    return max
a = [1,2,3,-4,3,4,1,432,6]
print(Maxsubarray(a, len(a)))