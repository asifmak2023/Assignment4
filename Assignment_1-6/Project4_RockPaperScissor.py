import random

def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    """Gets the user's choice and ensures it is valid."""
    choice = input("Choose rock, paper, or scissors: ").strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
    return choice

def determine_winner(user, computer):
    """Determines the winner based on user and computer choices."""
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Main function to play the game."""
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
