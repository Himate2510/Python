def powerof8(number):
    if number == 0:
        return False
    if (number & (number - 1)) != 0:
        return False
    count = 0
    while number > 1:
        number >>= 1
        count += 1
    return count % 3 == 0

number = int(input("Enter a number to check if it is a power of 8: "))
if powerof8(number):
    print("The number is a power of 8" )
else:
    print("The number is not a power of 8" )