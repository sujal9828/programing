# append text to a file and display the text
file = open("file.txt", "a")  #a for append the text to the file
file.write("hello python\n")  # write is used for write the text to the file
file.close()  # used for close the file after writing

file = open("file.txt", "r")  # r for reading the file
print(file.read())  # it show the content of the file
file.close()  # used for close the file after reading

