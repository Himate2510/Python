class Vehicle:
    def __init__(self, Type, Company, Top_speed):
        self.Type = Type
        self.Company = Company
        self.Top_speed = Top_speed

mode = Vehicle("SUV", "Ferrari", 280)

print("The top speed of the car is:", mode.Top_speed)
print("The type of the car is:", mode.Type)
print("The company of the car is:", mode.Company)