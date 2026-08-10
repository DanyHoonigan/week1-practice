name = input("Enter your name:")
age = int(input("Enter your age: "))
tickets = int(input("Enter number of tickets: "))
price = 0
if age < 12:
    price = 120*tickets
elif age >=12 and age <=59:
    price = 200*tickets
else:
    price = 150*tickets
if tickets >=5:
    discount = price*0.1
print(f"Customer Name: {name}")
print(f"Ticket Price: {price}")
print(f"Number of Tickets: {tickets}")
print(f"Total Before Discount: {price}")
print(f"Discount: {discount}")
print(f"Final Amount: {price-discount}")