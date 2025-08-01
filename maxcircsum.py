def kadane(a):
    n = len(a)
    max_so_far = 0
    max_ending_here = 0
    for i in range(n):
        max_ending_here += a[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

def maxcirc(a):
    n = len(a)
    max_kadane = kadane(a)

    max_wrap = 0
    for i in range(0, n):
        max_wrap += a[i]
        a[i] = -a[i]
    max_wrap = max_wrap + kadane(a)
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane
a = [1, 2, 3, -4, 3, 4, 1, 432, 6]
print(maxcirc(a))
