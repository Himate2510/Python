fn = open('Aryan3.txt', 'r')
fn1 = open ('Aryan5.txt', 'w')
cont = fn.readlines()
type(cont)
for i in range(1,len(cont)+1):
    if i % 2 != 0:
        print(cont[i-1])
        fn1.write(cont[i-1])
    else:
        pass
fn1.close()

fn1 = open('Aryan5.txt', 'r')
print("The contents of the file Aryan5.txt are: ")
print(fn1.read())

fn.close()
fn1.close()