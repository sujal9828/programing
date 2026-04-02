a = int(input("enter first integer :"))
b = int(input("enter second integer :"))
c = int(input("enter third integer :"))

if a==b or b==c or a==c:
    total = 0

else:
    total = a+b+c

print("the sum is :", total)
