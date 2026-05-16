#  Advanced E-commerce Discount System

member = input("Are you a member? ")
amount = float(input("Enter_amount: "))

if member == "yes":
    if amount >= 20000:
        final_bill = amount * 0.97
    elif amount >= 10000:
        final_bill = amount * 0.98
    else:
        final_bill = amount * 0.99
else:
    final_bill = amount

print("Final bill:", final_bill)