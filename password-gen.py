import random
import string
import pyperclip  # Import the pyperclip library

# Define/Ask the user what character sets for lowercase, uppercase, numbers, and special characters
lowercase_chars = string.ascii_lowercase
uppercase_chars = string.ascii_uppercase
numeric_chars = string.digits
special_chars = "!@#$%^&*()"

# Gather user preferences for character sets
include_lowercase = input("Include lowercase letters (y/n): ").strip().lower() == 'y'
include_uppercase = input("Include uppercase letters (y/n): ").strip().lower() == 'y'
include_numbers = input("Include numbers (y/n): ").strip().lower() == 'y'
include_special = input("Include special characters (y/n): ").strip().lower() == 'y'

# Ask the user for the desired length of the password
while True:
    try:
        password_length = int(input("Enter the desired password numerical length: "))
        if password_length <= 0:
            print("Please enter a positive password length.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Create a character set based on user preferences
selected_chars = ""
if include_lowercase:
    selected_chars += lowercase_chars
if include_uppercase:
    selected_chars += uppercase_chars
if include_numbers:
    selected_chars += numeric_chars
if include_special:
    selected_chars += special_chars

# Check if any character set was selected
if not selected_chars:
    print("Please select at least one character set.")
else:
    password = "".join(random.choice(selected_chars) for _ in range(password_length))
    print(f"Your password is: {password}")

    # Copy the generated password to the clipboard
    pyperclip.copy(password)
    print("The password has successfully been copied to your clipboard.")
