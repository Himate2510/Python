class Employee:
    def __init__(self):
        print("You have hired a new employee!")
    def __del__(self):
        print("Employee is bye bye!")

obj = Employee()
del obj
print(obj)