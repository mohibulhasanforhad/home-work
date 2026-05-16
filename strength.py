#  Password Strength Checker

password = input("Enter_password: ")

has_digit = False

for char in password:
    if char.isdigit():
        has_digit = True

if len(password) >= 8 and has_digit:
    print("Strong Password")
else:
    print("Weak Password")