# read file line by line and store in into list

file = open("file.txt" , "r")  # r for reading the file

lines = file.readlines()  #readlines is used for read the all line of file and store in the list

print(lines)  # it shows the all line of the file in the list

file.close()  # used for close the file after reading

