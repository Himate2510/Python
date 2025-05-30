new_file = open('New_File.txt', 'x')
new_file.close()

import os
print("Does my_file exist? Or does it not? It is a mystery only I can solve.")
if os.path.exists("my_file.txt"):
    print("Yes, it exists!")
else:
    print("NOOOOOOOO!!!!!!! It does not exist! I AM REALLY SAND ANGRY AND SAD NOW!!!! :( >:(")

my_file = open('my_file.txt', 'w')
my_file.write("Hey! I am Aryan, I am in 7th grade, what about you? I am 12 years old.")
my_file.close()

os.remove('New_File.txt')

os.rmdir('New_File.txt')