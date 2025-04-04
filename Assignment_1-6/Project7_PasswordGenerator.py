import random
import string

def generate_password(length):
    """Generates a random password of the given length"""
    
    # Store all possible characters in a single variable
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # ascii_letters = Uppercase (A-Z) + Lowercase (a-z)
    
    # Generate a password by randomly selecting 'length' characters

    password = "".join(random.choices(all_chars, k=length))
    return password

# Ask the user for password length
num_passwords = int(input("How many passwords do you want to generate? "))
length = int(input("Enter the length of the passwords: "))

for i in range(num_passwords):
    print(generate_password(length))
