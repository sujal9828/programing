main_string = input("enter a string :")
insert_string = input("enter a string :")

middle = len(main_string) //2

result = main_string[:middle] + insert_string + main_string[middle:]

print("result", result)