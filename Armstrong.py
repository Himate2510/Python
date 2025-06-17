number = int(input("Enter a number: "))

digits = len(str(number))

resultNumber = 0

temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digits
    temp //= 10

if number == resultNumber:
    print(number, "Your number is in fact an armstrong number....... Or is it?")
else:
    print(number, "Your number is not a Armstron number")



    