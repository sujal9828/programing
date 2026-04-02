s = input("Enter sentence: ")

words = s.split()

for i in range(len(words)):
    count = 0

    for j in range(len(words)):
        if words[i] == words[j]:
            count = count + 1

    print(words[i], ":", count)