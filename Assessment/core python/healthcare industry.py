appointment = []

slots =  ["10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm"]

while True:
    print("\n===== clinic appointment system ===== ")
    print("1. book appointment")
    print("2. view appointment")
    print("3. cancle appointment")
    print("4. Exit")

    choice = int(input("enter your choice :"))

    # book appointment #

    if choice == 1:
        name = input("enter name :")
        age = int(input("enter age :"))
        mobile = int(input("enter mobile number :"))
        doctor = input("enter doctor name :")

        print("available slots :")
        for i in range(len(slots)):
            print(i+1, slots[i])

        slot_choice = int(input("choice slot :"))
        slot = slots[slot_choice - 1]

        count = 0

        #cheak available slot

        for app in appointment:
            if app[3] == doctor and app[4] == slot:
                count += 1


        if count < 3:
            appointment.append([name, age, mobile, doctor, slot])
            print("appointment booked successfully")

        else:
            print("slot is full, please choose another slot")


    # view appointment #
    elif choice == 2:
        mobile = input("enter mobile number:")
        found = True

        for app in appointment:
            if app[2] == mobile:
                print("name :", app[0])
                print("age", app[1])
                print("doctor", app[3])
                print("slot", app[4])
                found == True

        if found == False:
            print("no appointment found with this mobile number")


    #cancel appointment #

    elif choice == 3:
        mobile = input("enter mobile number :")
        found = False

        for app in appointment:
            if app[2] == mobile:
                appointment.remove(app)
                print("appointment cancelled successfully")
                found = True
                break

        if found == False:
            print("no appointment found with this mobile number")

    # EXIT #
    elif choice == 4:
        print("thank uhh for using clinic appointment system")
        break

    else:
        print("invalid choice, please try again")

