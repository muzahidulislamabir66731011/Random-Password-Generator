import string
import random
import secrets ## built-in Python module for secure random

def generate_password(length: int) -> str:
    """Generate a cryptographically secure random password of given length."""

    upper = string.ascii_uppercase # String is direct compitable with secrets.choice
                                   # And helps in space optimization
    lower = string.ascii_lowercase
    digit = string.digits
    punct = string.punctuation
    all_chars = upper + lower + digit + punct
    
    # Ensure at least one character from each category
    password = [
        secrets.choice(upper),
        secrets.choice(lower),
        secrets.choice(digit),
        secrets.choice(punct)
    ]
    
    # Fill the remaining length with random characters
    password += [secrets.choice(all_chars) for _ in range(length - 4)]
    
    # Shuffle to avoid predictable positions
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def main():
    while True:
        try:
            user_input = input("How many characters do you need (or 'q' to quit): ").strip()
            if user_input.lower() == 'q':
                print("Exiting password generator.")
                break

            password_length = int(user_input)
            if password_length <= 0:
                print("Please enter a positive integer.")
                continue
            elif password_length < 4:
                raise ValueError("Length must be at least 4 for diversity.")
                continue


            pwd = generate_password(password_length)

            print(f"Your password is: {pwd}\n")
            download=input("Do you want to save the password as text file : ?(Yes/No)").strip() 
            if download.lower()== 'yes':
                purpose = input("What is this password for? (e.g., Facebook, Gmail): ").strip()
            filename = f"{purpose}.txt"
            with open(filename.capitalize(), 'w') as file:
                file.write(pwd)
            print(f"Password saved to {filename}")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
