
import random

message = input("enter a message to encode: ")

key = random.randint(1, 25)

encoded = ""

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = alphabet.upper()

for letter in message:
    if letter in alphabet:
        position = alphabet.index(letter)
        new_position = (position + key) % 26
        encoded = encoded + alphabet[new_position]

    elif letter in alphabet_upper:
        position = alphabet_upper.index(letter)
        new_position = (position + key) % 26
        encoded = encoded + alphabet_upper[new_position]

    else:
        encoded = encoded + letter

print("encoded message:", encoded)
print("ey:", key)
