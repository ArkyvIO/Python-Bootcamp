# Day 8: Caesar Cipher - Function Parameters and Simple Encryption

## Project Description

The Day 8 project revolves around implementing a Caesar Cipher, a simple encryption technique, utilizing function parameters in Python. The Caesar Cipher involves shifting each letter in a message by a fixed number of positions down the alphabet. This project aims to demonstrate the usage of function parameters to achieve encryption and decryption functionalities.

## Key Concepts Applied

- **Function Parameters:** Utilizing function parameters in Python to pass arguments and manage encryption/decryption processes.
- **Caesar Cipher Encryption:** Implementing the Caesar Cipher algorithm for basic text encryption and decryption.
- **Simple Encryption Techniques:** Exploring and applying fundamental encryption techniques using shifts within the alphabet.

## Project Progress

- [x] Define the structure and objectives of the Caesar Cipher project
- [x] Implement function for Caesar Cipher encryption
- [x] Develop decryption function
- [x] Complete the project for both encryption and decryption functionalities

## Code Snippet - Caesar Cipher Encryption Function

```python
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
