n = int(input("enter number :"))

a = 10
b = 20

print(a, b, end=" ")

for i in range(n-2):
    c = a + b
    print(c, end=" ")
    
    a = b
    b = c