file_write = open ('Aryan3.txt', 'w')
file_write.write("Hello World")
file_write.write('HEY! What are you doing?? You aint allowed to be here')
file_write.close()

file_append = open ('Aryan3.txt', 'a')
file_append.write("\nI am appending this line")
file_append.write("\nI am appending this line")
file_append.close()

file_read = open ('Aryan3.txt', 'r')
print(file_read.read())
file_read.close()