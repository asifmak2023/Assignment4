import random

def computer_guess(x):
    """
    This function allows the computer to guess a number the user is thinking of between 1 and x.
    The user provides feedback whether the guess is too high, too low, or correct.
    """
    
    # Initialize the lowest and highest possible values for the guess
    low = 1
    high = x
    feedback = ''  # Store user feedback
    
    print(f"Think of a number between 1 and {x}, and I will try to guess it!")
    
    # Loop until the computer guesses the correct number
    while feedback != 'c':
        # The computer makes a guess within the current range
        guess = random.randint(low, high) if low != high else low
        
        # Ask the user for feedback on the guess
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').strip().lower()
        
        # Adjust the guessing range based on feedback
        if feedback == 'h':
            high = guess - 1  # Narrow the range to lower numbers
        elif feedback == 'l':
            low = guess + 1   # Narrow the range to higher numbers
    
    # Display success message when the correct number is guessed
    print(f'Yay! The computer guessed your number, {guess}, correctly!')
    
# Example usage:
if __name__ == "__main__":
    max_number = int(input("Enter the maximum number for the guessing range: "))
    computer_guess(max_number)
