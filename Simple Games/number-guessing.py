import random

print("Number Guessing Game")

# randint function to generate the random no.
number = random.randint(1, 20)

# number of chances to be given to guess the no. = 5
chances = 0

print("Guess a number (between 1 and 20):")

# While loop to count the number of chances
while chances < 5:

	# Enter a number between 1 to 9
	guess = int(input())

	# Compare the user entered number
	# with the number to be guessed
	if guess == number:
		print("Congratulation YOU WON!!!")
		break

	# Check if the user entered no. is smaller than the no.
	elif guess < number:
		print("Your guess was too low: Guess a number higher than", guess)

	# Check if the user entered no. is greater than the no.
	else:
		print("Your guess was too high: Guess a number lower than", guess)

	# Increase the value of chance by 1
	chances += 1


# Check whether the user guessed the correct no.
if not chances < 5:
	print("YOU LOSE!!! The number was", number)
