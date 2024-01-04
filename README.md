# Vernam Encryption Python Program

This Python program is designed to encrypt and decrypt texts using the Vernam encryption method. Vernam encryption is based on the principle of using a randomly generated key of the same length as the text.

## How to Use

The program contains two main functions: `vernam_cipher_word` and `vernam_decipher_word`. These are used to encrypt and decrypt text, respectively.

```python
# Example Usage:
from vernam_cipher import vernam_cipher_word, vernam_decipher_word, generate_key

# Creating plaintext and a key
plaintext = "MEETINGplaceBELGIUM"
keyphrase = generate_key(len(plaintext))

# Encrypting the text
cipherText = vernam_cipher_word(plaintext, keyphrase)
print(f"Encrypted Text: {cipherText}")

# Decrypting the text
decryptedText = vernam_decipher_word(cipherText, keyphrase)
print(f"Decrypted Text: {decryptedText}")
