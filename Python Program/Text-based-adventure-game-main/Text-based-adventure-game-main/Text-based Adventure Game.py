import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a dark cave.")
    time.sleep(1)
    print("There are two paths in front of you. Which one do you choose?")
    time.sleep(1)

def choose_path():
    print("1. Take the left path.")
    print("2. Take the right path.")
    choice = input("Enter 1 or 2 to make your choice: ")
    return choice

def left_path():
    print("You chose the left path.")
    time.sleep(1)
    print("You encounter a friendly group of elves.")
    time.sleep(1)
    print("They offer you a magic potion. Do you accept?")
    time.sleep(1)
    print("1. Yes, I accept the potion.")
    print("2. No, I decline.")
    choice = input("Enter 1 or 2 to make your choice: ")
    return choice

def right_path():
    print("You chose the right path.")
    time.sleep(1)
    print("You stumble upon a treasure chest.")
    time.sleep(1)
    print("Do you open the chest?")
    time.sleep(1)
    print("1. Yes, I open the chest.")
    print("2. No, I leave it alone.")
    choice = input("Enter 1 or 2 to make your choice: ")
    return choice

def outcome(choice1, choice2):
    print("\n--- Results ---")
    time.sleep(1)

    if choice1 == '1':
        print("You accepted the potion from the elves.")
        time.sleep(1)
        print("The potion gives you magical powers!")
    else:
        print("You declined the potion from the elves.")
        time.sleep(1)
        print("You continue your journey without any magical assistance.")

    time.sleep(1)

    if choice2 == '1':
        print("You opened the treasure chest.")
        time.sleep(1)
        print("Congratulations! You found a valuable artifact.")
    else:
        print("You chose not to open the treasure chest.")
        time.sleep(1)
        print("You continue your journey without the additional treasure.")

def main():
    introduction()

    path_choice = choose_path()

    if path_choice == '1':
        elf_choice = left_path()
        treasure_choice = right_path()
    elif path_choice == '2':
        treasure_choice = right_path()
        elf_choice = left_path()

    outcome(elf_choice, treasure_choice)

if __name__ == "__main__":
    main()
