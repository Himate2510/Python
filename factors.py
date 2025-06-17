def printfactors(number):
    print("The factors for", number, "are:  ")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

number = int(input("Enter your number if you want to see its factors: "))

printfactors(number)