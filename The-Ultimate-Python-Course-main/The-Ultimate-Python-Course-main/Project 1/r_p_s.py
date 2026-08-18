"""
0 --> rock
1 --> paper
2 --> scissor
"""

import random

computer = random.choice([0, 1, 2])


user = input("Enter your choice: ")
user_dict = {"r": 0, "p": 1, "s": 2}
computer_dict = {0: "rock", 1: "paper", 2: "scissor"}

if user in user_dict:
    print(
        f"Computer choose {computer_dict[computer]} & u choose {computer_dict[user_dict[user]]}"
    )
    if computer == user_dict[user]:
        print("Match draw 😒")
    else:
        if computer == 0 and user_dict[user] == 2:
            print("u lose ")
        elif computer == 1 and user_dict[user] == 0:
            print("u lose")
        elif computer == 2 and user_dict[user] == 1:
            print("u lose ")
        else:
            print("u won")

else:
    print("Enter a valid input")
