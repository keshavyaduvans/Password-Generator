import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Input from the user for the desired password length
while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Generate and display the password
password = generate_password(length)
print("Generated Password:", password)
