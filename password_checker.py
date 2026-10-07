def is_strong(password):
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
password = input("Enter your password: ")

# check if the password is strong
if is_strong(password):
    print("Strong password")
else:
    print("Weak password")
