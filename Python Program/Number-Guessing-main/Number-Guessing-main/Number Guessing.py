import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    attempts = 0
    while True:
        # Get user input for a guess
        user_guess = int(input("Enter your guess: "))
        
        # Increment the attempts count
        attempts += 1

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    guess_number()
