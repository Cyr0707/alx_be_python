def safe_divide(numerator, denominator):
    """
    Performs division safely, handling ValueError for non-numeric input
    and ZeroDivisionError for division by zero.
    """
    try:
        # 1. Attempt to convert inputs to float. 
        # This will raise a ValueError if inputs are non-numeric.
        num = float(numerator)
        den = float(denominator)

    except ValueError:
        # Catch non-numeric input error
        return "Error: Please enter numeric values only."

    try:
        # 2. Attempt the division. 
        # This will raise a ZeroDivisionError if the denominator is 0.
        result = num / den
        
    except ZeroDivisionError:
        # Catch division by zero error
        return "Error: Cannot divide by zero."
    
    else:
        # If no exceptions were raised in the second try block
        return f"The result of the division is {result}"

# Note: The main logic (try-except structure) is placed inside 
# the function to be imported.
