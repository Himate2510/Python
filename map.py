numbersa = [1, 4 ,7, 9]
numbersb = [2, 3, 5, 6]
result = map(lambda x, y: x + y, numbersa, numbersb)
print(list(result))

numbers = [1,5,7,2,5634,2,0]
def square(x):
    return x*x
square = list(map(square, numbers))
print(square)