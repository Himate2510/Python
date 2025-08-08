def longest(arr):
    max_len = cur = 1
    for i in range(1, len(arr)):
        cur = cur + 1 if arr[i] %2 != arr[i-1] % 2 else 1
        max_len = max(max_len, cur)
    return max_len

print(longest([1, 2, 2, 4, 5, 6, 7, 8, 9]))