def smallest(arr):
    arr = sorted(arr)
    expected = 1
    for num in arr:
        if num == expected:
            expected += 1
        elif num > expected:
            break
    return expected

print("Smallest missing positive integer is:", smallest([1, 3,4, 5, 6]))