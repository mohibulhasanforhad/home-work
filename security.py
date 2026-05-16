#  Smart Login Security System

username = input("Enter_username: ")
password = input("Enter_password: ")
otp = input("Enter_OTP: ")

if username == "admin":
    if password == "12345":
        if otp == "9999":
            print("Login Approved")
        else:
            print("Invalid OTP")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")