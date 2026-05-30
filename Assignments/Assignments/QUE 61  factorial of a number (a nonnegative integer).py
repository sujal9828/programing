n = input("enter a nonnegative integer :")

def factorial(n):
    if n == 0:
        return 1
    
    else:
        return n * factorial(n-1)
    
print("factorial of given number is :", factorial(int(n)))

