data = ["Python", "Java", "SQL"]

file = open("file.txt", "w")

for i in data:
    file.write(i + "\n")

file.close()