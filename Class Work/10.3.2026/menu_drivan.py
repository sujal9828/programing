while True:
    menu = """
    press 1 for Fac number
    press 2 for fibonnaci
    press 3 for prime number
    press 4 for Exit

"""
    print(menu)
    choice = int(input("enter choice :"))

    if choice==1:
         for i in range (1,6):
            for k in range (1,6,i):
               print(" ",end="")
            for j in range (1,1+i):
             print("*",end="")
                      
            print()


    elif choice==2:
     for i in  range(1,6):
      for j in range (1,i+1):
        print("*",end="")

      print()

    elif choice==3:
     
     rows = 6
     for i in range( 0, -1):
      for j in range(rows - i):
        print(" ", end="")  
      print()

    elif choice==4:
    
      print("tank uh!!")
      break

    

    else:
      print("invalid choice!!")
      break









        
    
            
        
    

    
