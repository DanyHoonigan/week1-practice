seats = ["Available", "Booked","Available", "Booked","Available", "Booked", "Available", "Booked"]
countt = 0
for i in seats:
    countt += 1
    print(f"Seat {countt}: {i}")

while True:
    inputt = int(input("Enter a seat number: "))
    if (seats[inputt-1]) == "Available":
        seats[inputt-1] = "Booked"
        print("Seat Successfully Booked")
        break
    else:
        print("Seat is already Booked.")
        continue
print(f"Total Seats: {len(seats)}")
print(f"Booked Seats: {seats.count("Booked")}")
print(f"Available Seats: {seats.count("Available")}")

