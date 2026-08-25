"""
# Lecture 1
print("Hello world")
print(23)  # as a number
print(4 + 3)
print("33")  # as a string


# variable (here name and age is variable where we store value)
name = "Danish"
age = 23  # means 25 value goes and stores in age variabale so like a=b meanseing value of b stores in a now
print("My name is", name, "& my Age is ", age)


age2 = age  # now the value in age stores in age 2
print(age2)

a = True
b = False
# Type

print(type(name))
print(type(age))
print(type(a))

x = 10
y = 20
print(x + y)
print(x - y)



# Arthematic operators
a = 10
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # always remains float coz anwer becames 5.0
print(a % b)  # used for finding remainders
print(a**b)  # power means a to the power b



a = 5j
print(type(a))  # complex data type only use j

b = "D"
c = "🙌"
print(ord(b))  # ord() converts character to unicode
print(ord(c))

x = 68
print(chr(x))  # chr() converts unicode into character



# Indexing

a = "Danish_Nisar"
print(a[5])
print(a[-1])

# silicing

print(a[7:12:1])  # but for end point we have to take one extra

print(a[7::1])  # here at stop if we didnt put value it will always then go to end point

print(a[7::])
# and in steps section if we also dont put value here it will by deafult takes 1 step



# Type conversion

a = 21
print(type(a))

a = str(a)
print(type(a))  #  now a is string
a = bool(a)
print(type(a))


b = "danish"
b = int(b)
print(type(b))  # invalid becuase like chaecters can be numbers bruhh



c = "danish"
print(bool(c))  # true

d = 99
print(bool(d))  # again true

# so there are some truthy valuesand some falsy values and falsy values are in notes page no. 10



# now input and output

name = "danish"
age = 19

print(name, age)
print("hello my name is", name, "and my age is", age)  # or
print(f"Assamalikum my name is {name} & my age is {age}")

# now for input
input("Hello user plz enter ur name:")
# and to store that we can use any variable

a = input("Hello user plz enter ur name:")
print(a)
print(type(a))
# and remember the data type of input() function is always string so for others use type conversation page 11.

b = int(input("Hello enter your age plz:"))
print(type(b))



# Questions

# Accept numbers from a user
# Accept age from the user and print it
# user_number = int(input("Hello plz enter your number:"))
# user_age = int(input("Hello plz enter your age:"))

# print(f"your age is {user_age} & your number is {user_number}")



# arthematic operators in page 12


a = 23
b = 10
print(a / b)  # float not int

print(a // b)
# float divison provides integer always & if number wasnt proper divided then int also
#  gives integer that comes and make hide the decimal values
print(5**2)  # means 5 ki power 2

print(a % b)  # reminder


# we can resign values in python like

a = 1
print(a)

a = 2
print(a)

a = 3
print(a)


a = a + 9  # for this we can just use a += 9 means a = a + 9 page number 13.
print(a)



#  comparision operators always provide boolean values page 14.

a = 19
b = 21
print(a > b)  # False
print(a == b)  # False
print(a < b)  # true
print(a != b)  # true
print(a <= b)  # true means smaller than oor equalto
print(a >= b)  # false

# comaprison operators can also use in strings on the basis of ascii values means unicodes unicodes
print(ord("a"))
print(ord("b"))

print("a" > "b")  # look here it compares there ascii values


# Logical operator  page number 14. { connection b/w 2 or more comparisions}

print(12 == 12 and 1.1 > 1 and a <= b and 1 > 2)
# and says if all are true then i am true
# or says id atleast one is true then i am true
# not reverse the boolean
print(12 < 5 or 1 == 2 or 1 == 1)
print(not 1 == 1)  # here not says that all the operations before me i make them reverse
print(1 == 1) != (2 < 1)



# Conditional statement
a = 13
if a > 10:
    print("I will do task 1")
else:  # no need to write here anything cause if 1 didnt execute the another one execute

    print("i will do task be")

# or
chocobar = 10
orangebar = 15

money = int(input("mummy nai kitne paise diye hai:"))
if money >= chocobar and money < orangebar:
    print(f"Ok u can buy chocobar & get {money-chocobar}rs back")
elif money >= orangebar:
    print(f"u can get orangebar and get {money-orangebar}rs back")
else:
    print("u can get nothing")



# Q1-->  Accept two numbers and print the greatest between them.

a = int(input("Enter ist number:"))
b = int(input("Enter 2nd number:"))

if a > b:
    print(f"{a} is greater than{b}")
elif b > a:
    print(f"{b} is greater than{a}")
else:
    print("both the numbers are same")


# Q2----> Accept the gender from the user as char and print the
# respective greeting message
# Ex - Good Morning Sir (on the basis of gender)

x = str(input("Enter your gender M or F / m or f:"))

if ord(x) == ord("M") or ord(x) == ord("m"):
    print("Good morning sir")

elif ord(x) == ord("F") or ord(x) == ord("f"):
    print("Good morning mam")
else:
    print("Enter valid gender")



# Q3---->  Accept an integer and check whether it is an even number or odd
a = int(input("Enter a integer:"))
if a % 2 == 0:
    print("Number is even")
else:
    print("number is odd")


# Q4----> Accept name and age from the user. Check if the user is a
# valid voter or not.
# Ex- “hello shery you are a valid voter”

user_name = str(input("Please enter your name:"))
x = str(input("Enter your gender M or F / m or f:"))

if ord(x) == ord("M") or ord(x) == ord("m"):
    user_age = int(input(f"Please enter your age Mr. {user_name}:"))
    if user_age < 18 and user_age > 0:
        print(f"u are not a valid voter Mr.{user_name}")
    elif user_age >= 18 and user_age > 0:
        print(f"u are a valid user Mr.{user_name}")


elif ord(x) == ord("F") or ord(x) == ord("f"):
    user_age = int(input(f"Please enter your age Mrs. {user_name}:"))
    if user_age < 18 and user_age > 0:
        print(f"u are not a valid voter Mrs.{user_name}")
    elif user_age >= 18 and user_age > 0:
        print(f"u are a valid user Mrs.{user_name}")


# For loop page 21.

a = range(1, 20, 2)
for i in a:
    print(i)

# or
for i in range(2, 20, 3):
    print(i)


# for loop in negative
for i in range(30, 0, -1):
    print(i)


# Lets print a table of 5

for i in range(1, 11, 1):
    print(f"5 x {i}: {5*i}")

# user input table

user_num = int(input("Enter your number Please:"))

for i in range(1, 11, 1):
    print(f"{user_num} x {i} :- {user_num*i}")



# Loops for strings page no. 22.

name = "Danish"  # using index values

for i in range(0, 6, 1):
    print(name[i])
# here it use 0 to 5 values of name varibale which contains string and use index values

# we can find lenth of our string so we dont have to count everytime


name = "Danish"  # using index values


print(len(name))  # 6 len starts from 1

for i in range(0, len(name), 1):
    print(name[i])


# Or we can directly access string bruhh damnnn 😲😲😲

a = "Python is the best"

for i in a:
    print(i)



# Break and Continue

for i in range(1, 21, 1):
    if i == 15:
        break  # at break it didnt continue it completely stops
    else:
        print(i)

for i in range(1, 21, 1):
    if i == 15:
        continue  # here at 15 it breks 15 and continues after 16 till loop ends
    else:
        print(i)


# page 23 last point that else works with loops also if break runs else didnt work if break didnt runs else works

for i in range(1, 21, 1):
    if i == 15:
        print("Break executed")
        break
    else:
        print(i)
else:
    print("else executed here ")


# or
for i in range(1, 21, 1):
    if i == 30:
        print("Break executed")
        break
    else:
        print(i)
else:
    print("else executed here & break didnt execute")



# For loop questions
# Q1---> Accept an integer and Print hello world n times

User_integer = int(input("Enter your integer :-"))
for i in range(0, User_integer, 1):
    print("Hello world")


# Q2---> Sum up to n terms

User_integer = int(input("Enter your integer :-"))
sum = 0

for i in range(1, User_integer + 1, 1):
    sum += i
print(f"{sum}")

# Q3---> Factorial of a number

n = int(input("Plz enter the number"))
factorial = 1
for i in range(1, n + 1, 1):
    factorial *= i
print(f"your factorial is {factorial}")


# Q4---> Print the sum of all even & odd numbers in a range separately

Even_sum = 0
odd_sum = 0
n = int(input("Plz enter the number"))

for i in range(1, n + 1, 1):
    if i % 2 == 0:
        Even_sum += i
    else:
        odd_sum += i
print(f"your even summ is {Even_sum} & odd sum {odd_sum}")



# Q5----> Print all the factors of a number
n = int(input("Plz enter the number"))

for i in range(1, n + 1, 1):
    if n % i == 0:
        print(i)


# Q6----> Accept a number and check if it a perfect number or not
# A number whose sum of factors is equal to the number itself
# Ex -  6 = 1, 2, 3 = 6


n = int(input("Plz enter the number"))
sum_factors = 0
for i in range(1, n, 1):
    if n % i == 0:
        sum_factors += i
        print(i)
if sum_factors == n:
    print(f"yes your number {n} is perfect number")
else:
    print(f" no your number {n} is not perfect number")



# Q7 ---> Check wether the number is prime or not

n = int(input("Plz enter the number"))
prime_sum = 0

for i in range(2, n, 1):
    if n % i == 0:
        prime_sum += i
if prime_sum == 0:
    print("yes prime number")
else:
    print("no not a prime number")

# chatgpt approach improves my ist

n = int(input("Plz enter the number"))
is_prime = True

for i in range(2, n):
    if (
        n % i == 0
    ):  # here if n =7 ans no one divisor of 7 == 0 then is pprime remains true while if there was then i will became false

        is_prime = False

if is_prime:
    print("Yes, prime number")
else:
    print("No, not a prime number")

# sir approach
n = int(input("Plz enter the number"))

count = 0

for i in range(1, n + 1, 1):
    if n % i == 0:
        count += 1
if count == 2:
    print("yes a prime")
else:
    print("not a prime")




# Q8 ---> Reverse a string without using in build functions

a = input(" Enter string")
b = ""

for i in range(len(a) - 1, -1, -1):
    b+=a[i] # it will save the reverse string in b


# Q9 ----> Check string is Pallindrome or not

a = input(" Enter string")
b = ""

for i in range(len(a) - 1, -1, -1):
    b += a[i]

if b == a:
    print(" yes it is palandrome")
else:
    print(" no it is not a palandrome")

# Q10 ---->Count all letters, digits, and special symbols from a given string
# Given: str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits, and symbols
# Chars = 8
# Digits = 3
# Symbol = 4

str1 = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbols = 0

for i in str1:
    if i.isalpha():
        # these are methods of string when ever needed go and check google methods of string used to see alphabets in string
        chars += 1
    elif i.isdigit():  # also method of string  used to see digits in string
        digits += 1
    else:
        symbols += 1

print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)


# While loop (give condition till condition is true while loop runs) page 25.
a = 1
while a <= 30:
    print(a)
    a += 1


# questions on while loop

# Q1---> Separate each digit of a number and print it on the new line.

a = int(input("Enter any number here:-"))
number = 0

while a > 0:
    print(a % 10)
    a //= 10


# Q2 ---> Accept a number and print its reverse
a = int(input("Enter any number here:-"))
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a //= 10

print(rev)


# Q3 ---> Accept a number and check if it is a pallindromic number
a = int(input("Enter any number here:-"))
rev = 0
copy = a
while a > 0:
    rev = rev * 10 + a % 10
    a //= 10

print(rev)
print(copy)
if rev == copy:
    print(" yes it is a pallandromic number")

else:
    print(" No it is not a pallondromic number")


# Create a random number guessing game with python.
# we use here a library of python called random that generates random number

import random

num = random.randint(1, 10)  # it includes both parameters also
tries = 0
print(num)
while True:

    guess = int(input("Please enter your number"))
    tries += 1

    if guess == num:  # this one is for guess condition

        print(f"u won the game and take {tries} try to complete it")
        break
    elif guess < num:
        print("try liitle bit higher")

    elif guess > num:
        print("try liitle bit lower")

    if tries == 3:
        print(
            "you loose the game"
        )  # this one is different conditional statement for differnt condition tries
        break



# Functions
def salam():
    print("Assalamuaalikum")


# here i create a function when i need this i can call this function

salam()
salam()
salam()
salam()
salam()
salam()


# parametrs and arguments page no. 27


def sum(a, b):
    print(f"Sum of your numbers is: {a+b}")


sum(2, 8)

sum(int(input("Enter ist numbers")), int(input("Enter 2nd numbers")))


def intro(name, age):
    print(f"hello {name} your age is {age}")


intro(age=19, name="danish")  # page 28. called KEY WORD ARGUMENT

# here we dont use deafult  positions of 1---> 1 and 2----> 2 we directly use with parammeters name




def cross(a, b=5):
    # we make b here default if we didnt give value in calling fun. b will take default
    print(f" multiply is {a*b}")


cross(3)
cross(9, 2)


def pallindrome(st):
    rev = ""
    for i in st:
        rev = i + rev  # for hello it will collect ist o,l,l,e,h and it is reverse
    if rev == st:

        print("yes a pallindrome")
    else:
        print("Not a pallindrome")


pallindrome("nfgamany")



# return we return the value to the line where we call it and like if we print the call function then we can see it


def hello():
    return "hello how are u"


hello()  # now value is stored at line ^88 hello() where we call it

print(hello())



# Data Structure page no. 29

# list or arrays

a = [11, 12, 13, 14, 15, 16, 11, "Hello", print(), 33.3, False, ()]
b = a.copy()  # here we use copy function to make shallow copy of list
# list indexing and slicing is same as string

print(a[0], a[11])
print(a[0:5:2])  # slicing

a[8] = "Changed"  # we modify it here

print(a)

print(b)

for i in a:
    print(i)
    for i in range(len(a) - 1):
        print(a[i])


x = 0
while x < 3:
    x += 1
    print(x)



# Q1 ---> Print positive and negative elements of an List

l = [1, 3, 7, 5, -4, 9, 7, 2, -7, -6, -3]

for i in l:
    if i > 0:
        print(i)
for i in l:
    if i < 0:
        print(i)


# Q1 ---> Mean of List elements

l = [1, 3, 7, 5, -4, 9, 7, 2, -7, -6, -3]

sum = 0

for i in l:
    sum += i

print(f"Mean of the list is {sum/len(l)}")



# Q3---> Find the greatest element and print its index too

l = [1, 3, 7, 5, -4, 9, 7, 2, -7, -6, -3]
largest = l[0]
index = 0
for i in range(0, len(l), 1):
    if l[i] > largest:
        largest = l[i]
        index = i
print(f" largest number is {largest} and at index value {index}")



# Q4---> Find the second greatest element

l = [1, 3, 7, 5, -4, 9, 7, 2, -7, -6, -3]

largest = l[0]
sec_largest = l[0]
index_1 = 0
index_2 = 0

for i in range(len(l)):
    if l[i] > largest:
        sec_largest = largest
        largest = l[i]
        index_2 = index_1
        index_1 = i
    elif l[i]>sec_largest:
    sec_largest = l[i]
    index_2=i
print(sec_largest, index_2)
print(largest, index_1)


# Q5---> Check if List is sorted or not

l = [1, 3, 7, 5, -4, 9, 7, 2, -7, -6, -3]

sorted = l[0]

for i in range(len(l) - 1):
    if l[i] < l[i + 1]:
        continue
    else:
        print("not sorted")
        break
else:
    print("yes sorted")



# Tuple page 33.

a = (1, 2, 3, 4, 5, 5)
print(a.index(5))

# tuple unpacking

a, b, c = (1, 2, 3)
# here a gets ist b gets 2nd and then c gets 3rd value

# set

a = {1, 2, 3, 4, 5}

A = {1, 2, 3}
B = {3, 4, 5}

union_set = A.union(B)  # {1, 2, 3, 4, 5}
# or
union_set1 = A | B

intersection_set = A.intersection(B)  # {3}
# or
intersection_set1 = A & B

difference_set = A.difference(B)  # {1, 2}
# or
difference_set1 = A - B

symmetric_diff = A.symmetric_difference(B)  # {1, 2, 4, 5}
# or
symmetric_diff1 = A ^ B


#  set contains keys and value pair



introduction = {
    "name": "Danish",
    "age": 19,
    "hobbies": "Barista",
    "Friend": ["s", "j", "a"],  # look we can store list and tupple also in set
    "tupple": (1, 2, 3, 4, 5),
}

print(introduction["name"])

introduction["tupple"] = 1000  # here i change the tupple value into 1000

print(
    introduction
)  # {'name': 'Danish', 'age': 19, 'hobbies': 'Barista', 'Friend': ['s', 'j', 'a'], 'tupple': 1000} output


introduction.update({"sex": "male"})  # i update my set here and add this part also
print(introduction)
# or we can do it simply
introduction["fav_lang"] = "python"  # this will also get updated like this in set
print(introduction)


# For deleting

del introduction["tupple"]  # it will delete the tupple
print(introduction)



# looping over sets

a = {
    "name": "Danish",
    "age": 19,
    "hobbies": "Barista",
    "Friend": ["s", "j", "a"],  # look we can store list and tupple also in set
    "tupple": (1, 2, 3, 4, 5),
}

for i in a:
    print(i)  # it will print / acess keys
    print(a[i])  # it will acess values

# or


for i in a.values():
    print(i)  # here it acess direct values

for i in a.keys():  # or it will be default
    print(i)

# Deep copy and shallow copy

a = [1, 2, 3]
b = a
b[0] = 100
print(a)  # look here it is deep copy we change in b & a also gets changed

c = a.copy()
c[1] = 200
print(c)
print(a)  # look here it is shallow copy only change gets in c and be remains safe


# Q1----> Write a Python script to merge two Python dictionaries

student = {"name": "Danish", "age": 19, "course": "Backend", "marks": 92}

laptop = {"brand": "HP", "model": "Victus", "ram": 16, "gpu": "RTX 3050"}

for i in laptop:
    student[i] = laptop[
        i
    ]  # means heree student[brand] = laptop[hp] here is no brand in student so it creates that in this
print(student)

# or
merge = student | laptop
print(merge)

# or
c = student.update(laptop)
print(c)


# Q2----> Write a Python program to sum all the values in a dictionary

marks = {"Python": 85, "Math": 78, "English": 90, "Computer": 88, "Physics": 82}

total = 0

for i in marks.values():
    total += i
print(total)


# Q3----> Count the frequency of each elements in a list(frequency = number of occurrences of an element)

list = [1, 2, 2, 3, 3, 3, 4, 9, 9, 9, 1, 1, 4, 1]
d = {}
for i in list:
    if i in d.keys():
        d[i] += 1  # it sees hh now 1 is available so on value it +1
    else:
        d[i] = 1  # it make ist key in of 1 and put its value in it as 1
print(d)


# Q4---> Write a Python program to combine two dictionary by adding values for common keys

d1 = {1: 10, 2: 20, 3: 30}
d2 = {3: 30, 4: 40, 5: 50}


for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

d1 = {1: 10, 2: 20, 3: 30}
d2 = {3: 30, 4: 40, 5: 50}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]


# STEP 1:
# for i in d2:

# This means:
# "Go through every KEY of d2."

# So i will be:

# i = 3
# i = 4
# i = 5


# STEP 2:
# if i in d1.keys():

# This means:
# "Check if this key already exists in d1."


# STEP 3:
# When i = 3:

# 3 is already in d1.

# So this runs:

# d1[i] += d2[i]

# Which means:

# d1[3] = d1[3] + d2[3]
#        = 30 + 30
#        = 60

# Now d1 becomes:

# {1: 10, 2: 20, 3: 60}


# STEP 4:
# When i = 4:

# 4 is NOT in d1.

# So the else part runs:

# d1[i] = d2[i]

# Which means:

# d1[4] = d2[4]
#        = 40

# Now d1 becomes:

# {1: 10, 2: 20, 3: 60, 4: 40}


# STEP 5:
# When i = 5:

# 5 is NOT in d1.

# So:

# d1[5] = d2[5]
#        = 50

# Final d1:

# {1: 10, 2: 20, 3: 60, 4: 40, 5: 50}


# EASY WAY TO REMEMBER:

# If the key already exists in d1:
#     ADD the values.

# If the key does NOT exist in d1:
#     ADD the new key and value.

# So:

# 3 exists → 30 + 30 = 60
# 4 doesn't exist → add 4:40
# 5 doesn't exist → add 5:50



# Exception handling
# in python from indentation and syntax error except all errors we can handle those e.g.,
# when error came it didnt make run the other code after that so we can handle those

# a = int(input("Enter your number:-"))


# divide = (
#     10 / a
# )  # what if user give 0 so zeroDivisionError came so we can handle it to not distrub our other code

# print(divide)

a = int(input("Enter your number:-"))

try:
    divide = 10 / a
    print(divide)
except (
    ZeroDivisionError
):  # but error has 30 to 40 types how we can remember every name so simply use
    # exception as err
    print("undefined")

print("we complete divide")



# like

a = int(input("Enter your number:-"))

try:
    divide = 10 / a
    print(divide)
except Exception as err:
    print("undefined")
else:
    print(
        "no exception here"
    )  # this one is for coder to check exception came or not if else works except not and vise versa

finally:
    print("i will run no matter what")  # it will always run bruhhh
print("we complete divide")


# and we also can create error by raise eg

age = int(input("enter your age"))

if age < 10 or age > 18:
    raise ValueError("Sorry u must have b/w 10 to 18")
else:
    print("ok u got the admission")


print(
    "hello"
)  # but this line didnt execute so we can put the code block in try and except


# output
# enter your age5
# Traceback (most recent call last):
#   File "d:\learning_py\Python.py", line 1114, in <module>
#     raise ValueError("Sorry u must have b/w 10 to 18")
# ValueError: Sorry u must have b/w 10 to 18
# PS D:\learning_py>


age = int(input("enter your age"))

try:
    if age < 10 or age > 18:
        raise ValueError("Sorry u must have b/w 10 to 18")
    else:
        print("ok u got the admission")

except Exception as err:
    print(f"so so {err}")

print("the club will start soon")



# File handling
file = open(r"D:\learning_py\chatgpt_q.py")

print(file.read())  # r in open() for reading

# creating and writting file

a = open("superman.txt", "w")
# and here my file automatically created

a.write("Hello i am Danish and creted this file ")

a.close()  # this one is important otherwise file remains open


a = open("superman.txt", "a")  # append now and also creates
a.write("now i am appending this file ")

# and "x" only creates
# there is picture in readme
# and a file_handling project



a = open("pactice_set.py", "x")  # for that i created here the file



# Class and object ----> object oriented programming


class Employee:
    language = "Python"
    salary = 120000


Danish = Employee()

Danish.mood = "sad"

print(Danish.language, Danish.salary, Danish.mood)




class room:
    a = 33  # attribute

    def table(self):  # methods
        print("hello there is a laptop")

    print("ist initilazation")


print(room().a)
room().table()


obj = room()  # object
print(obj.a)

obj2 = room()  # object
print(obj2.a)



class factory:
    def __init__(self, company, material, zips, pockets):
        self.company = company
        self.material = material
        self.zips = zips
        self.pockets = pockets
        print(
            f"{self.company} wants {self.material} as material & {self.zips} zips & {self.pockets} as pockets "
        )


addidas = factory("addidas", "leather", 3, 2)
nike = factory("nike", "cotton", 3, 5)

print(nike.pockets)




class factoryjammu:  # parent class
    a = 2

    def hello():
        print("hello i am jammu factory")


class factorykashmir(factoryjammu):  # child class
    pass


jammu = factoryjammu()
print(jammu.a)

kashmir = factorykashmir
print(kashmir.a)



# class animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"hi your name is {self.name} & age is {self.age}")


# class human(animal):
#     def __init__(
#         self, name, age
#     ):  # here came error becoz 2nd one is child and has access to parent  but cant show them so we use super fun
#         self.age = age


# a = animal("lion")
# a.show()

# b = human("Danish", 19)
# b.show()


# so we write it another way


class animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"hi your name is {self.name} & age is {self.age}")


class human(animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


a = animal("lion")
# a.show()

b = human("Danish", 19)
b.show()



# easy way to do it is use show function also in 2nd to not get error in parent


class animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"hi your name is {self.name} ")


class human(animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"hi your name is {self.name} & age is {self.age}")


a = animal("lion")
a.show()

b = human("Danish", 19)
b.show()


class human:
    pass


class animal:
    pass


class robot(human, animal):  # multiple class inherit it can inherit more classes now
    pass




# private attributes


class A:
    a = 1

    def show(self):
        print(self.a)


hi = A()
hi.show()  # look here we can easily acess the attribut and even we can change it

hi.a = 2
hi.show()
# to keep it protected we use private attribute so we can only do __





class A:
    __a = 1

    def show(self):
        print(
            A.__a
        )  # to use it we can use it in own class only and with class name only


hi = A()
hi.show()

hi.__a = 2  # it didnt change now
hi.show()



from abc import ABC, abstractmethod


class abstract(ABC):
    @abstractmethod
    def perimeter(
        self,
    ):  # now these attributes cant pass to child when @abstractmethod is given on any attribute
        pass

    @abstractmethod
    def area(self):
        pass


class Square(abstract):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        print("i have created")

    def area(self):
        print("I have created this ")


class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("i have created")

    def area(self):
        print("I have created this ")


obj = Circle(7)
obj2 = Square(12)


# Dunder methods
# use chatgpt for dunder methods in python and their use cases and how to use them easy pizy lemon squeezy



# decorate


def decorate(a):  # a is hello here
    def wrapper():
        print("hi")
        a()
        print("bye")

    return wrapper


@decorate
def hello():
    print("how are u")


hello()

# 66 page number important


def addition(a, b):
    sum = 0
    sum = a + b
    print(sum)


addition(
    2, 3, 4, 5
)  # if we send more arguments than parameters then it shows error for that we use



# Args


def addition(*args):  # it makes arguments a tuple

    print(args)  # (2, 4, 5, 7, 9, 3, 0, 1) output
    sum = 0
    for i in args:
        sum += i
    print(sum)


addition(2, 3, 5)


# args means arguments

# kwargs means key word arguments


def addition(a, b):
    sum = 0
    sum = a + b
    print(sum)


addition(
    a=2, b=3
)  # for like this but if we have to send more arguments then use kwargs



# kwargs


def addition(**kwargs):  # it makes arguments a tuple

    print(kwargs)  # here output is {'a': 2, 'b': 3, 'c': 5} dict with keys and values
    sum = 0
    for i in kwargs.values():
        sum += i
    print(sum)


addition(a=2, b=3, c=5)



# use of args and kwargs in decorate


def decorate(func):
    def wrapper(
        *args, **kwargs
    ):  # here i dont have to change arguments again and again
        print("the addition to your numbers are ")
        func(*args, **kwargs)
        print("thankyou I hope you liked it ")

    return wrapper


@decorate
def addition(a, b):
    print(f"your total is {a + b} ")


addition(
    12, 67
)  # how many i can give here using args and kwargs we dont need to change them again and again


# lambda is simply used to take arguments and result give in same line easy pizzy eg


def addition(a, b):
    sum = 0
    sum = a + b
    print(sum)


addition(2, 3)


# in easy language

addition2 = lambda a, b: a + b

print(addition2(4, 5))  # easy pizzy lemon squeezy


even = lambda a: "even" if a % 2 == 0 else "odd"

print(even(4))



# map filter and zip


a = [1, 2, 3, 4, 5]


def double(y):
    return y * 2


result = map(
    double, a
)  # "Take the function double and apply it to the values inside a. # map used for that
print(list(result))  # output [2, 4, 6, 8, 10]


# so basically map is used for like doing any operation to list or other set dict etc
#  but after the operation return same as list or set etc
# 69 to 70 page number is best for that


# Checks each item using a function (a test
# Keeps only the items that pass the test (i.e., return True)
# filter works on only true or false condition page 70

b = (1, 2, 3, 4, 5, 33, 45, 60, 98, 56)


def even(z):
    return z % 2 == 0


result2 = filter(even, b)  # it means apply filter even function to tuple b

print(list(result2))  # hey what ever we type here in that sequence we get our output
print(tuple(result2))
print(set(result2))
# but only one can work at a time


# modules and packages
# simply we can use differnt files
# e.g., if i make maths22.py and use it here


import maths22

print(maths22.addition(3, 2, 5, 6, 7))



# its called module

# pacakage is folder conatins one or more module
# eg here if i make packagesss folder and add it maths22.py and hello.py then i will show how to use them


from packagesss.hello import hi

hi()


# Type definitions
# You can send me your Python code, and I’ll add type definitions/type hints only,
# without changing your existing logic, variable names, structure, or output.


# Advanced Type Hints
# Python's (typing) module provides more advanced type hints, such as List, Tuple, Dict and Union.
from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type
identifier: Union[int, str] = "ID123"


# Match case


# it matches the given match with case e.g.,


def enter(a):
    match a:
        case 200:
            return "Ok 200"
        case 400:
            return "no 400"
        case 30:
            return "bruhh 30 seriously"
        case _:  # if no one matches
            return "wrong input"


print(enter(5))

# Merge dict

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"e": 5, "f": 6}

final = d1 | d2 | d3

print(final)
# output {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}




# we can open multiple files with "with" also e.g.,

with open("file.txt", "r") as f1, open("anotherfile.txt", "r") as f2:
    print(f1.read())
    print(f2.read())




# global keyword
# time stamp 8:42 in python of harry


# enumarate

l = [
    2,
    4,
    6,
    7,
    8,
    75,
    4,
    3,
    3,
    4,
    5,
    67,
    8,
]
index = 0
for item in l:
    print(f"the index number {index} has item {item}")
    index += 1


# this thing can be simplified using enumarate fun # important enumarate is important


l = [
    2763737,
    4,
    6,
    7,
    8,
    75,
    4,
    3,
    3,
    4,
    5,
    67,
    8,
]

for index, item in enumerate(l):  # allows us to use both index and item in a list
    print(f"the index number {index} has item {item}")

"""

# Join method

a = ["Hello", "how", "byy"]

b = "----".join(a)  # output Hello----how----byy
print(b)
