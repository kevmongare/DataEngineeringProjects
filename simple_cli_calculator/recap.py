number1 = float(input("Enter The first number:"))
number2 = float(input("Enter the Second number:"))

operator = input(("Enter your the operation youd like to do( + , - , / , *)"))

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "/":
    result = number1 / number2
elif operator == "*":
    result = number1 * number2
else:
    result="Invalid Query"
print(result)