#  Username Validator

username = input("Enter_username: ")

if username.isalnum() and len(username) >= 5:
    print("Valid username")
else:
    print("Invalid username")