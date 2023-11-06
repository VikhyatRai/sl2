# Implement encryption of Vigenère cipher.
def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.replace(" ", "")
    encrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(plain_text):
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')
            
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + key_shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + key_shift) % 26 + ord('A'))
            
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')
            
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a' if char.islower() else 'A') - key_shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('a' if char.islower() else 'A') - key_shift) % 26 + ord('A'))
            
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

plaintext = input("Enter the plaintext: ")
key = input("Enter the encryption key: ")
encrypted = vigenere_encrypt(plaintext, key)
print("Encrypted:", encrypted)

decrypted = vigenere_decrypt(encrypted, key)
print("Decrypted:", decrypted)
