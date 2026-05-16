#  Hospital Emergency Priority System

age = int(input("Enter_age: "))
emergency = int(input("Enter_emergency_level: "))

if age >= 60 or emergency >= 7:
    print("Priority Treatment")
elif age >= 18 and emergency >= 4:
    print("Normal Treatment")
else:
    print("Standard Queue")