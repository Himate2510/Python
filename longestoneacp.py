def maxConsecutiveOnes(n):
    max_count = 0
    current_count = 0

    while n > 0:
        if n & 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
        n = n >> 1
    return max_count
n = int(input("Enter a number to find the maximum consecutive ones: "))
print("Maximum conescutive ones: ", maxConsecutiveOnes(n))