import random
import string

# Function to generate a password based on user-defined rules
def generate_password(min_length,numbers= True, Special_characters= True):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation 

# Start with letters only, add more if selected
    characters = letters
    if numbers:
        characters += digits
    if Special_characters:
        characters += special_characters
    password = ''.join(random.choice(characters) for _ in range(min_length))

# Initialize variables for validation
    pwd = ''    
    meets_criteria = False
    has_numbers = False
    has_special_characters = False

    while not meets_criteria or len(pwd) < min_length:
        meets_criteria = True
        new_char = random.choice(characters)
        pwd+= new_char
        if new_char in digits:
            has_numbers = True
        if new_char in special_characters:
            has_special_characters = True  
        meets_criteria= True
        if numbers and not has_numbers:
            meets_criteria = False
        if Special_characters and not has_special_characters:
            meets_criteria = False
        if len(pwd) < min_length:
            meets_criteria = False
    return pwd

# Main function to interact with the user
def main(): 
    min_length = int(input("Enter the minimum length of the password: "))
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    special_characters = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(min_length, numbers, special_characters)
    print(f"Generated password: {password}")
if __name__ == "__main__":
    main()
# This code generates a random password based on user-defined criteria.
# It prompts the user for the minimum length of the password, whether to include numbers, and whether to include special characters.    