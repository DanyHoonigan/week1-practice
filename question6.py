expenses = [250,1200,450,800,150,2000,350]
total = 0
count = 0
for i in expenses:
    total += i
    count = count+1
average = total/count
minimum = min(expenses)
maximum = max(expenses)
above = 0
below = 0
for i in expenses:
    if i >500:
        above += 1
    else:
        below += 1
    print(f"Total Expenses: {total}")
    print(f"Average Expenses: {average:.2f}")
    print(f"Highest Expenses: {maximum}")
    print(f"Lowest Expense: {minimum}")
    print(f"Number of Expenses above ₹500: {above}")
    print(f"Number of expenses Below or Equal to ₹500: {below}")
