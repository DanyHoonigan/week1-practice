#counting "a" in a string
name = input("Enter your name:")
def count_freq(name):
    count = 0
    for i in name:
        if i == "a":
            count += 1
    print(f"The number of times a is repeated is :{count}")
count_freq(name)