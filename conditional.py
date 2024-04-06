import re

def validate_username(username):
    # Username validation criteria:
    # - Contains a dot (.)
    # - Contains an @ symbol (@)

    if '.' in username and '@' in username:
        return True
    else:
        return False

def validate_password(password):
    # Password validation criteria:
    # - Length between 6 and 12 characters
    # - Contains at least one special character
    # - Contains at least one uppercase letter
    # - Contains at least one digit

    if 6 <= len(password) <= 12 and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) \
        and re.search(r"[A-Z]", password) and re.search(r"\d", password):
        return True
    else:
        return False

def main():
    valid_username = False

    while not valid_username:
        username = input("Enter a username: ")

        if not validate_username(username):
            print("Invalid username. Username must contain a dot (.) and an @ symbol.")
        else:
            valid_username = True

    valid_password = False

    while not valid_password:
        password = input("Enter a password: ")

        if not validate_password(password):
            print("Invalid password. Password must have a length between 6 and 12 characters, contain at least one special character, one uppercase letter, and one digit.")
        else:
            valid_password = True

    print("Successfully logged in!")

    # Rest of your code...

if __name__ == "__main__":
    main()
