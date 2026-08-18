#counting "a" in a string
name = input("Enter your name:")
target = input("Enter a character to count:")
def count_freq(name,target):
    count = 0
    for i in name:
        if i == target:
            count += 1
    print(f"The number of times a is repeated is :{count}")
count_freq(name,target)