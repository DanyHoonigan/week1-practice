hours = int(input("Enter number of hours your vehicle was parked here: "))
if hours <=2:
    parking = 30*hours
elif hours >=3 and hours <=5:
    parking = 25*hours
else:
    parking = 20*hours
charge = 0
if parking >150:
    parking += 20
    charge = 20
print(f"Parking Charge: {parking}")
print(f"Service Charge: {charge}")
print(f"Final Amount: {parking+charge}")
