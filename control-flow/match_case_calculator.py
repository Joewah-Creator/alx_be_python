# prompt the user to enter two numbers and select an operation

def main():
    # Prompt user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask for the operation
    operation = input("Choose the operation (+, -, *, /): ")

    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _: # Default case (if user entered something invalid)
            print("Invalid operation selected.")

if __name__ == "__main__":
    main()
