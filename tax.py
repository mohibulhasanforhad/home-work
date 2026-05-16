#  Salary Tax Calculator

salary = float(input("Enter_salary: "))

if salary > 1000000:
    tax = salary * 0.30
elif salary > 500000:
    tax = salary * 0.10
else:
    tax = 0

print("Tax:", tax)