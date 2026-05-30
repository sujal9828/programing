count = 0
list = ["aba", "aa", "x", "bbb"]

for s in list:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print(count)