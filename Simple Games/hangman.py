import time
import json
import random
import urllib.request

url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
words = json.loads(url.read())
random_word = random.choice(words)

#Welcome the user
name = input("What is your name? ")

print("Hello " + name, "\nTime to play hangman!")

print("\n")

time.sleep(1)

print("Start guessing...")
time.sleep(1)

#Generates a random word
word = random_word

#Creates a variable with an empty value
Guess = ''

turns = 6

while turns > 0:

    failed = 0
    for char in word:
        if char in Guess:
            print(char)
        else:
            print("_")

            failed += 1

    if failed == 0:
        print("\n\nYou won")
        break

    print("\n")

    guess = input("Guess a letter:")

    Guess += guess

    if guess not in word:
        turns -= 1
        print("\nWrong")

        print("You have", + turns, 'more guesses left')

        if turns == 0:
            print("\nYou lose")
            print("\nThe word was: " + random_word)
