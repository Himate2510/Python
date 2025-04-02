class vehicle:
    def __init__(self, name, types, Topspeed, Special_Features):
        self.name = name
        self.types = types
        self.Topspeed = Topspeed
        self.Special_Features = Special_Features

class Bus(vehicle):
    pass

KindOfSchoolBus = Bus("SpecialBus", "Nuclear", 10000, "Has a nuclear bomb.")
print("The name of the kind of bus is:", KindOfSchoolBus.name, )
print("The bus type is:", KindOfSchoolBus.types)
print("The bus topspeed is:", KindOfSchoolBus.Topspeed)
print("The special feature. (That is totally safe)is:", KindOfSchoolBus.Special_Features)
