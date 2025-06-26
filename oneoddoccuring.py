def oddoccurring(arr):
    res = 0

    for element in arr:
        res = res ^ element
    
    return res
arr = []

n = int(input("Enter the size of the array: "))

while(n):
    num = int(input("Enter a number: "))
    arr.append(num)
    n -= 1

print("\n\n\n The odd occurring element is: ", oddoccurring(arr))