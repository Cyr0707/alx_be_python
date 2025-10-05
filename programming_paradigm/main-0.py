import sys
# Import the BankAccount class from the bank_account module
try:
    from bank_account import BankAccount
except ImportError:
    print("Error: Could not import BankAccount. Make sure bank_account.py is in the same directory.")
    sys.exit(1)


def main():
    # 1. Initialize the account with a starting balance for testing
    # Note: Subsequent command calls will not preserve changes from previous runs
    account = BankAccount(100.00) 

    # 2. Check for required arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    # 3. Parse the command line argument
    arg = sys.argv[1]
    
    # Handle the 'display' command which has no amount
    if arg == "display":
        command = "display"
        amount = None
    else:
        try:
            # Split the argument (e.g., "deposit:50")
            command, amount_str = arg.split(':')
            amount = float(amount_str)
        except ValueError:
            print("Invalid command format. Use <command>:<amount> or 'display'.")
            sys.exit(1)

    # 4. Execute the command
    print(f"Initial Balance for testing: ${account._account_balance:.2f}") # Display initial balance for context

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print(f"Insufficient funds. Attempted to withdraw: ${amount:.2f}")
    
    elif command == "display":
        account.display_balance()
    
    else:
        print("Invalid command or missing amount.")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        
    # 5. Show final balance after operation
    account.display_balance()

if __name__ == "__main__":
    main()
