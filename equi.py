def equi(arr):
    leftsidesum = 0
    rightsidesum = 0
    n = len(arr)
    for i in range(n):
        leftsidesum = 0
        rightsidesum = 0
        for j in range(i):
            leftsidesum += arr[j]
        for j in range(i + 1,n):
            rightsidesum += arr[j]
        if leftsidesum == rightsidesum:
            return i
    return -1
arr = [1, 2, 3, 4, 6, -8, 3, -1, 3]
print("The index of the equilibrium point is:", equi(arr))