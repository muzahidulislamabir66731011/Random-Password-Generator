import string
import random
import secrets  

def generate_password(length: int) -> str:
    """Generate a cryptographically secure random password of given length."""

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digit = string.digits
    punct = string.punctuation
    all_chars = upper + lower + digit + punct


    password = [
        secrets.choice(upper),
        secrets.choice(lower),
        secrets.choice(digit),
        secrets.choice(punct)
    ]

    if length > 4:
        password += [secrets.choice(all_chars) for _ in range(length - 4)]


    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def main():
    """Main function to run the password generator application."""
    while True:
        try:
            user_input = input("Enter the desired password length (or 'q' to quit): ").strip()
            if user_input.lower() == 'q':
                print("Exiting the password generator. Goodbye!")
                break

            password_length = int(user_input)

            if password_length < 4:
                print("Password length must be at least 4 to include all character types.")
                continue

            pwd = generate_password(password_length)
            print(f"\nYour new secure password is: {pwd}\n")

            save_file = input("Do you want to save this password to a text file? (yes/no): ").strip().lower()
            if save_file == 'yes':
                purpose = input("What is this password for? (e.g., Gmail, GitHub): ").strip()
                if purpose:  
                    filename = f"{purpose.replace(' ', '_')}.txt"
                    with open(filename, 'w') as file:
                        file.write(f"Password for {purpose}:\n")
                        file.write(pwd)
                    print(f"Password saved to '{filename}'")
                else:
                    print("No purpose given, so the password was not saved.")

        except ValueError:
            print("Invalid input. Please enter a valid number for the length.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        print("-" * 30) 

if __name__ == "__main__":
    main()

