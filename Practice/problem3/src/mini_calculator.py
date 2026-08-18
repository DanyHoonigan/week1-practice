#function of a calculator
def mini_calculator(num1,num2,operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "//":
        return num1 // num2
    else:
        return "Invalid Operator"

while True:
    num1 = int(input("Enter a Number or -1 to exit:"))
    if num1 == -1:
        break
    else:
        num2 = int(input("Enter a Number:"))
        operator = input("Enter the operation to be made: ")
        print( mini_calculator(num1,num2,operator))