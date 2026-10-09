# Password strength checker script

#import getpass because we want to hide the password input from the console
import getpass

# Load common passwords from a file into a list
COMMON_PASSWORDS = []

with open("common_passwords.txt") as f:
    for line in f:
        word = line.strip()
        if word:
            COMMON_PASSWORDS.append(word)

def is_strong(password):
    # convert password to lowercase for common password check
    #(it makes big-O small because we avoid repeated lower() calls)
    lower_password = password.lower()  
    for common in COMMON_PASSWORDS:
        if common in lower_password:
            return False
    # check password strength
    has_digit = False
    has_upper = False
    has_lower = False
    has_symbol = False
    length_ok = False

    # check there are a digit and uppercase letter in the password
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if not char.isalnum():
            has_symbol = True

    # check if the length of password is over 8 characters
    if len(password) >= 8:
        length_ok = True


    # final check
    if has_digit and has_upper and length_ok and has_lower and has_symbol:
        return True
    else:
        return False


# Input password from user
password = getpass.getpass("Enter your password: ")

# check if the password is strong
if is_strong(password):
    print("Strong password")
else:
    print("Weak password")
