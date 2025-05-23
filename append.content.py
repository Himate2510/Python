firstfile = open('Aryan3.txt', 'r')
secondfile = open("Aryan4.txt", "w")

f1 = firstfile.read()
f2 = secondfile.write(f1)

firstfile.close()
secondfile.close()

f1 = open('Aryan3.txt', 'r')
f2 = open("Aryan4.txt", "r")

print(f1.read())
print(f2.read())
f1.close()
f2.close()
