import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 10.")

number_to_guess = random.randint(1,10)

attempts = 0
guess = 0

while guess != number_to_guess:
    try:
        guess = int(input("Enter your guess: "))

        if guess < number_to_guess:
            print("Too low")
        elif guess > number_to_guess:
            print("Too high")
        else:
            print("🐟Correct🐟")
    except ValueError:
        print("Please enter a valid number.")
        