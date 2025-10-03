# match_case_calculator.py

# This script demonstrates the use of the Python 3.10+ match-case statement 
# to handle multiple operation choices in a simple calculator.

def run_calculator():
    """
    Prompts the user for two numbers and an operation, then uses match-case 
    to execute the calculation and display the result immediately.
    """
    
    try:
        # 1. Prompt for User Input (Numbers)
        num1_input = input("Enter the first number: ")
        num2_input = input("Enter the second number: ")
        
        # Convert input to floating-point numbers to handle decimals
        num1 = float(num1_input)
        num2 = float(num2_input)
        
        # 2. Ask for the operation
        operation = input("Choose the operation (+, -, *, /): ").strip()
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # 3. Perform the Calculation and Output Using Match Case
    match operation:
        case '+':
            result = num1 + num2
            # Output the Result directly
            print(f"The result is {result}")
            
        case '-':
            result = num1 - num2
            # Output the Result directly
            print(f"The result is {result}")
            
        case '*':
            result = num1 * num2
            # Output the Result directly
            print(f"The result is {result}")
            
        case '/':
            # Handle division by zero gracefully
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                # Output the Result directly
                print(f"The result is {result}")
                
        case _:
            # Default case for unexpected operation input
            print(f"Invalid operation '{operation}'. Please choose one of +, -, *, /.")

# Run the calculator function
if __name__ == "__main__":
    run_calculator()
