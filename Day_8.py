print("Simple Calculator")
print("Operations: +  -  *  /")

# Input numbers and operator
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Calculation using if-elif-else
if operator == '+':
    print("Result:", num1 + num2)

elif operator == '-':
    print("Result:", num1 - num2)

elif operator == '*':
    print("Result:", num1 * num2)

elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero.")

else:
    print("Invalid operator")
