#  University Admission System

gpa = float(input("Enter_GPA: "))
ielts = float(input("Enter_IELTS: "))

if gpa >= 3.5 and ielts >= 6.5:
    print("Eligible for admission")
elif gpa < 3.5:
    print("GPA requirement not met")
else:
    print("IELTS requirement not met")