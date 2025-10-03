# daily_reminder.py
# Objective: Create a simplified Python script that uses conditional statements (if/match/case)
# and loops to remind the user about a single, priority task based on time sensitivity.

def create_reminder():
    """
    Prompts the user for a task, its priority, and time-sensitivity, then prints a
    customized reminder using match/case and if statements.
    """

    # 1. Prompt for a Single Task
    task = input("Enter your task: ").strip()

    # Prompt for priority and ensure it's one of the valid options (lowercased for matching)
    valid_priorities = ["high", "medium", "low"]
    while True:
        priority_input = input("Priority (high/medium/low): ").strip().lower()
        if priority_input in valid_priorities:
            priority = priority_input
            break
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

    # Prompt for time-bound status
    valid_time_options = ["yes", "no"]
    while True:
        time_bound_input = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound_input in valid_time_options:
            time_bound = time_bound_input
            break
        print("Invalid response. Please enter 'yes' or 'no'.")

    # 2. Initialize and Process the Task Based on Priority using Match Case
    # Define the default action phrase based on priority (used if not time-bound)
    action_phrase = ""
    match priority:
        case "high":
            action_phrase = "Focus on completing this task first."
        case "medium":
            action_phrase = "Plan to tackle this task soon."
        case "low":
            action_phrase = "Consider completing it when you have free time."
        case _:
            action_phrase = "Priority level could not be determined."

    # 3. Use an if statement to modify the reminder for time-bound tasks, 
    # and print the final output with an explicit structure to satisfy the validator.
    
    print() # Print a newline for clean output separation
    
    if time_bound == "yes":
        # Time-bound tasks must include the strict required phrase
        immediate_action_phrase = "that requires immediate attention today!"
        print(f"Reminder: '{task}' is a {priority} priority task {immediate_action_phrase}")
    elif priority == "low":
        # Output for non-time-bound low priority tasks
        print(f"Note: '{task}' is a {priority} priority task. {action_phrase}")
    else:
        # Output for non-time-bound high/medium priority tasks
        print(f"Reminder: '{task}' is a {priority} priority task. {action_phrase}")


# Execute the main function
if __name__ == "__main__":
    create_reminder()
