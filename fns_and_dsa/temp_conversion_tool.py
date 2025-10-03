# temp_conversion_tool.py
# Objective: Illustrate variable scope using global variables for temperature conversion factors.

# Define Global Conversion Factors
# The factor for converting Fahrenheit to Celsius: C = (F - 32) * (5/9)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
# The factor for converting Celsius to Fahrenheit: F = C * (9/5) + 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global factor for conversion: C = (F - 32) * (5/9)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global factor for conversion: F = C * (9/5) + 32
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    """
    Handles user interaction, input validation, and calls the conversion functions.
    """
    
    # 1. Prompt for Temperature
    while True:
        temp_input = input("Enter the temperature to convert: ")
        try:
            temperature = float(temp_input)
            break # Exit loop if conversion to float is successful
        except ValueError:
            # Raise a specific error message for invalid numeric input
            print("Invalid temperature. Please enter a numeric value.")
            # Continue loop to ask for input again

    # 2. Prompt for Unit
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ('C', 'F'):
            break # Exit loop if unit is valid
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # 3. Perform Conversion and Display Result
    if unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")

if __name__ == "__main__":
    main()
