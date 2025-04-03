import random

def get_word():
    """Selects a random word from a predefined list."""
    words = ["python", "hangman", "developer", "challenge", "programming", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed and others as underscores."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    """Main function to play the Hangman game."""
    word = get_word()
    guessed_letters = set()
    print(guessed_letters)
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").strip().lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts remaining.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            return
    
    print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()
