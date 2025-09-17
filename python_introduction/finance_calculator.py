# Define the annual interest rate
annual_interest_rate = 0.05
months_in_year = 12

# --- User Input ---
try:
    # Prompt for monthly income and convert to a float for potential decimal values
    monthly_income = float(input("Enter your monthly income: "))

    # Prompt for monthly expenses and convert to a float
    monthly_expenses = float(input("Enter your total monthly expenses: "))

except ValueError:
    print("\nError: Please enter valid numerical values for income and expenses.")
    exit()

# --- Calculate Monthly Savings ---
monthly_savings = monthly_income - monthly_expenses

# --- Project Annual Savings ---

# 1. Calculate total savings over a year without interest
annual_savings_base = monthly_savings * months_in_year

# 2. Calculate the simple interest earned on the base savings
# Interest is calculated as: Annual Base Savings * Interest Rate
interest_earned = annual_savings_base * annual_interest_rate

# 3. Calculate the projected savings after one year (Base + Interest)
projected_savings = annual_savings_base + interest_earned

# --- Output Results ---

# Use f-strings and formatting to display currency values clearly
print(f"\nYour monthly savings are ${monthly_savings:,.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:,.2f}.")
