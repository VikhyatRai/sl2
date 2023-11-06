#  playfair and vignear cipher
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

def create_playfair_key(key):
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I")  # Replace J with I
    key_set = set()
    key_matrix = []
    for char in key:
        if char not in key_set:
            key_set.add(char)
            key_matrix.append(char)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    remaining_chars = [char for char in alphabet if char not in key_set]
    for char in remaining_chars:
        if len(key_matrix) < 25:
            key_matrix.append(char)
    return [key_matrix[i:i+5] for i in range(0, len(key_matrix), 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def playfair_encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    plaintext = plaintext.replace("J", "I")  # Replace J with I
    pairs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
            pairs.append(plaintext[i] + "X")
            i += 1
        else:
            pairs.append(plaintext[i] + plaintext[i + 1])
            i += 2
    ciphertext = ""
    for pair in pairs:
        row1, col1 = find_position(key_matrix, pair[0])
        row2, col2 = find_position(key_matrix, pair[1])
        if row1 == row2:
            ciphertext += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]
    return ciphertext

def playfair_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.replace(" ", "").upper()
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(key_matrix, ciphertext[i])
        row2, col2 = find_position(key_matrix, ciphertext[i + 1])
        if row1 == row2:
            plaintext += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]
    plaintext = plaintext.replace("X", "")  # Remove any padding 'X' characters
    return plaintext

key = input("Enter the encryption key: ")
plaintext = input("Enter the plaintext: ")
key_matrix = create_playfair_key(key)

print("\nPlayfair Key Matrix:")
print_matrix(key_matrix)

ciphertext = playfair_encrypt(plaintext, key_matrix)
print("\nCiphertext:", ciphertext)

decrypted_text = playfair_decrypt(ciphertext, key_matrix)
print("\nDecrypted Text:", decrypted_text)
