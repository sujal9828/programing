# read a file line by line and store into a variable

file = open("file.txt", "r")  #r for read the file

data = file.read()

print(data)

file.close()

