list1 = [1, 2, 3]
list2 = [1, 2, 3]

found = False

for i in list1:
    if i in list2:
        found = True
        break

print(found )