def water(a, a_size):
    leftTallest = [0]*a_size

    rightTallest = [0] * a_size
    water = 0
    leftTallest[0] = a[0]
    for i in range(1, a_size):
        leftTallest[i] = max(leftTallest[i-1], a[i])
    rightTallest[a_size-1] = a[a_size-1]
    for i in range(a_size-2, -1, -1):
        rightTallest[i] = max(rightTallest[i+1], a[i])
    for i in range(a_size):
        water += min(leftTallest[i], rightTallest[i]) - a[i]
    return water
a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
bar = len(a)
print("Water that can be trapped is: ", water(a, bar))