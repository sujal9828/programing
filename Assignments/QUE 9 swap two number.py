# swap two number using temp variable #
a = 10
b = 20

temp = a

a = b
b = temp

print("After swapping : a =",a, "and b =",b)



# without useing temp variable #
a = 10
b = 20

a = a + b
b = a - b
c = a - b

print("After swapping : a =", a, "and b =",b)