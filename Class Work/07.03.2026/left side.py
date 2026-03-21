
for i in range(1,6):
    for k in range (1,6-i):
        print(" ",end="")

    for j in range(1,i+1):
            print("*",end="")


    print()





#    rows = 6

#for i in range(rows, 0, -1):
#    for j in range(rows - i):                          ##inverted pattern##
#        print(" ", end=" ")
#    for j in range(i):
#        print("*", end=" ")
#    print()