# python program to find the longest words

text = input("python is very easy language")
text = input("sql is also a very easy language")

words = text.split()

longest = max(words, key=len)

print("longest word is:" , longest)