s = input("enter a name :")
if len(s) < 3:
    print(s)

elif s.endswith("ind"):
    print(s + "ly")

else:
    print(s + "ing")