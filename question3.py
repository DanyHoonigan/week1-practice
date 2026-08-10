n = int(input("Enter a number: "))
for i in range(11):
    if n*i%2 == 0:
        print(f"{n} X {i} = {n*i} = Even")
    else:
        print(f"{n} X {i} = {n*i} = Odd")