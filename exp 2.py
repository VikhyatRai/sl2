# product and transposition cipher
def contains_number(string):
    return any(char.isdigit() for char in string)

def create_cipher_matrix(cipher, transpositionKey):
    matrix = []
    for i in range(0, len(cipher), transpositionKey):
        row = cipher[i:i + transpositionKey]
        if len(row) < transpositionKey:
            row += "*" * (transpositionKey - len(row))
        matrix.append(row)
    return matrix

inputString = input("Enter the input string:")
key = int(input("Enter the key:"))
cipher = ""
if not contains_number(inputString):
    for i in inputString:
        if i.isalpha():
            if i.islower():
                cipher = cipher + chr(ord("a") + (ord(i) - ord("a") + key) % 26)
            else:
                cipher = cipher + chr(ord("A") + (ord(i) - ord("A") + key) % 26)
        elif i == " ":
            cipher = cipher + "#"
        else:
            cipher = cipher + i

    print(f"Encrypted Text: {cipher}")

    decrypted_text = ""
    for i in cipher:
        if i.isalpha():
            if i.islower():
                decrypted_text = decrypted_text + chr(ord("a") + (ord(i) - ord("a") - key) % 26)
            else:
                decrypted_text = decrypted_text + chr(ord("A") + (ord(i) - ord("A") - key) % 26)
        elif i == "#":
            decrypted_text = decrypted_text + ""
        else:
            decrypted_text = decrypted_text + i
    print(f"Decrypted Text: {decrypted_text}")

    transpositionKey = int(input("Enter the Transposition Key:"))

    cipher_matrix = create_cipher_matrix(cipher, transpositionKey)
    print("Transposition Cipher:")
    for row in cipher_matrix:
        print("".join(row))

    print("Product Cipher:")
    productCipher = []
    for colIndex in range(transpositionKey):
        column = []
        for row in cipher_matrix:
            if colIndex < len(row):
                column.append(row[colIndex])
        productCipher.append("".join(column))
    print("".join(productCipher))

else:
    print("Error: Your String contains a number")
