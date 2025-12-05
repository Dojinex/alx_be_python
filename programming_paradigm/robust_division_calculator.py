def safe_divide(numerator, denominator):
    """
    Safely performs division while handling:
    - Division by zero
    - Non-numeric input
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
