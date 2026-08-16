# 1. Write a program to store seven fruits in a list entered by the user
fruits = []

for i in range(1, 8):
    name = input(f"Enter fruit {i}")
    fruits.append(name)
print(fruits)
