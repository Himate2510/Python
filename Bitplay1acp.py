def bitplay(number):
    return number & -number
number = int(input("Enter a number to find its rightmost set bit: "))
print("The rightmost set bit of the number is:", bitplay(number))
