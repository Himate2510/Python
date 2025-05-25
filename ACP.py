sample_file = open('Sample_File.txt', 'w')
sample_file.write("Hey what are yyou doing? My name is Aryan, I am in 7th grade what bout you? I am 12 years old.")
sample_file.close()


sample_file = open('Sample_File.txt', 'a')
sample_file.write(" I am a penguin, What are you?")
sample_file.close()
sample_file = open('Sample_File.txt', 'r')

print(sample_file.read())
sample_file.close()
