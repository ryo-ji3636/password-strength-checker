password = input("Enter your password: ")

strength = True

if len(password) >= 8:
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
    if has_digit:
        has_upper = False
        for char in password:
            if char.isupper():
                has_upper = True
                break
        if has_upper:
            strength = True
        else:
            strength = False

    else:
        strength = False
           
else: 
    strength = False

if strength:
    print("Strong")
else:
    print("Weak")

