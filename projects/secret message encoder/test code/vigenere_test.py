
message = input("enter a message to encode: ")

key = "key"

encoded = ""

alphabet = "abcdefghijklmnopqrstuvwxyz"

key_index = 0

for letter in message.lower():
    if letter in alphabet:
        shift = alphabet.index(key[key_index % len(key)])
        position = alphabet.index(letter)

        new_position = (position + shift) % 26
        encoded = encoded + alphabet[new_position]

        key_index = key_index + 1

    else:
        encoded = encoded + letter

print("encoded message:", encoded)
