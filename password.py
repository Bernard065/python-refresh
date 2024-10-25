from itertools import product
import os

def is_valid(password):
    # Ensure the first two digits are not the same and the first digit is "6"
    if password[0] != '6' or password[0] == password[1]:
        return False
    # Check if any digit repeats more than 2 times
    for digit in set(password):
        if password.count(digit) > 2:
            return False
    return True

def generate_passwords(file_path):
    # Generate all possible 6-digit combinations using digits 0-9
    digits = '0123456789'
    all_passwords = product(digits, repeat=6)
    
    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Filter and write valid passwords to the file
        for pwd in all_passwords:
            pwd_str = ''.join(pwd)
            if is_valid(pwd_str):
                file.write(pwd_str + '\n')

# Generate and write passwords to a file in the Development folder
development_folder = os.path.expanduser('~/Development')
file_path = os.path.join(development_folder, 'valid3_passwords.txt')

# Ensure the Development directory exists
if not os.path.exists(development_folder):
    os.makedirs(development_folder)

generate_passwords(file_path)
print(f"Passwords saved to {file_path}")
