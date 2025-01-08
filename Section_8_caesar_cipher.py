import string

alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for character in original_text:
        shifted_position = alphabet.index(character) + shift_amount
        shifted_position %= len(alphabet)
        encrypted_text += alphabet[shifted_position]
    print(f"Encypted text:{encrypted_text}")

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for character in original_text:
        shifted_position = alphabet.index(character) - shift_amount
        decrypted_text += alphabet[shifted_position]
    print(f"Decrypted text: {decrypted_text}")

def caesar(method, original_text, shift_amount):
    if method == "encode":
        encrypted_text = ""
        for character in original_text:
            shifted_position = alphabet.index(character) + shift_amount
            shifted_position %= len(alphabet)
            encrypted_text += alphabet[shifted_position]
        print(f"Encypted text: {encrypted_text}")
    elif method == "decode":
         decrypted_text = ""
         for character in original_text:
            shifted_position = alphabet.index(character) - shift_amount
            decrypted_text += alphabet[shifted_position]
         print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid input.")

#encrypt(original_text = text, shift_amount = shift)
#decrypt(original_text = text, shift_amount = shift)
caesar(method = direction, original_text = text, shift_amount = shift)
