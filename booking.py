#  Cinema Seat Booking

seats = [10, 11, 12, 13, 14, 15, 16]

print("First seat:", seats[0], "| Last seat:", seats[-1])

booked_seats = seats[2:5]

print("Booked seats:", booked_seats)

if len(booked_seats) == 3:
    print("Booking confirmed for 3 seats!")
else:
    print("Booking failed")