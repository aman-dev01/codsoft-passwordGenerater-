import random
import string

# Function to generate a password
def generate_password(length):
    # Define possible characters (letters, digits, punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use random.choices to select random characters from the list
    password = ''.join(random.choices(characters, k=length))
    
    return password

# Main program
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length < 6:
            print("Password should be at least 6 characters long.")
        else:
            print(f"Generated Password: {generate_password(length)}")
    except ValueError:
        print("Please enter a valid number.")
    
    choice = input("Do you want to generate another password? (y/n): ").lower()
    if choice != 'y':
        print("Goodbye!")
        break
