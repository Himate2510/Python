def setOrNot(number, n):
    if number & (1 << (n - 1)):
        print("\n It is a set")
    else:
        print("\n It is not a set")


number = int(input("Please enter a number: "))
n = int(input("Please enter the bit number: "))
setOrNot(number, n)