#  Login System with Nested Conditions

username = input("Enter_username: ")
password = input("Enter_password: ")

if username == "admin":
    if password == "12345":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")