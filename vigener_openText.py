def vigenere_encrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = alphabet.index(key)
    encrypted_text = ''
    for i, symb in enumerate(text):
        if symb in alphabet:
            enc_symb = (alphabet.index(symb) + key) % 26
            encrypted_text += alphabet[enc_symb]
            key = alphabet.index(text[i])
        else:
            encrypted_text += symb
    return encrypted_text

def vigenere_decrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = alphabet.index(key)
    decrypted_text = ''
    for i, symb in enumerate(text):
        if symb in alphabet:
            dec_symb = (alphabet.index(symb) - key) % 26
            decrypted_text += alphabet[dec_symb]
            key = dec_symb
        else:
            decrypted_text += symb
    return decrypted_text

text = input("Введите открытый текст: ")
key = input("Введите ключ: ")

encrypted_text = vigenere_encrypt(text, key)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = vigenere_decrypt(input("Введите зашифрованный текст: "), input("Введите ключ: "))
print("Расшифрованный текст:", decrypted_text)
