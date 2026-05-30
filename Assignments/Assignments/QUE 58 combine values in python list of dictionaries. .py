data = [
    {"item": "item1", "amount": 400},
    {"item": "item2", "amount": 300},
    {"item": "item1", "amount": 500}

]

result = {}

for i in data:
    result[i["item"]] = result.get(i["item"], 0)+ i["amount"]

print(result)