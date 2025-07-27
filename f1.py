import os
f = open("acp.txt" , "w")
f.write("Hello world")
f.write("\n I am Aryan")
f.write("\n I am learning Python")
f.write("\n I use VS code")
f.close()

f = open("acp.txt" , "r")
for i in f:
    h = i.strip().split()
    print(h)
f.close()
if os.path.exists("acp.txt"):
    print("File exists")
else:
    print("File does not exist")
os.remove("acp.txt")