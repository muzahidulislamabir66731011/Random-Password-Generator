import string
import random

def generate_password(length: int) -> str:
    """Generate a random password of given length."""
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    digit = list(string.digits)
    punct = list(string.punctuation)

    # Shuffle lists (optional, random.choices is already random)
    random.shuffle(upper)
    random.shuffle(lower)
    random.shuffle(digit)
    random.shuffle(punct)

    all_chars = upper + lower + digit + punct

    # Generate password by choosing random characters
    password = ''.join(random.choices(all_chars, k=length))
    return password

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
