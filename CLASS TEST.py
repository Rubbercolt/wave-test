import re
import random
import string

def is_strong_password(password):
    # Check if password has at least 8 characters
    if len(password) < 8:
        return False
    
    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Check if password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    
    # Check if password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Check if password contains at least one special character
    if not re.search(r'[@$!%*?&]', password):
        return False
    
    return True

def generate_password():
    # Generate a new random password
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def suggest_password():
    print("Your password is not strong enough. Here's a suggested strong password:")
    return generate_password()

def main():
    while True:
        password = input("Enter your password: ")
        if is_strong_password(password):
            print("Your password is strong. Proceed!")
            break
        else:
            print("Invalid password. Please try again.")
            password = suggest_password()
            print("New password:", password)

if __name__ == "__main__":
    main()
