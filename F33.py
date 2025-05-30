output_file = open('output.txt', 'w')

input_file = open('my_file.txt', 'r')

linesseensofar = set()
print("Nuking duplicate lines............ (Dont call the cops.)")
for line in input_file:
    if line not in linesseensofar:
        output_file.write(line)
        linesseensofar.add(line)

input_file.close()
output_file.close()
