def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y== 0:
        return "Error: You can not divide any number by 0"
    return x / y

print("Calculator (Not scientific)")
print("Option 1. Add")
print("Option 2: Subtract")
print("Option 3. Multiplication")
print("Option 4. Divide")

choice = input("Enter either of the choices for the operation you want to do: ")

if choice in ("1", "2", "3", "4"):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
