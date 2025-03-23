class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

Green = parrot("Nuke", 10)
Blue = parrot("Tank", 15)
print("The name is of the parrot is", Green.name)
print("The age of the parrot is", Green.age)
print("The species of the parrot is", Green.species)
print("The name is of the parrot is", Blue.name)
print("The age of the parrot is", Blue.age)
print("The species of the parrot is", Blue.species)
