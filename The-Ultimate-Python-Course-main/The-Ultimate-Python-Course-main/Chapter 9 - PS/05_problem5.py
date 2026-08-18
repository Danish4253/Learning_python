l = ["bad", "Donkey", "gf", "touch"]
with open(
    "The-Ultimate-Python-Course-main/The-Ultimate-Python-Course-main/Chapter 9 - PS/file.txt",
    "r",
) as f:
    a = f.read()
    for i in l:

        a = a.replace(i, "*" * len(i))
with open(
    "The-Ultimate-Python-Course-main/The-Ultimate-Python-Course-main/Chapter 9 - PS/file.txt",
    "w",
) as f:
    f.write(a)
