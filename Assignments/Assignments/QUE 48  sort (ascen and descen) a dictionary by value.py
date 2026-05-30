d = {"a": 10, "b": 20, "c": 40, "d": 50}

# sort the dic by value in acending order

print("Ascending order:")
print(sorted(d.items(), key=lambda x: x[1]))


#sort the dict by value in desending order

print("Descending order:")
print(sorted(d.items(), key=lambda x: x[1], reverse = True))