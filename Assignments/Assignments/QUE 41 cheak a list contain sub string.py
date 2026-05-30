main_list = [1, 2, 3, 4, 5]
sub_list = [2, 3]

found = False

for i in range (len(main_list) - len(sub_list) + 1):
    if main_list[i:i+len(sub_list)] == sub_list:
        found = True
        break

if found:
    print("sub_list found !!")

else:
    print("sub_list not found !!")