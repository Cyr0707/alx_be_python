# explore_datetime.py
# Objective: Utilize Python’s datetime module to perform date and time operations.

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and displays the current date and time in a specified format.
    """
    # Part 1: Display the Current Date and Time
    current_date = datetime.now()
    
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\nCurrent date and time: {formatted_datetime}")
    # Returns the current date object for use in the next function
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days, calculates the future date, 
    and displays it in "YYYY-MM-DD" format.
    
    Args:
        current_date (datetime): The starting datetime object from which to calculate.
    """
    # Part 2: Calculate a Future Date
    
    # Loop to ensure the user enters a valid positive integer
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            if days_to_add >= 0:
                break
            else:
                print("Please enter a positive number of days.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Calculate the future date using timedelta
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {formatted_future_date}")


def main():
    # Call Part 1 to get and display the current time
    current_date = display_current_datetime()
    
    # Call Part 2 to calculate and display the future date
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
