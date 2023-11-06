def encrypt_columnar_transposition(text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    num_columns = len(key)
    num_rows = -(-len(text) // num_columns)

    transposition_grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    for i in range(len(text)):
        row = i // num_columns
        col = key_order[i % num_columns]
        transposition_grid[row][col] = text[i]

    ciphertext = ''
    for col in range(num_columns):
        for row in range(num_rows):
            ciphertext += transposition_grid[row][col]

    return ciphertext

def decrypt_columnar_transposition(ciphertext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    num_columns = len(key)
    num_rows = -(-len(ciphertext) // num_columns)

    transposition_grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    for i in range(len(ciphertext)):
        row = i // num_columns
        col = key_order[i % num_columns]
        transposition_grid[row][col] = ciphertext[i]

    plaintext = ''
    for row in range(num_rows):
        for col in range(num_columns):
            plaintext += transposition_grid[row][col]

    return plaintext

plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

ciphertext = encrypt_columnar_transposition(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt_columnar_transposition(ciphertext, key)
print("Decrypted text:", decrypted_text)
