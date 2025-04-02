import random

def main():
    secret_number = random.randint(1, 100)
    print("Guess the number between 1 and 100")
    
    attempts = 0  # Initialize attempts counter
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        attempts += 1  # Increment attempts with each guess
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    main() 