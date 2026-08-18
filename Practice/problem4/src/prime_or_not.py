def is_prime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
        else:
            return True
while True:
    number = int(input("Enter a number or -1 to exit"))
    if number == -1:
        break
    else:
        print(f"{'Prime' if is_prime(number) else 'Not Prime'}")
