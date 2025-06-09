import datetime

# Function to log calculations with timestamp
def log_operation(operation, result):
    with open("calculator_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {operation} = {result}\n")

# Main calculator function
def calculator():
    print("📟 Welcome to the Enhanced Python Calculator!")
    print("Available operations: +  -  *  /  %  ^")

    # Get user input
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, %, ^): ")
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Error: Please enter valid numbers.")
        return

    # Perform operation
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("❌ Error: Division by zero!")
            return
    elif op == "%":
        result = num1 % num2
    elif op == "^":
        result = num1 ** num2
    else:
        print("❌ Invalid operator!")
        return

    # Output result and log it
    print(f"✅ Result: {result}")
    log_operation(f"{num1} {op} {num2}", result)

# Run the calculator
calculator()
