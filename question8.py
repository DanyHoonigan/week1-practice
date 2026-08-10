employee = ("Arjun", "Developer", 4500, 3)

employee_name,designation,monthly_salary,years_of_experience = employee

annual_salary = monthly_salary*12

if years_of_experience <2:
    Bonus = 0.05*annual_salary
elif years_of_experience >2 and years_of_experience <=5:
    Bonus = 0.1*annual_salary
else:
    Bonus = 1.5*annual_salary
print(f"Employee Name: {employee_name}")
print(f"Designation: {designation}")
print(f"Experience: {years_of_experience}")
print(f"Monthly Salary: {monthly_salary}")
print(f"Annual Salary: {annual_salary}")
print(f"Bonus: {Bonus}")
print(f"Total Annual Compensation: {Bonus+annual_salary}")