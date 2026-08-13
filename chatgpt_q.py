"""
# Q1. ATM Withdrawal Logic

# Take from the user:

# Account balance
# Withdrawal amount

# Rules:

# Withdrawal must be a greater than 100.
# Withdrawal cannot be greater than the balance.
# If everything is valid, subtract the amount from the balance.
# Otherwise print the appropriate reason.
# Finally print the remaining balance.

balance = int(input("Enter your account balance "))
withdraw = int(input("Enter the withdrawal amount "))

if withdraw < 100 and balance >= 100:
    print("Withdrawal amount must be multiple of 100")
elif withdraw >= 100 and withdraw <= balance and balance >= 100:
    print(
        f"Your withdrawal of Rs {withdraw} is sucessfull \n remaining balaces is {balance-withdraw}"
    )
elif balance < withdraw and balance >= 100:
    print("your account has not sufficient balance")
elif balance < 100:
    print("balance should be greater than 100")


# Q2. Find the Longest Word

# Take 5 words from the user and store them in a list.

# Find the word with the largest number of characters.

# Example:

# Input:
# cat
# elephant
# dog
# tiger
# lion

# Output:
# Longest word = elephant
# Length = 8

# Rules:

# Don't use max().
# Don't sort the list.
# Use a loop.

words_num = int(input("how many words u enter :-"))
words = []

for i in range(1, words_num + 1, 1):
    word = input(f"Enter {i} word :-")
    words.append(word)

largest_word = words[0]
for i in range(len(words)):
    if len(words[i]) > len(largest_word):
        largest_word = words[i]

print(f"largest words is {largest_word}")



# Q3. Shopping Bill

# Take the prices of 5 products from the user and store them in a list.

# Calculate the total bill.

# Then apply this discount:

# Total >= 5000  → 20% discount
# Total >= 3000  → 10% discount
# Total >= 1000  → 5% discount
# Otherwise      → No discount

# Finally print:

# Original bill
# Discount
# Final bill

# Extra rule: You must calculate the total yourself using a loop.

# This combines input, type conversion, lists, arithmetic operators,
#  loops, conditions, variables and formatted output.

list = []
show_other_things = True

for i in range(5):
    product = int(input(f"Enter the price of {i+1} product :-"))
    if product > 0:
        list.append(product)
    else:
        print("Enter a valid price")
        show_other_things = False
        break
if show_other_things == True:
    sum = 0
    for i in list:
        sum += i

    def discount_fun(original_bill=sum):
        if original_bill >= 5000:
            discount = original_bill * 0.2

        elif original_bill >= 3000 and original_bill < 5000:
            discount = original_bill * 0.1

        elif original_bill >= 1000 and original_bill < 3000:
            discount = original_bill * 0.05

        else:
            discount = 0

        final_sum = original_bill - discount

        return discount, final_sum

    discount, final_sum = (
        discount_fun()
    )  # here we call function and fun returns 2 data types and we store them in 2 variables
    print(
        f" --->sir ur orginal bill is {sum} \n---> dicount applied is {discount} \n --->final bill is {final_sum}"
    )



# Q4. Username Validator

# Take a username from the user.

# Your program should check whether it is valid.

# A username is valid if:

# It contains at least 5 characters
# It contains no spaces
# It starts with a letter
# It contains only letters and numbers

# Example:

# Input: Danish123
# Output: Valid username
# Input: 123Danish
# Output: Invalid username

# Don't use advanced validation libraries.

# Use the string itself, indexing, loops and conditions to build the logic.

user_name = input("Enter your user name :-")


def user_name_checker(a=user_name):

    if len(a) < 5:
        return "Invalid username"

    for i in a:
        if i == " ":
            return "Invalid username"

    if a[0].isalpha() == False:
        return "Invalid username"

    for i in a:
        if i.isalnum() == False:
            return "Invalid username"

    return "Valid username"


print(user_name_checker())
"""

# Q5. 🧠 Bus Seat Booking

# There are 10 seats in a bus.

# Represent them using a list:

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 0 = empty
# 1 = booked

# Keep asking the user for a seat number.

# When they enter a seat:

# If the seat is empty, book it.
# If it's already booked, tell them it's occupied.
# If they enter an invalid seat number, reject it.
# Allow them to enter -1 to stop booking.
# At the end, print the final seat list and number of booked seats.

# Example:

# Choose seat: 4
# Seat 4 booked.

# Choose seat: 4
# Seat 4 is already booked.

# Choose seat: 7
# Seat 7 booked.

# Choose seat: -1

# Final seats:
# [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]

# Booked seats: 2

# This one is the best of the five for your current level because you have to
#  figure out the state of the list,
#  repeated input, conditions, indexing and loop termination yourself.
"""
seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 0

how_many = int(input("how many seats u wanna book:-"))
for_whom = []
for i in range(how_many):
    name = input(f"Enter the name of {i+1} passenger:-")
    for_whom.append(name)
for i in for_whom:

    while True:
        seat_num = int(input(f"Enter seat Number for {i}: "))

        if seat_num < 1 or seat_num > 10:
            print("Invalid seat number")

        elif seats[seat_num - 1] == 0:
            seats[seat_num - 1] = 1
            count += 1
            print("Your seat is booked")
            cancel = int(
                input(
                    "u can canel ur seat by pressing -1 or if u wanna continue then press 0"
                )
            )
            if cancel == -1:
                seats[seat_num - 1] = 0
                count -= 1
                print("ur seat is cancelled")
                break
            elif cancel == 0:
                break
            else:
                print("enter a valid option next time u lost ur chance")

        elif seats[seat_num - 1] == 1:
            print("Oops, that seat is already booked")

        if count == how_many:
            break
    if count == how_many:
        break
print("Final seats:", seats)
print("Booked seats:", count)

"""  # my chutiya code

# copilot code
# Q5. Bus Seat Booking

seats = [0] * 10  # 10 seats, all empty
count = 0  # booked seat counter

while True:
    seat_num = int(input("Choose seat (1-10) or -1 to stop: "))

    if seat_num == -1:
        break  # user wants to stop booking

    if seat_num < 1 or seat_num > 10:
        print("Invalid seat number. Please choose between 1 and 10.")
        continue

    if seats[seat_num - 1] == 0:
        seats[seat_num - 1] = 1
        count += 1
        print(f"Seat {seat_num} booked.")
    else:
        print(f"Seat {seat_num} is already booked.")

print("\nFinal seats:")
print(seats)
print("Booked seats:", count)
