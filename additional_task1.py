import random

f = open("books.txt", encoding="utf-8")
s = f.readlines()
if len(s) != 0:
    print(s[random.randrange(len(s))])