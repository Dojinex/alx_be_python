from datetime import datetime, timedelta


def display_current_datetime():
    # Save the current date in a variable
    current_date = datetime.now()

    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {formatted_datetime}")

    # Return the current date so it can be reused
    return current_date


def calculate_future_date(current_date):
    # Prompt the user for number of days
    days_input = input("Enter the number of days to add to the current date: ")

    try:
        number_of_days = int(days_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Calculate future date
    future_date = current_date + timedelta(days=number_of_days)

    # Format and print the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate future date
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
