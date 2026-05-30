a = input("enter a string :")
if len(a) < 2:
    print("empty string !!")

else:
    result = a[:2] + a[-2:]
    print("result", result)