import datetime

# Function to log calculations with timestamp
def log_operation(operation, result):
    with open("calculator_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {operation} = {result}\n")

# Main calculator function
def calculator():
    print("📟 Welcome to the Enhanced Python Calculator!")
    print("Available operations: +  -  *  /  %  ^  (Type 'log', 'clear', or 'exit')")

    while True:
        first = input("Enter first number (or type 'log', 'clear', or 'exit'): ").lower()

        if first == "log":
            try:
                with open("calculator_log.txt", "r") as log_file:
                    print("\n--- 📄 Calculation Log ---")
                    print(log_file.read())
            except FileNotFoundError:
                print("⚠️ Log file not found.")
            continue

        elif first == "clear":
            open("calculator_log.txt", "w").close()
            print("🧹 Log cleared.")
            continue

        elif first == "exit":
            print("👋 Goodbye!")
            break

        try:
            num1 = float(first)
            op = input("Enter operator (+, -, *, /, %, ^): ")
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Error: Please enter valid numbers.")
            continue

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
                continue
        elif op == "%":
            result = num1 % num2
        elif op == "^":
            result = num1 ** num2
        else:
            print("❌ Invalid operator!")
            continue

        print(f"✅ Result: {result}")
        log_operation(f"{num1} {op} {num2}", result)

# Run the calculator
calculator()
