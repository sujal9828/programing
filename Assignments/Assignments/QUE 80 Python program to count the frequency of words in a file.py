# Count frequency of words in a file

file = open("file.txt", "r")

text = file.read()
words = text.split()

for word in set(words):
    print(word, ":", words.count(word))

file.close()