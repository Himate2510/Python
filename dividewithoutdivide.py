def divide(ourDivdend, ourDivisor):
    sign = (-1 if((ourDivdend < 0) ^
               (ourDivisor < 0)) else 1)
    ourDivdend = abs(ourDivdend)
    ourDivisor = abs(ourDivisor)

    quotient = 0
    tempNumber = 0


    for i in range(31, -1, -1):
        if (tempNumber + (ourDivisor << i) <= ourDivdend):
            tempNumber += (ourDivisor << i)
            quotient |= (1 << i)

    if sign == -1:
        quotient = -quotient
    return quotient


a = int(input("Enter the dividend: "))
b = int(input("Enter the divisor: "))
print("The quotient is:", divide(a, b))
