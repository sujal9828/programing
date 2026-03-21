for i in range(1,6):
    for j in range(1, 7):
        if (i == 1 and j % 3 != 0) or \
            (i == 2 and j % 3 == 0) or \
            (i - j == 2) or \
            (i + j == 8):
            print("❤",end=" ")

        else:
            print(" ", end="")

    print()



rows = 6

for i in range(1,6):
    for j in range (rows - i):
        print(" ", end="")


    for k in range(i):
        print("❤ ",end="")


        
    print()
