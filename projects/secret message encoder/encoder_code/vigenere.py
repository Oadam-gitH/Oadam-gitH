
import string

message = input("enter a message to encode: ")
key = input("enter a key ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = alphabet.upper()

if key == "" or not key.isalpha():
    print("error, Key must contain letters only")

else:
    encoded = ""
    key_index = 0

    for letter in message:
        if letter in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            position = alphabet.index(letter)

            new_position = (position + shift) % 26
            encoded = encoded + alphabet[new_position]

            key_index = key_index + 1

        elif letter in alphabet_upper:
            shift = alphabet.index(key[key_index % len(key)])
            position = alphabet_upper.index(letter)

            new_position = (position + shift) % 26
            encoded = encoded + alphabet_upper[new_position]

            key_index = key_index + 1

        else:
            encoded = encoded + letter

    print("encoded message:", encoded)
    print("jey:", key)
