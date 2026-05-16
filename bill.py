#  Electricity Bill Warning

units = int(input("Enter_units: "))

if units > 500:
    print("High Bill")
else:
    print("Normal Bill")