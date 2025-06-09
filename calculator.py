import datetime

# Function to log calculations
def log_operation(operation, result):
    with open("calculator_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {operation} = {result}\n")

# Main calculator function
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select operation: +  -  *  /  %  ^")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, %, ^): ")
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Error: Please enter valid numbers.")
        return

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

    print(f"✅ Result: {result}")
    log_operation(f"{num1} {op} {num2}", result)

# Run the calculator
calculator()
