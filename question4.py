string = input("Enter a string: ")
lower = 0
upper = 0
digit = 0
space = 0
other = 0
for i in string:
    if i in "qwertyuiopasdfghjklmnbvcxz":
        lower += 1
    elif i in "QWERTYUIOPLKJHGFDSAZXCVBNM":
        upper += 1
    elif i in "1234567890":
        digit += 1
    elif i in " ":
        space += 1
    else:
        other += 1
print(f"Uppercase Letters: {upper}")
print(f"lowercase Letters: {lower}")
print(f"Digits: {digit}")
print(f"Spaces: {space}")
print(f"Other: {other}")
