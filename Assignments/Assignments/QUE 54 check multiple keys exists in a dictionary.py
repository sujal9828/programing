d = {"name": "sujal",
     "age": 20,
     "city": "rajasthan"
}

# keys to cheak

keys = ["name", "age", "city"]

# cheaking the keys     


for key in keys:
    if key not in d:
        print("keys does not found in the dict !!")
        break

else:
    print("all keys found !!")
     