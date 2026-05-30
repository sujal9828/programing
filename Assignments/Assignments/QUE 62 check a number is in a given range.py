n = int(input("enter a number :"))

def check_number(n):
    if n in range(1, 50):
        print("number is in range !!")
         

    else:
        print("number is out of range !!")
        
check_number(n) 