values = [10,10,20,20,20,30,10,10,40]
new_values = []
for i in range(len(values)):
    if values[i]!= values[i-1] :
        new_values.append(values[i])
print(f"Original List: {values}")
print(f"Result: {new_values}")
