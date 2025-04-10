# password_checker
EXPLANATION OF THE CODE IN DETAIL (LINE BY LINE)

import string
import sys

What it does:
string: gives us access to predefined strings like string.punctuation (all special characters like !@#$%).
sys: used here to flush the print output immediately (so you see the message before input prompt shows up).

def check_password_strength(password)
This defines a function called check_password_strength that takes one argument — the password entered by the user.

 has_upper = any(char.isupper() for char in password)
 Checks if any character in the password is uppercase (A-Z).
1)char.isupper() is True for uppercase letters.
2)any() returns True if at least one character matches.
Example: "Abc123" → has_upper = True

 has_lower = any(char.islower() for char in password)
Similar check, but for lowercase letters (a-z).
Example:"Abc123" → has_lower = True

 has_digit = any(char.isdigit() for char in password)
Checks if the password has any digits (0-9).
Example:"Abc123" → has_digit = True

has_special = any(char in string.punctuation for char in password)
Checks for special characters, like !@#$% etc.
string.punctuation is a string of all special symbols.
Example: "Abc@123" → has_special = True

length = len(password)
Stores the length of the password (number of characters) in a variable.
Example:"Abc123" → length = 6

 is_strong = length >= 8 and has_upper and has_lower and has_digit and has_special
This line sets is_strong = True only if:
Length is at least 8 and
Contains upper, lower, number, and special char
Example:"Abc@1234" → is_strong = True

 is_medium = (length >= 6 and 
                 ((has_upper or has_lower) and 
                 (has_digit or has_special)))
Checks if the password qualifies as medium strength:
At least 6 characters
Has either upper/lower and
Has either digit or special char
Example:"abc123" → is_medium = True

if is_strong:
        return "Strong"
If is_strong is True, return that it's a Strong password.

 elif is_medium:
        return "Medium"
If not strong but is_medium is True, return Medium.

 else:
        return "Weak"
If neither condition is met, it’s a Weak password

print("\nWelcome to Password Strength Checker")
sys.stdout.flush()
\n just adds a blank line before the welcome message.
sys.stdout.flush() ensures the message prints before waiting for input.

password = input("Enter your password: ")
This waits for the user to type a password and press Enter.

strength = check_password_strength(password)
Calls the function using the entered password and stores the result (Strong, etc) in strength.

print(f"\nYour password is: {strength}")
Displays the final result with a nice emoji and formatting.

**Output Example:**
Welcome to Password Strength Checker
Enter your password: Abc@1234
Your password is: Strong


