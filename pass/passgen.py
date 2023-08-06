import random
import string


def generate_password(length, include_digits, include_special_chars):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = " ".join(random.choice(characters) for i in range(length))
    return password


def main():
    print("                Password Generator             ")
    length = int(input("Enter desired password length: "))
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, include_digits, include_special_chars)
    print(f"Generated Password: {password}")



main()
