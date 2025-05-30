with open('my_file.txt', 'r') as fp:
    data = fp.read()

with open('Aryan1.txt') as fp1:
    data1 = fp1.read()



print("The 2 files are being merged, please hope it works as it has a 0.000000000000000000000000000000001% chance of working")
with open('Merged.txt', 'w') as fp:
    fp.write(data1)
    fp.write(data)
print("The files have been merged successfully! :) Wow you are lucky it actuallly worked with the 0.000000 Howe many ever zeros 1% chance of working!")
