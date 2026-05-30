# read last n lines of a file
file = open("file.txt", "r")  # r for reading the file
n = int(input("enter the number of line to read:"))

lines = file.readlines()   # readlines is used for read the all line of the file and store in the list

print(lines[-n:])  # it show the last n line of the file

file.close()  # used for close the file after reading