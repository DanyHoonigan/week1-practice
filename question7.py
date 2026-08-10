values = [10,10,20,20,20,30,10,10,40]
new_values = []
for i in values:
    if i not in new_values:
        new_values.append(i)
print(f"Original List: {values}")
print(f"Result: {new_values}")
