def calculate_product(numbers):
    product = 1
    for number in numbers:
        product = number
    return product


tuple = (2, 3, 5, 7)


result = calculate_product(tuple)
print("Product of the tuple is... ", result)