from datetime import date

def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    return age

def main():
    while True:
        valid_input = False
        while not valid_input:
            try:
                birth_year = int(input("Enter your birth year: "))
                birth_month = int(input("Enter your birth month (1-12): "))
                birth_day = int(input("Enter your birth day (1-31): "))
                
                if birth_month < 1 or birth_month > 12 or birth_day < 1 or birth_day > 31:
                    print("Invalid month or day input. Please enter valid values.")
                else:
                    valid_input = True
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        
        age = calculate_age(birth_year, birth_month, birth_day)
        print("You are {} years old.".format(age))
        
        repeat = input("Do you want to calculate age again? (yes/no): ").lower()
        if repeat != 'yes':
            break

if __name__ == "__main__":
    main()
