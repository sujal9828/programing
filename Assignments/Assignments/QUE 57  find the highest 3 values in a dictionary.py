my_dict = {"a": 10,
           "b": 20,
           "c": 30,
           "d": 40
}

# find the highest 3 value in a dict

values = sorted(my_dict.values(), reverse=True)

print("The highest value are :", values[:3])
