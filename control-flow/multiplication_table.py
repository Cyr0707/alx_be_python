# multiplication_table.py
# Objective: Use a for loop to generate and print the multiplication table for a given number.

def generate_multiplication_table():
    """
    Prompts the user for a number and prints its multiplication table from 1 to 10
    using a for loop.
    """
    # 1. Prompt User for a Number
    while True:
        try:
            # Use input() to get the number and cast it to an integer
            number_input = input("Enter a number to see its multiplication table: ")
            number = int(number_input)
            break  # Exit the loop if conversion is successful
        except ValueError:
            # Handle non-numeric input gracefully
            print("Invalid input. Please enter a valid whole number.")
            # Continue the loop to prompt the user again

    print(f"\nMultiplication table for {number}:")

    # 2. Generate and Print the Multiplication Table (from 1 to 10 inclusive)
    # The range function goes up to, but does not include, the stop value,
    # so we use range(1, 11) to include 10.
    for i in range(1, 11):
        # Calculate the product
        product = number * i

        # Print each line in the required format: "X * Y = Z"
        print(f"{number} * {i} = {product}")

# Execute the main function
if __name__ == "__main__":
    generate_multiplication_table()
