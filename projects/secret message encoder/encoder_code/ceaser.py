message = input("enter a message to encode: ")

key = 3

encoded = ""

for letter in message:
    if letter.isalpha():
        new_letter = chr(ord(letter) + key)
        encoded = encoded + new_letter
    else:
        encoded = encoded + letter

print("encoded message:", encoded)
