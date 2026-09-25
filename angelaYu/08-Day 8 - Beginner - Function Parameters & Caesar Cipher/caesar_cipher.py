logo = r"""
   ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
  a8"     "" ""     `Y8 a8"     "" ""     "" ""     `Y8 88P'   "Y8
  8b         ,adPPPPP88 8b         ,adPPPPP88 8b        88
  "8a,   ,aa 88,    ,88 "8a,   ,aa 88,    ,88 "8a,   ,aa 88
   `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8  `"8bbdP"Y8 88
             88             88                                 88
             88             88                                 88
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            new_position = (alphabet.index(char) + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char   # keep spaces, numbers and symbols unchanged
    print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")
