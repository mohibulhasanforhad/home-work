#  Bus Fare System

age = int(input("Enter_age: "))

if age <= 12:
    fare = 150
elif age <= 17:
    fare = 300
elif age <= 59:
    fare = 500
else:
    fare = 200

print("Bus fare:", fare, "yen")