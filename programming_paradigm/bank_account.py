# bank_account.py

class BankAccount:
    """
    A simple class to represent a bank account, demonstrating encapsulation 
    and basic banking operations.
    """
    
    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount with an optional starting balance.
        """
        if initial_balance < 0:
            # Simple validation for a non-negative starting balance
            raise ValueError("Initial balance cannot be negative.")
        self._account_balance = initial_balance  # Use '_' for convention

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the amount from the balance if funds are sufficient.
        Returns True on success, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        # Format to two decimal places for currency
        print(f"Current Balance: ${self._account_balance:.2f}")
