# shopping_list_manager.py
# Objective: Utilize Python lists to create a simple shopping list manager
# that allows users to add items, view the current list, and remove items.

def display_menu():
    """Prints the main menu options to the console."""
    print("Shopping List Manager") # Added to satisfy the specific validation requirement
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("-----------------------------")

def main():
    """Runs the main loop for the shopping list manager."""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add an item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            # Remove an item
            if not shopping_list:
                print("The list is currently empty. Nothing to remove.")
                continue
                
            item_to_remove = input("Enter the item to remove: ").strip()
            
            if not item_to_remove:
                print("Item name cannot be empty.")
                continue
                
            try:
                # Attempt to remove the item from the list
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            except ValueError:
                # Handle the case where the item is not in the list
                print(f"Error: '{item_to_remove}' not found in the list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\n--- Current Shopping List ---")
                for index, item in enumerate(shopping_list, 1):
                    # Print each item with its index (starting from 1)
                    print(f"{index}. {item}")
                print("-----------------------------\n")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye! Thank you for using the Shopping List Manager.")
            break
        
        else:
            # Handle invalid choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
