#  Bank Loan Eligibility System

salary = float(input("Enter_salary: "))
experience = int(input("Enter_experience: "))

if salary >= 300000 and experience >= 2:
    print("Loan Approved")
elif salary < 300000:
    print("Salary requirement not met")
else:
    print("Experience requirement not met")