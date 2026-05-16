# AI Course Enrollment System

skill = input("Enter_skill_level: ")
age = int(input("Enter_age: "))

if skill == "beginner":
    if age >= 18:
        print("Enrollment Approved")
    else:
        print("Enrollment Denied")

elif skill == "intermediate":
    if age >= 16:
        print("Enrollment Approved")
    else:
        print("Enrollment Denied")

elif skill == "advanced":
    if age >= 14:
        print("Enrollment Approved")
    else:
        print("Enrollment Denied")

else:
    print("Invalid Input")