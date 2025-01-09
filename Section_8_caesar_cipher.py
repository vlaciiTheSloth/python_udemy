import string

alphabet = list(string.ascii_lowercase)
should_continue = True

def caesar(encode_or_decode, original_text, shift_amount):
        output_text = ""
        if encode_or_decode == "decode":
            shift_amount *= -1

        for character in original_text:
            if character not in alphabet:
                  output_text += character
            else:
                shifted_position = alphabet.index(character) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
                
        print(f"Here is the {encode_or_decode}d result: {output_text}")


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(encode_or_decode = direction, original_text = text, shift_amount = shift)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye!")