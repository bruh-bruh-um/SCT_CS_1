def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result
def decrypt(text, shift):
    return encrypt(text, -shift)
print("=== Caesar Cipher Program ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value (1-25): "))
print("\nChoose an option:")
print("1. Encrypt")
print("2. Decrypt")
choice = input("Enter your choice (1 or 2): ")
if choice == '1':
    encrypted_text = encrypt(message, shift)
    print(f"\nEncrypted message: {encrypted_text}")
elif choice == '2':
    decrypted_text = decrypt(message, shift)
    print(f"\nDecrypted message: {decrypted_text}")
else:
    print("\nInvalid choice. Please run the program again.")
