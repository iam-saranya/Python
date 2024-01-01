import random
import string

def generate_password(length=12):
    # Define character sets for password generation
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure the password length is at least 4 characters
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    # Generate a password with at least one character from each set
    password = random.choice(uppercase_letters) + random.choice(lowercase_letters) + random.choice(digits) + random.choice(special_characters)

    # Fill the remaining length with random characters from all sets
    for _ in range(length - 4):
        password += random.choice(all_characters)

    # Shuffle the password to mix characters
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

# Example: Generate a password of length 16
password = generate_password(16)
print("Generated Password:", password)

#Certainly! Below is a simple password generator program in Python. This program uses the random module to generate random passwords with a combination of uppercase letters, lowercase letters, digits, and special characters.
#You can customize the length of the password by providing a different value to the generate_password function. Just be sure the length is reasonable for your use case. The example above generates a password of length 16. Feel free to adjust the length or character sets based on your specific requirements.
