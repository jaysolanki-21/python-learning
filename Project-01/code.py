import random

print("Hello! Welcome to the Snake Water Gun Game.\n")

choices = {
    0: "Snake",
    1: "Water",
    2: "Gun"
}

try:
    user_input = int(input("Enter 0 for Snake, 1 for Water, and 2 for Gun: "))
    if user_input not in choices:
        print("Invalid choice. Please enter 0, 1, or 2 only.")
    else:
        computer_choice = random.randint(0, 2)

        print(f"\nYou chose: {choices[user_input]}")
        print(f"Computer chose: {choices[computer_choice]}\n")

        if user_input == computer_choice:
            print("It's a Tie!")
        elif (user_input == 0 and computer_choice == 1) or \
             (user_input == 1 and computer_choice == 2) or \
             (user_input == 2 and computer_choice == 0):
            print("You Win!")
        else:
            print("Computer Wins!")
except ValueError:
    print("Invalid input! Please enter a number (0, 1, or 2).")
