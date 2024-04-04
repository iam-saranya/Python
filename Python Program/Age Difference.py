from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def age_difference(birthdate1, birthdate2):
    age1 = calculate_age(birthdate1)
    age2 = calculate_age(birthdate2)
    age_diff = abs(age1 - age2)
    return age_diff

# Input birthdates from the user
def input_birthdate():
    while True:
        try:
            birthdate_str = input("Enter birthdate (YYYY-MM-DD), or 'quit' to exit: ")
            if birthdate_str.lower() == 'quit':
                return None
            birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
            return birthdate
        except ValueError:
            print("Invalid input. Please enter the date in the format YYYY-MM-DD.")

while True:
    print("\nEnter birthdate for Person 1:")
    birthdate1 = input_birthdate()
    if birthdate1 is None:
        break

    print("\nEnter birthdate for Person 2:")
    birthdate2 = input_birthdate()
    if birthdate2 is None:
        break

    difference = age_difference(birthdate1, birthdate2)
    print("The age difference between the two individuals is:", difference, "years")

print("Exiting the program.")
