import string
import sys

def check_password_strength(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    length = len(password)

    is_strong = length >= 8 and has_upper and has_lower and has_digit and has_special
    is_medium = (length >= 6 and 
                 ((has_upper or has_lower) and 
                 (has_digit or has_special)))

    if is_strong:
        return "Strong "
    elif is_medium:
        return "Medium "
    else:
        return "Weak"

# --- START of Script ---
print("\nWelcome to Password Strength Checker")
sys.stdout.flush()  # force print to show immediately

password = input("Enter your password: ")
strength = check_password_strength(password)

print(f"\nYour password is: {strength}")
