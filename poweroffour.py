n = int(input("Enter your number to check if it is a power of four: "))
def ifpower(n):
    if(n<=0):
        return False
    if(n==1):
        return True
    if(n%4==0):
        return ifpower(n/4)
    return False

if(ifpower(n)):
    print(n, "is a power of four")
else:
    print(n, "is not a power of four")