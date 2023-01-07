def vernam_cipher_encrypt(plaintext, key):
    # Convert plaintext and key to lists of ASCII values
    plaintext_ascii = [ord(c) for c in plaintext]
    key_ascii = [ord(c) for c in key]
    # XOR the plaintext and key
    ciphertext = [p ^ k for p, k in zip(plaintext_ascii, key_ascii)]

    # Convert the resulting list of ASCII values to a string
    return ''.join([chr(c) for c in ciphertext])

def vernam_cipher_decrypt(ciphertext, key):
    # Convert ciphertext and key to lists of ASCII values
    ciphertext_ascii = [ord(c) for c in ciphertext]
    key_ascii = [ord(c) for c in key]

    # XOR the ciphertext and key
    plaintext = [c ^ k for c, k in zip(ciphertext_ascii, key_ascii)]

    # Convert the resulting list of ASCII values to a string
    return ''.join([chr(p) for p in plaintext])

text = input("Input text: ")
key = input("Input key: ")
ciphertext = vernam_cipher_encrypt(text, key)
print(f"Ma hoa: {ciphertext}")

plaintext = vernam_cipher_decrypt(ciphertext, key)
print(f"Giai ma: {plaintext}")