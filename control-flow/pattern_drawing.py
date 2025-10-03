# pattern_drawing.py
# Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.

def draw_square_pattern():
    """
    Prompts the user for a positive integer (size) and draws a square pattern 
    of that size using nested loops (while for rows, for for columns).
    """
    # 1. Prompt User for Pattern Size
    size = -1
    while size <= 0:
        try:
            # Use input() to get the size and cast it to an integer in one line
            size = int(input("Enter the size of the pattern: "))

            # Check if the number is positive
            if size <= 0:
                print("Size must be a positive integer.")
        except ValueError:
            # Handle non-numeric input gracefully
            print("Invalid input. Please enter a valid whole number.")

    print(f"\nDrawing a {size}x{size} square pattern:")

    # 2. Draw the Pattern using a while loop for rows and a for loop for columns
    
    # Initialize the row counter for the while loop
    current_row = 0

    # The outer WHILE loop iterates through each row of the pattern
    while current_row < size:
        # The inner FOR loop iterates through each column in the current row
        for current_col in range(size):
            # Print an asterisk without a newline character
            print("*", end="")
        
        # Print a newline character after the row is complete to move to the next line
        print()
        
        # Increment the row counter
        current_row += 1

# Execute the main function
if __name__ == "__main__":
    draw_square_pattern()
