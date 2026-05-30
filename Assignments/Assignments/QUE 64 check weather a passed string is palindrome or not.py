s = input("enter a string :")

def palindrome(s):

    if s == s[::-1]:
        print("string is palindrome !!")

    else:
        print("string is not palindrome !!")

palindrome(s)

