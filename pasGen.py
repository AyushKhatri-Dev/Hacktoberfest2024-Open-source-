import random
import string

# Function to generate a random password
def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    # Define character sets
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # Special characters like !, @, #

    # Ensure the password contains at least one of each type of character
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Generate the rest of the password
    password += random.choices(all_characters, k=length-4)

    # Shuffle the result to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Main function to take user input and generate password
def main():
    print("Welcome to the Random Password Generator!")
    
    try:
        length = int(input("Enter the length of the password (minimum 4): "))
        password = generate_password(length)
        if password:
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
