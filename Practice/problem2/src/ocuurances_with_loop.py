#counting "a" in a string

def count_freq(name,target):
    count = 0
    for i in name:
        if i == target:
            count += 1
    print(f"The number of times a is repeated is :{count}")
while True:
    name = input("Enter your name or enter no to exit:").strip().lower()
    
    if name == "no":
        break
    else:
        target = input("Enter a character to count:")
        count_freq(name,target)