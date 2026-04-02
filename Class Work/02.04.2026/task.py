l = [1,2,3,1,2,4]
uni = []

for i in l:
    if l.count(i) > 1 and i not in uni:
        uni.append(i)


print(uni)