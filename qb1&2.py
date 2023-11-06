# Implement encryption and decryption of the Mono-alphabetic Substitution Cipher 
def monoalphabetic_substitution_cipher(text, key):
    ciphertext = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            if char == " ":
                ciphertext += "#"
            else:
                ciphertext += char
    return ciphertext

def decrypt_monoalphabetic_substitution_cipher(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            if char == "#":
                decrypted_text += ""
            else:
                decrypted_text += char

plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key (an integer between 1-25): "))
ciphertext = monoalphabetic_substitution_cipher(plaintext, key)
print("Ciphertext:", ciphertext)

#Implement Frequency analysis method for a given Plain Text. 
# option = input("Do you want to decrypt the text? (Y/N): ")
# if option.upper() == "Y":
#     decrypted_text = decrypt_monoalphabetic_substitution_cipher(ciphertext, key)
#     print("Decrypted Text:", decrypted_text)

# Frequency calculation and percentage printing
# freq = {}
# total_alphabets = sum(1 for char in plaintext)
# for i in plaintext:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print("\nFrequency of each alphabet:")
# for alphabet, count in freq.items():
#     frequency_percentage = float((count / total_alphabets) * 100)
#     print(f"{alphabet}: {round(frequency_percentage, 2)}%")
