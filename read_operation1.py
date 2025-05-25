file = open("Aryan4.txt", 'r')
print(file.read())
file.close()

file = open('Aryan4.txt', 'r')
print("Read the thing in parts")
print(file.read(8))
file.close()

file = open('Aryan4.txt', 'a')
file.write(" Hey I am a penguin, What are you?")
file.close()
