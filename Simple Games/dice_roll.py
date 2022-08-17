import random

yes = ["Y", "y", "yes", "Yes"]

answer=input("Do you wanna roll the dice? ")

if answer in yes:
    roll = random.randint(1, 6)
    print("You got", roll)
else:
    print("Thanks")

