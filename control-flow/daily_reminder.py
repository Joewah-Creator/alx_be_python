# Ask the user for a task, its priority, and whether it's time-bound.
# Then give a customized reminder using match-case, if, and loops.

def main(): # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    # Use a loop to keep prompting until valid priority is entered
    while priority not in ("high", "medium", "low"):
        print("Invalid priority. Please enter high, medium, or low.")
        priority = input("Priority (high/medium/low): ").lower().strip()

    # Match-case for priority
    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task."
        case "medium":
            message = f"Reminder: '{task}' is a medium priority task."
        case "low":
            message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            message = f"Reminder: '{task}' has an unspecified priority."

    # Check if task is time-bound
    if time_bound == "yes":
        message += " It requires immediate attention today!"
    print()
    print(message)

if __name__ == "__main__":
    main()

    # Customized Reminder example

def main(): # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    # Match-case for priority
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a medium priority task.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print(f"Reminder: '{task}' has an unspecified priority.")

if __name__ == "__main__":
    main()
