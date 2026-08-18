f = open(
    "The-Ultimate-Python-Course-main/The-Ultimate-Python-Course-main/Chapter 9 - PS/poem.txt"
)
content = f.read()
if "twinkle" in content:
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")

f.close()
