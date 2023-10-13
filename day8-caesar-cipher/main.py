direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    finalText = ""  # Placeholder for the final encrypted text
    for x in range(len(text)):
        char = text[x]
        if char.isupper():
            finalText += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            finalText += chr((ord(char) + shift - 97) % 26 + 97)

    return finalText

# Decoding function
def decrypt(text, shift):
    finalText = ""  # Placeholder for the final encrypted text
    for x in range(len(text)):
        char = text[x]
        if char.isupper():
            finalText += chr((ord(char) + (26 - shift) - 65) % 26 + 65)
        else:
            finalText += chr((ord(char) + (26 - shift) - 97) % 26 + 97)

    return finalText

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction.lower()[0] == "e":
    final = encrypt(text, shift)
    print(final)
else:
    final = decrypt(text, shift)
    print(final)