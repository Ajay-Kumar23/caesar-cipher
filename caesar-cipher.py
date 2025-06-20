def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    while True:
        choice = input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'q':
            print("Exiting program.")
            break
        if choice not in ['e', 'd']:
            print("Invalid choice. Try again.")
            continue

        message = input("Enter your message: ")
        while True:
            try:
                shift = int(input("Enter shift value (integer): "))
                break
            except ValueError:
