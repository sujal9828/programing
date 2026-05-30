file1 = open("file.txt", "r")
file2 = open("copy.txt", "w")

file2.write(file1.read())

file1.close()
file2.close()