# rock_paper_scissors.py

import random

options = ["rock", "paper", "scissors"]
user_score = 0
comp_score = 0

print("🎮 Rock Paper Scissors Game!")
print("Type 'quit' to exit.\n")

while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    if user_choice not in options:
        print("Invalid choice. Try again.\n")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("✅ You win!\n")
        user_score += 1
    else:
        print("❌ Computer wins!\n")
        comp_score += 1

    print(f"Score - You: {user_score}, Computer: {comp_score}\n")
