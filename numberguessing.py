import random

number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100\n")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!\n")
        elif guess > number:
            print("Too high!\n")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
            break
    except ValueError:
        print("Please enter a valid number.\n")
