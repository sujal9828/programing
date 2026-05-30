d1 = {"a": 10, }
d2 = {"b": 20}
d3 = {"c": 30}

# concatenate the above dictionaries to create a new one
new_dict = {}

new_dict.update(d1)
new_dict.update(d2)
new_dict.update(d3)

print(new_dict)

