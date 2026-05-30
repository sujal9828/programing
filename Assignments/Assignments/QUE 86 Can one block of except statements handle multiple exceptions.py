try:
    x = int("abc")
except (ValueError, TypeError):
    print("Exception Handled")