# 

import sys
# Import the function from the calculator module
try:
    from robust_division_calculator import safe_divide
except ImportError:
    print("Error: Could not import safe_divide. Make sure robust_division_calculator.py is in the same directory.")
    sys.exit(1)


def main():
    """
    Reads numerator and denominator from command line arguments and 
    calls safe_divide.
    """
    # Check if exactly 3 arguments (script name + 2 numbers) were provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Arguments are passed as strings from the command line
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the robust division function
    result = safe_divide(numerator, denominator)
    
    # Print the result or the error message
    print(result)

if __name__ == "__main__":
    main()
