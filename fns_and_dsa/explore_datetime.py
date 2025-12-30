from datetime import datetime, timedelta

def display_current_datetime():
    # Part 1: Display the Current Date and Time
    current_date = datetime.now()
    # Formatting using strftime (string format time)
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    # Part 2: Calculate a Future Date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Use timedelta to represent the duration
        future_date = current_date + timedelta(days=days_to_add)
        
        # Format and print the future date
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
        return future_date
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

if __name__ == "__main__":
    # Execute Part 1
    now = display_current_datetime()
    
    # Execute Part 2
    calculate_future_date(now)
