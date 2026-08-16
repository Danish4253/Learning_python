# marks = []

# f1 = int(input("Enter Marks here: "))
# marks.append(f1)
# f2 = int(input("Enter Marks here: "))
# marks.append(f2)
# f3 = int(input("Enter Marks here: "))
# marks.append(f3)
# f4 = int(input("Enter Marks here: "))
# marks.append(f4)
# f5 = int(input("Enter Marks here: "))
# marks.append(f5)
# f6 = int(input("Enter Marks here: "))
# marks.append(f6)

# marks.sort()

# print(marks)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

# marks = []
# m1 = int(input("Enter student 1 marks: "))
# marks.append(m1)
# m2 = int(input("Enter student 2 marks: "))
# marks.append(m2)
# m3 = int(input("Enter student 3 marks: "))
# marks.append(m3)
# m4 = int(input("Enter student 4 marks: "))
# marks.append(m4)
# m5 = int(input("Enter student 5 marks: "))
# marks.append(m5)
# m6 = int(input("Enter student 6 marks: "))
# marks.append(m6)
# marks.sort()
# print(marks)

marks = []
for i in range(1, 7):
    mark = int(input(f"Enter student {i} marks: "))
    marks.append(mark)
marks.sort()
print(marks)
