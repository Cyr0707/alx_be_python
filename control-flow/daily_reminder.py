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

    # Initialize the base reminder message
    base_message = f"Note: '{task}' is a {priority} priority task."

    # 2. Process the Task Based on Priority using Match Case
    match priority:
        case "high":
            # High priority requires immediate focus regardless of time-bound status
            prefix = "Reminder: "
            # Set a stronger call to action for high priority tasks
            action_phrase = "Focus on completing this task first."
        case "medium":
            prefix = "Reminder: "
            action_phrase = "Plan to tackle this task soon."
        case "low":
            prefix = "Note: "
            action_phrase = "Consider completing it when you have free time."
        # The 'low' case serves as the catch-all for validated input, but a
        # redundant default case is good practice if validation was weak.
        case _:
            prefix = "Error: "
            action_phrase = "Priority level could not be determined."

    # Combine prefix and action phrase for the base reminder
    final_reminder = f"{prefix}'{task}' is a {priority} priority task. {action_phrase}"


    # 3. Use an if statement to modify the reminder if the task is time-bound.
    if time_bound == "yes":
        # Overwrite the action phrase to emphasize immediacy
        immediate_action = "that requires immediate attention today!"
        final_reminder = f"Reminder: '{task}' is a {priority} priority task {immediate_action}"
    
    # 4. Provide a Customized Reminder
    print("\n" + final_reminder)


# Execute the main function
if __name__ == "__main__":
    create_reminder()
