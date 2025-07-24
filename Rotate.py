def rotations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)

def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size-1):
        a[i] = a[i+1]
    a[a_size - 1] = temp

def print_array(a, a_size):
    for i in range(a_size):
        print(a[i], end=' ')
    print()

a = [6, 23, 634, 1, 423, 6]
print_array(a, len(a))
rotations(a, 2, len(a))
print_array(a, len(a))