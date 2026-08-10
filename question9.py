string = input("Enter a string: ")

print(f"First 5 Characters: {string[:5]}")
print(f"Last 5 Characters: {string[-5:]}")
print(f"Characters from Index 2 to 7: {string[2:8]}")
print(f"Every Second Character: {string[::2]}")
print(f"Message in Reverse: {string[::-1]}")
print(f"Message without First and Last Character: {string[1:-1:1]}")
