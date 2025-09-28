# perform a basic arithmetic functions 

from typing import Union

def perform_operation(num1: float, num2: float, operation: str) -> Union[float, str]:
    if not isinstance(operation, str):
        return "Error: Invalid operation. Choose add, subtract, multiply, or divide."

    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide": # handle division by zero
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation. Choose add, subtract, multiply, or divide."
    
def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

