# This is a simple python script that was made in 100 Days Of Code Couse on day 4
import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

question = str(input("What do you choose? Rock, Paper or Scissors?\n").lower())
list = ["rock","paper", "scissors"]
random_list = random.choice(list)

if question == "rock":
    print(Rock)
    print("Computer Chose:\n")
    print(random_list)
    if random_list == "rock":
        print(Rock)
        print("\nDraw!")
    elif random_list == "paper":
        print(Paper)
        print("\nYou Loose!")
    else:
        print(Scissors)
        print("\nYou Win!")

if question == "paper":
    print(Paper)
    print("Computer Chose:\n")
    print(random_list)
    if random_list == "rock":
        print(Rock)
        print("\nYou Win!")
    elif random_list == "paper":
        print(Paper)
        print("\nDraw!")
    else:
        print(Scissors)
        print("\nYou Loose")

if question == "scissors":
    print(Scissors)
    print("Computer Chose:\n")
    print(random_list)
    if random_list == "rock":
        print(Rock)
        print("\nYpu Loose!")
    elif random_list == "paper":
        print(Paper)
        print("\nYou Win!")
    else:
        print(Scissors)
        print("\nDraw!")

else:
    print("Please choose only existing options!")
