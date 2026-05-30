n = int(input("enter a number :")) 

def perfect_number(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total = total + i


    if total == n:
        print("number is pefect  !!")

    else:
        print("number is not perfect !!")

perfect_number(n)
    
