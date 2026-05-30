from multiprocessing import Value


keys = ['a', 'b', 'c', 'd']
Values = [10, 20, 30, 40]

#map the above two lists in dict

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = Values[i]

print(my_dict) 