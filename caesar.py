def caesar_cipher_encrypt(plaintext, n, k):
    result = ""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):  #if the text[i] is in upper case
            result=result+chr(((ord(char)-65)*n+k) %26+65)
        else:
            result=result+chr(((ord(char)-97)*n+k) %26+97)
    return result

text = input("Input text: ")
n = int(input("n = "))
k = int(input("k = "))
ciphertext = caesar_cipher_encrypt(text, n, k)
print(f"Ma hoa: {ciphertext}")
