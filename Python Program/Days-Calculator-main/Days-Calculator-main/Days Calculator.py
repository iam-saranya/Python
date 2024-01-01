from datetime import datetime

def days_difference(date_str1, date_str2):
    # Convert date strings to datetime objects
    date1 = datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d")

    # Calculate the difference between dates
    delta = date2 - date1

    # Return the difference in days
    return delta.days

if __name__ == "__main__":
    # Input dates in the format "YYYY-MM-DD"
    date_str1 = input("Enter the first date (YYYY-MM-DD): ")
    date_str2 = input("Enter the second date (YYYY-MM-DD): ")

    try:
        # Calculate and display the difference in days
        difference = days_difference(date_str1, date_str2)
        print(f"The difference between the two dates is {difference} days.")
    except ValueError:
        print("Invalid date format. Please use the format 'YYYY-MM-DD'.")
