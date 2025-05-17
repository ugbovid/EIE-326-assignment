# Function to encrypt the message
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97  # Uppercase or lowercase
            # Shift the character and wrap around using modulo
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

# Function to decrypt the message
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Decrypt by reversing the shift

# Program starts here
print("Welcome to the Caesar Cipher Program!")
message = input("Enter the message to encrypt: ")
shift = int(input("Enter the shift value (e.g., 3): "))

# Encrypt the message
encrypted_message = caesar_encrypt(message, shift)
print(f"\nEncrypted Message: {encrypted_message}")

# Decrypt the message
decrypted_message = caesar_decrypt(encrypted_message, shift)
print(f"Decrypted Message: {decrypted_message}")