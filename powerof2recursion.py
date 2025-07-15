def pow(n):
    count = 0
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return pow(n / 2)
    return False
n = int(input("Enter your number to check if it is a power of two: "))
if pow(n):
    print(n, "is a power of two")
else:
    print(n, "is not a power of two")