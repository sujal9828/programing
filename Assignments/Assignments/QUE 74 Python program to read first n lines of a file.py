# read first n line of file

file = open("file.txt", "r")  #r for reading the file

n = int(input("enter the number of line to read:"))

for i in range(n):
    print(file.readline())  #readline is used for read the line of the file
    