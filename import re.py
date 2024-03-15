import re

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

def suggest_password():
    print("Your password is not strong enough. Please follow these rules:")
    print("- Minimum length of 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character from @$!%*?&")
    print()
    return input("Please enter a new password: ")

def main():
    while True:
        password = input("Enter your password: ")
        if is_strong_password(password):
            print("Your password is strong. Proceed!")
            break
        else:
            password = suggest_password()

if __name__ == "__main__":
    main()
