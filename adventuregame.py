# adventure_game.py

def start_game():
    print("\n🏞️ Welcome to the Adventure Game!")
    print("You're in a dark forest. You see a path to the left and right.")

    choice = input("Which way do you want to go? (left/right): ").lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Game Over.")

def left_path():
    print("\nYou walk left and see a river.")
    action = input("Do you want to swim across or walk along the river? (swim/walk): ").lower()

    if action == "swim":
        print("You swim safely and find a treasure chest. 🎉 You win!")
    else:
        print("You get lost in the woods. 😢 Game over.")

def right_path():
    print("\nYou walk right and find a dark cave.")
    action = input("Do you want to enter the cave or walk past it? (enter/past): ").lower()

    if action == "enter":
        print("A bear wakes up and chases you out. 😱 Game over.")
    else:
        print("You walk past and find a friendly village. 🎉 You win!")

start_game()
