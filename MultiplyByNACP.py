def Multiply(a,b):
    return a*b
print(Multiply(2,3))
print("This is the first itteration case.")

def Multiply1(d,e):
    product = 0
    for i in range(d):
        product += e
    return product
print(Multiply1(2,3))
print("This is the second itteration case.")