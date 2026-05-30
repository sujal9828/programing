# num = int(input("Enter an odd number: "))

# if num % 2 == 0:
#     raise Exception("Even number is not allowed")

# print("You entered:", num)


try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero")