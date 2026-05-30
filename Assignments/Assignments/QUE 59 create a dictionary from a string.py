string = "sujal" 

# creating a dict from the string

d = {}

for i in string:
    d[i] = d.get(i, 0) + 1

print(d)