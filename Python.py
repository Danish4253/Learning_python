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
"""

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
