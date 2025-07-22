def Median(arr, arr_size):
    sorted(arr)
    if arr_size % 2 == 0:
        return float(arr[arr_size // 2 - 1] + arr[arr_size // 2]) / 2
    else:
        return float(arr[arr_size // 2])
arr = [1, 2, 3, 8, 6, 5]
print("Median of array is:", Median(arr, len(arr)))