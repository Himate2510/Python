def Pushzeroes(a, a_size):
    zero = 0

    nonzero = 0

    while(nonzero!= a_size):
        if a[nonzero] != 0:
            a[zero], a[nonzero] = a[nonzero], a[zero]
            zero += 1
        nonzero += 1
a = [1,5,0,0,0,4,0,2,1,0,3,2,1,0,0,0,0,0]
a_size = len(a)
print(a)
Pushzeroes(a, a_size)
print("Array after moving all zeroes to the end is:", a)
