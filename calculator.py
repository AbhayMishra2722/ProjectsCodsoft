# calculator.py

# Simple Calculator

# Prompt the user to enter two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Prompt the user to select an operation
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# Perform calculation based on user choice
if choice == '1':
    result = num1 + num2
    print("Result: ", result)
elif choice == '2':
    result = num1 - num2
    print("Result: ", result)
elif choice == '3':
    result = num1 * num2
    print("Result: ", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid input. Please select a valid operation.")
