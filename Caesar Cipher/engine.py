alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message, shiftamt):
    encrypted_message = ""
    for letter in message:
        if letter in alphabet:
            letter_pos = alphabet.index(letter)
            encrypted_message += alphabet[(letter_pos + shiftamt)%26]
        else:
            encrypted_message += letter

    print(f"Your encrypted message is: {encrypted_message}")

def decrypt(message, shiftamt):
    decrypted_message = ""
    for letter in message:
        if letter in alphabet:
            letter_pos = alphabet.index(letter)
            decrypted_message += alphabet[letter_pos - shiftamt]
        else:
            decrypted_message += letter
    print(f"Your encrypted message is: {decrypted_message}")
