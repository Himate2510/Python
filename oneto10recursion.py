def printto10(n):
    if(n>10):
        return
    print(n)

    printto10(n+1)

printto10(1)