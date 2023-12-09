def password_check(password):
# Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
# Initialize variables to track if the password contains the characters
    upper = False
    lower = False
    digit = False
# Check each character in the password
    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
# Check if the password satisfy the three conditions
    return (upper and lower and digit)


password = input("Enter a password: ")
if password_check(password):
    print("Good password!")
else:
    print("Not a good password.")