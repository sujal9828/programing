#def greatest_number():
#    n1 = int(input("enter number 1 :"))
#    n2 = int(input("enter number 2 :"))
#    n3 = int(input("enter number 3 :"))

#    if n1 > n2 and n1 > n3:
#        print(n1,"is greatest")
#    elif n2 > n3:
#        print(n2,"is greatest")
#    else:
#        print(n3,"is greatest")



#def prime_number():

#    num = int(input("enter number :"))
#    if num > 1:
#        for i in range(2, num):
#            if num % i == 0 :
#                print("not a prime number ")
#                break
#            else:
#               print("is prime number")

#    else:
#        print("not a prime number ")

#def triangle():
             
#    rows = 6
#    for i in range(1,6):
#        for j in range(rows - i):
#            print(" ",end="")

#        for k in range(i):
#            print("* ",end="")

#    print()

#def menu_drivan():
#    while True:
#        menu = """
#        press 1 for greatest number
#        press 2 for prime number
#        press 3 for triangle
#        press 4 for exit
#"""
#        print("menu")
#        choice = int(input("enter choice :"))

#        if choice == 1:
 #           greatest_number()
#
#        elif choice == 2:
#            prime_number()

#        elif choice == 3:
#            triangle()

#        elif choice == 4:
#            print("thank uhh !!")
    

 #       else:
 #           print("invalid choice ")

#menu_drivan()
#menu_drivan()



#def greatest_number():

#    n1 = int(input("enter number 1 :"))
#    n2 = int(input("enter number 2 :"))
#    n3 = int(input("enter number 3 :"))

#    if n1 > n2 and n1 > n3:
#        print(n1,"is greatest")
#    elif n2 > n3:
#        print(n2,"is greatest")
#    else:
#        print(n3,"is greatest")

#def prime_number():
#    num = int(input("enter number :"))
#    if num > 1:
#        for i in range(2, num):
#            if num % i == 0 :
#                print("not a prime number")
#                break
#            else:
#                print("is a prime number")
            
#    else:
#        print("not a prime number")



#def triangle():
#    rows = 6
#    for i in range(1, 6):
#        for j in range(rows - i):
#            print(" ",end="")

#            for k in range(i):
#                print("* ",end="")   

#    print()


#def menu_driven():
#    while True:
#        menu = """
#        press 2 for greatest number
#        press 2 for prime number
#        press 3 for triangle
#        press 4 for exit
#"""
#        print(menu)
#        choice = int(input("enter choice :"))
#        if choice == 1:
#            greatest_number()

#        elif choice == 2:
#            prime_number()

#        elif choice == 3:
#            triangle()

#        elif choice == 4:
#            print("thank uhh !!")
#            break

#        else:
 #           print("invalid choice")
 #           break

#menu_driven()




#def greatest_number():
#    n1 = int(input("enter number 1"))
#    n2 = int(input("enter number 2"))
#    n3 = int(input("enter number 3"))

#    if n1 > n2 and n1 > n3 :
#        print(n1,"is greatest !!")
#   elif n2 > n3 :
#        print(n2,"is greatest !!")
#    else:
#        print(n3,"is greatest !!")


#def prime_number():
#    num = int(input("enter number :"))
#    if num > 1:
#        for i in range(2, num):
#            if num % 1 ==0:
#                print("not a prime number !!")
#                break

#            else:
#                print("is a prime number !!")

#    else:
#        print("not a prime number !!")


#def triangle():
#    rows = 6
#    for i in range(1,6):
#        for j in range(rows-i):
#            print("",end="")
#        for k in range(i):
#            print("* ",end="")

#        print()



#def menu_driven():
#    while True:
#        menu ="""

#        press 1 for greatest number
#        press 2 for prime number
#        press 3 for triangle
#        press 4 for exit
#        """
        
#        print(menu)
#        choice = int(input("enter choice :"))

#        if choice == 1:
 #           greatest_number()

 #       elif choice == 2:
 #           prime_number()

#        elif choice == 3:
#            triangle()

#        elif choice == 4:
#            print("thank uhhhh !!")
#            break

#        else:
#            print("invalid choice")
#            break

#menu_driven()



def greatest_number():
    n1 = int(input("enter number 1 :"))
    n2 = int(input("enter number 2 :"))
    n3 = int(input("enter number 3 :"))

    if n1 > n2 and n1 > n3:
        print(n1,"is greatest")

    elif n2 > n3:
        print(n2,"is greatest")

    else:
        print(n3,"is greatest")
    
def prime_number():
    num = int(input("enter number :"))
    if num > 1:
        for i in range(2, num):
            if num % 1 == 0:
                print("not a prime number")
                break

            else:
                print("is a prime number")

    else:
        print("not a prime number")

def triangle():
    rows = 6
    for i in range(1,6):
        for j in range(rows - i):
            print(" ",end="")

        for k in range(i):
            print("* ",end="")

    print()


def menu_driven():
    while True:
        menu = """
        press 1 for greatest number
        press 2 for prime number
        press 3 3for triangle
        press 4 4for exit
"""
        print(menu)
        choice = int(input("enter choice :"))

        if choice == 1:
            greatest_number()

        elif choice == 2:
            prime_number()

        elif choice == 3:
            triangle()

        elif choice == 4:
            print("thak uhh!!")
            break

        else:
            print("invalid choice")
            break
menu_driven()


