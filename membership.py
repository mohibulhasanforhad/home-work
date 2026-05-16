#  Restaurant Membership Discount

member = input("Are you a member? ")
bill = float(input("Enter_bill_amount: "))

if member == "yes":
    final_bill = bill * 0.90
else:
    final_bill = bill

print("Final bill:", final_bill)