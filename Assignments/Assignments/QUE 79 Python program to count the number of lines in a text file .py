# program to count the number of lines in a text file

file = open("file.txt" , "r")  # r for read the file\

count = len(file.readlines())   # readlines is used for read the file line by line 

print("number of lines in the file is:" , count)


file.close()