def power2(number):

    if (number == 0):
        return 0
    if ((number & (~(number - 1))) == number):
        return 1
    return 0

number = int(input("Enter a number to check if it is a power of 2: "))
if (power2(number)):
    print("The number is a power of 2")
else:
    print("The number is not a power of 2")