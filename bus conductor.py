
def is_strong_password(password):
    # Check if password has at least 8 characters
    if len(password) < 8:
        return False
    
    # Check if password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check if password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Check if password contains at least one digit
    if not re.search(r'[0-9]', password):
        return False
    
    # Check if password contains at least one special character
    if not "research"(r'[@$!%*?&]', password):
        return False
    
    return True

def suggest_password():
    # This function suggests a new password if the user's password is not strong
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
            password = ()

if __name__ == "__main__":
    main()