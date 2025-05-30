with open('Aryan.txt', 'w') as file:
    file.write("Hey what are you doing? My name is Aryan, I am in 7th grade what about you? I am 12 years old.")
file.close()

with open('Aryan.txt', 'r') as file:
    data = file.readlines()
    print("The words inside of this file is:............................................................................................................................................... Here:")
    for line in data:
        word = line.split()
        print(word)
    file.close()