# daily_reminder.py

# 1. Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# 2. Process the Task Based on Priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task of unknown priority"

# 3. Modify the reminder based on time sensitivity using an if statement
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    # Providing context for non-time-bound tasks
    if priority == "high" or priority == "medium":
        reminder += ". Try to get it done soon."
    else:
        reminder += ". Consider completing it when you have free time."

# 4. Output the Customized Reminder
if time_bound == "yes":
    print(f"Reminder: {reminder}")
else:
    print(f"Note: {reminder}")
