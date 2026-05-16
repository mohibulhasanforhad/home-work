#  Smart Parking System

vehicle = input("Enter_vehicle_type: ")
hours = int(input("Enter_parking_hours: "))

if vehicle == "bike":
    fee = hours * 100
    print("Total fee:", fee, "yen")

elif vehicle == "car":
    fee = hours * 300
    print("Total fee:", fee, "yen")

elif vehicle == "truck":
    fee = hours * 500
    print("Total fee:", fee, "yen")

else:
    print("Invalid vehicle type")