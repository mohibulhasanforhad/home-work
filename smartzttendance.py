#  Smart Attendance System

attendance = float(input("Enter_attendance: "))
assignment = input("Assignment_submitted? ")

if attendance >= 75 and assignment == "yes":
    print("Eligible for final exam")
elif attendance < 75:
    print("Not eligible (low attendance)")
else:
    print("Not eligible (missing assignment)")