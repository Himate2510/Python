def print2largest(a, a_size):
    largest = second_largest = -2147483648
    for i in range(a_size):
        if (a[i] > largest):
            second_largest = largest
            largest = a[i]
        
        elif (a[i] > second_largest and a[i] != largest):
            second_largest = a[i]
    print("The second largest element is:", second_largest)
a = [12, 35, 1, 10, 34, 1]
a_size = len(a)
print2largest(a, a_size)
