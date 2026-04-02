student_id = 1

name = ""
age = 0
student_class = 0
mobile = ""

while True:
    print("\n==== school management system ====")
    print("1. New Admission")
    print("2. view student details")
    print("3. update student info")
    print("4. remove student from record")
    print("5. exit")

    choice = int(input("enetr your choice :"))

    if choice == 1:
        if name == "a":
            print("student record already exists !")
            

        else:
            a = input("eneter student name :")
            b = int(input("eneter student age :"))
            c = int(input("enter class (1-12) :"))
            d = input("enter guardian mobile number :")

            if b < 5 or b > 18:
                print("invalid age ! age should be between 5 and 18.")

            elif c < 1 or c > 12:
                print("invalid class ! class should be between 1 and 12.")

            elif len(d) != 10:
                print("invalid mobile number ! mobile number should be 10 digit long.")

            else:
                name = a
                age = b
                student_class = c
                mobile = d
                print("Admission successful !")
                print("student ID is", student_id)

    elif choice == 2:
        sid = int(input("enter student ID to view details :"))

        if sid == student_id and name != "":
            print("\n--- student details ---")
            print("student ID :", student_id)
            print("name :", name)
            print("age :", age)
            print("class :", student_class)
            print("guardian mobile number :", mobile)
        else:
            print("student record not found !")

    elif choice == 3:
        sid = int(input("enter student iD to update details :"))

        if sid == student_id and name == "":
            print("1. update mobilr number :")
            print("2. update class :")

            update_choice = int(input("enter your choice :"))

            if update_choice == 1:
                new_mobile = input("enter new mobile number :")
                if len(new_mobile) == 10:
                    mobile = new_mobile
                    print("mobile number updated successfully !")

                else:
                    print("invalid mobile number.")

            elif update_choice == 2:
                new_class = int(input("enter new class (1-12) :"))
                if new_class >= 1 and new_class <= 12:
                    student_class = new_class
                    print("class updated successfully.")
                else:
                    print("invalid class !")

            else:
                print("invalid update choice.")

        else:
            print("student record not found")

    elif choice == 4:
        sid = int(input("enter student ID to remove record :"))

        if sid == student_id and name != "":
            name = ""
            age = 0
            student_class = 0
            mobile = ""
            print("student record removed successfully !")
        else:
            print("student record not found !")
    
    elif choice == 5:
        print("exiting the system. goodbye !")
        break

    else:
        print("invaloid choice. please try again.")
        
            



            

