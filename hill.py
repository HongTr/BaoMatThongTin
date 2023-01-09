import numpy as np

def hill_cipher(text, key, mode):
    # make sure the key is invertible
    det = int(round(np.linalg.det(key)))
    if det == 0:
        raise ValueError("The key is not invertible.")

    # make sure the key is of the correct size
    # n = int(np.sqrt(len(key)))
    # if len(key) != n**2:
    #     raise ValueError("The key is not a square matrix.")

    # make sure the text is a multiple of the key size
    # if len(text) % n != 0:
    #     raise ValueError("The length of the text is not a multiple of the key size.")

    # split the text into blocks of size n
    n = len(key[0])
    blocks = [text[i:i+n] for i in range(0, len(text), n)]
    print("block = ", blocks)
    # convert the blocks and key to numerical form
    #key = np.array(key).reshape(n, n)
    if mode == "encrypt":
        key = np.mod(key, 26)
    blocks = np.array([ord(c) - ord('a') for c in text]).reshape(-1, n)
    # encrypt or decrypt the blocks
    if mode == "encrypt":
        encrypted = np.array([np.mod(np.dot(key, block), 26) for block in blocks])
    elif mode == "decrypt":
        inverted_key = np.linalg.inv(key)
        inverted_key = np.mod(inverted_key, 26)
        encrypted = np.mod(np.dot(blocks, inverted_key), 26)

    # convert the encrypted blocks back to text
    print("encrypt = ", encrypted)
    encrypted = "".join([chr(int(c) + ord('A')) for c in encrypted.flatten()])

    return encrypted

def insert_key(key):
    key = key.split(" ")
    matrix = []
    index = 0
    length_row = int(np.sqrt(len(key)))
    print("Length: ", length_row)
    while(1):
        row = []
        for i in range(length_row):
            row.append(int(key[index]))
            index += 1
        matrix.append(row)
        if index == len(key):
            break
    return np.array(matrix)

text = input("Insert text: ")
key = input("Insert key: ")
key = insert_key(key)
#print("dim = ", key.size)
    
encrypted = hill_cipher(text, key, "encrypt")
print(encrypted)
