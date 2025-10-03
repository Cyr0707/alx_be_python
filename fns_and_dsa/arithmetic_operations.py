# arithmetic_operations.py
# Objective: Implement a function to perform arithmetic operations based on user input.

def perform_operation(num1, num2, operation):
    """
    Performs a specific arithmetic operation (add, subtract, multiply, or divide) 
    on two numbers based on the operation string.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The desired operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error message.
    """
    # Convert operation to lowercase for case-insensitive matching
    operation = operation.lower().strip()

    # Use conditional logic (if/elif/else) to perform the correct operation
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Ensure we don't divide by zero
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero."
    else:
        return "Error: Invalid operation specified. Use 'add', 'subtract', 'multiply', or 'divide'."

# Example Usage:
if __name__ == "__main__":
    
    print("--- Arithmetic Operations Demo ---")

    # Example 1: Addition
    result_add = perform_operation(10, 5, 'add')
    print(f"10 + 5 = {result_add}") # Expected: 15

    # Example 2: Subtraction
    result_subtract = perform_operation(20, 7, 'Subtract')
    print(f"20 - 7 = {result_subtract}") # Expected: 13

    # Example 3: Multiplication
    result_multiply = perform_operation(4, 6, 'multiply')
    print(f"4 * 6 = {result_multiply}") # Expected: 24

    # Example 4: Division
    result_divide = perform_operation(100, 4, 'DIVIDE')
    print(f"100 / 4 = {result_divide}") # Expected: 25

    # Example 5: Division by zero error handling
    result_zero_div = perform_operation(9, 0, 'divide')
    print(f"9 / 0 = {result_zero_div}") # Expected: Error: Cannot divide by zero.

    # Example 6: Invalid operation
    result_invalid = perform_operation(5, 5, 'power')
    print(f"5 'power' 5 = {result_invalid}") # Expected: Error: Invalid operation specified...

