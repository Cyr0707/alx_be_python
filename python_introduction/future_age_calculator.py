# The year difference to calculate the future age (2050 - 2023 = 27 years)
YEARS_TO_ADD = 27

# 1. Prompt the user for their current age and store the input.
# The input is immediately converted to an integer (int) for calculation.
try:
    current_age = int(input("How old are you? "))
except ValueError:
    # Handle non-integer input gracefully, though the prompt assumes valid input
    print("Invalid input. Please enter a whole number for your age.")
    exit()

# 2. Calculate the future age in the year 2050
future_age = current_age + YEARS_TO_ADD

# 3. Print the result in the required format
print(f"In 2050, you will be {future_age} years old.")
