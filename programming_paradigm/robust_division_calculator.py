# robust_division_calculator.py
def safe_divide(numerator, denominator):
    """
    Safely divides two values with error handling for:
    - Non-numeric inputs
    - Division by zero
    """
    try:
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
