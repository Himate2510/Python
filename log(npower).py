def computepower( x, y):

    result = 1

    while (y>0):
        if (y % 2 == 0):
            x = x * x
            y>>=1
        else:
            result = result * x
            y = y-1

    return result

x = int(input("Enter x: "))
y = int(input("Enter y: "))
result = computepower(x, y)
print("The result of x raised to the power y is: ", result)