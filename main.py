def vigenere_encrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_length = len(key)
    key_as_int = [alphabet.index(k) for k in key]
    encrypted_text = ''
    for i, char in enumerate(text):
        if char in alphabet:
            shift = key_as_int[i % key_length]
            encrypted_text += alphabet[(alphabet.index(char) + shift) % 26]
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_length = len(key)
    key_as_int = [alphabet.index(k) for k in key]
    decrypted_text = ''
    for i, char in enumerate(text):
        if char in alphabet:
            shift = key_as_int[i % key_length]
            decrypted_text += alphabet[(alphabet.index(char) - shift) % 26]
        else:
            decrypted_text += char
    return decrypted_text

text = input("Введите открытый текст: ")
key = input("Введите ключ: ")

encrypted_text = vigenere_encrypt(text, key)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = vigenere_decrypt(input("Введите зашифрованный текст: "), input("Введите ключ: "))
print("Расшифрованный текст:", decrypted_text)
