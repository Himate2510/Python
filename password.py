import random
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ42423452709987654321"
number = int(input("What do you want the lenght of your passcode to be?: "))
for i in range(number):
    print(random.choice(Alphabet), end="")