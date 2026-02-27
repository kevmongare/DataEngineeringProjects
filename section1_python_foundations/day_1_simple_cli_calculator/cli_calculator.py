# This is a CLI calculator
num1 = float(input("Enter The first Number: "))
num2 = float(input("Enter The Second Number: "))
operator = input("Enter the Calculation You'd Like to Do +, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = "Error: Division by zero" if num2 == 0 else num1 / num2
else:
    result = "Invalid operator"

# 3. Output
print(f"Result: {result}")