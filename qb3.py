# Implement encryption of transposition cipher.
import numpy as np 

def encrypt(plain_text, key):
    block_size = len(key)
    while len(plain_text) % block_size != 0:
        plain_text += '*'  # Padding with '*' to make the length a multiple of block_size
    num_blocks = len(plain_text) // block_size
    cipher_matrix = []
    for i in range(num_blocks):
        block = plain_text[i * block_size:(i + 1) * block_size]
        cipher_block = [block[key[j]] for j in range(block_size)]
        cipher_matrix.append(cipher_block)
    return np.array(cipher_matrix)

def decrypt(cipher_matrix, key):
    block_size = len(key)
    num_blocks = len(cipher_matrix)
    plain_text = ""
    for i in range(num_blocks):
        cipher_block = cipher_matrix[i]
        plain_block = [''] * block_size
        # Reverse the key to get the inverse permutation
        inverse_key = [key.index(j) for j in range(block_size)]
        for j in range(block_size):
            plain_block[inverse_key[j]] = cipher_block[j]
        plain_text += ''.join(plain_block)
    return plain_text

def get_key():
    while True:
        try:
            key = input("Enter the transposition key (e.g., '3124'): ")
            key = [int(k) for k in key]
            # Check if the key is a valid permutation
            if sorted(key) == list(range(len(key))):
                return key
            else:
                print("Invalid key. Please enter a valid permutation.")
        except ValueError:
            print("Invalid input. Please enter a sequence of digits.")

plain_text = input("Enter the plain text: ")
key = get_key()
encrypted_matrix = encrypt(plain_text, key)
print("Encrypted Matrix:")
print(encrypted_matrix)

# Transpose the encrypted matrix to decrypt column-wise
decrypted_matrix = np.transpose(encrypted_matrix)
# Concatenate the columns to get the final decrypted text
decrypted_text = ''.join(decrypted_matrix.flatten())
print("Decrypted Text:", decrypted_text)

# # transposition product cipher 
# import numpy as np 

# def encrypt1(plain_text, key):
#     cipher_text = ""
#     for char in plain_text:
#         if char.isalpha():
#             if char.islower():
#                 cipher_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
#             else:
#                 cipher_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
#         elif char == ' ':
#             cipher_char = '#'
#         else:
#             cipher_char = char
#         cipher_text += cipher_char
#     return cipher_text

# def encrypt(plain_text, key):
#     block_size = len(key)
#     while len(plain_text) % block_size != 0:
#         plain_text += '*'  # Padding with '*' to make the length a multiple of block_size
#     num_blocks = len(plain_text) // block_size
#     cipher_matrix = []
#     for i in range(num_blocks):
#         block = plain_text[i * block_size:(i + 1) * block_size]
#         cipher_block = [block[key[j]] for j in range(block_size)]
#         cipher_matrix.append(cipher_block)
#     return np.array(cipher_matrix)

# def decrypt(cipher_matrix, key):
#     block_size = len(key)
#     num_blocks = len(cipher_matrix)
#     plain_text = ""
#     for i in range(num_blocks):
#         cipher_block = cipher_matrix[i]
#         plain_block = [''] * block_size
#         # Reverse the key to get the inverse permutation
#         inverse_key = [key.index(j) for j in range(block_size)]
#         for j in range(block_size):
#             plain_block[inverse_key[j]] = cipher_block[j]
#         plain_text += ''.join(plain_block)
#     return plain_text

# def get_key():
#     while True:
#         try:
#             key = input("Enter the transposition key (e.g., '3124'): ")
#             key = [int(k) for k in key]
#             # Check if the key is a valid permutation
#             if sorted(key) == list(range(len(key))):
#                 return key
#             else:
#                 print("Invalid key. Please enter a valid permutation.")
#         except ValueError:
#             print("Invalid input. Please enter a sequence of digits.")

# plain_text = input("Enter the plain text: ")
# key = int(input("Enter the key for encryption/decryption: "))
# encrypted_text = encrypt1(plain_text, key)
# print("Encrypted Text: ", encrypted_text)

# key = get_key()
# encrypted_matrix = encrypt(encrypted_text, key)
# decrypted_text = decrypt(encrypted_matrix, key)
# print("Encrypted Matrix:")
# print(encrypted_matrix)

# # Transpose the encrypted matrix to decrypt column-wise
# decrypted_matrix = np.transpose(encrypted_matrix)
# # Concatenate the columns to get the final decrypted text
# decrypted_text = ''.join(decrypted_matrix.flatten())
# print("Decrypted Text:", decrypted_text)
# print("Original Text:", plain_text)
