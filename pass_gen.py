import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if is_unique(password):
            return password

def is_unique(password):
    # Check if the password has at least one lowercase, one uppercase, one digit, and one punctuation
    return (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password))

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length should be greater than zero. Please enter a valid length.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    length = get_password_length()
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
