# rsa cryptosystem
import math
import random

primes = set()
public_key = None
private_key = None
n = None
sieve = [True] * 250
sieve[0] = False
sieve[1] = False

# Fill the primes set using the Sieve of Eratosthenes algorithm
def primefiller():
    for i in range(2, 250):
        if sieve[i]:
            primes.add(i)
            for j in range(i * 2, 250, i):
                sieve[j] = False

def pickrandomprime():
    global primes
    k = random.randint(0, len(primes) - 1)
    it = iter(primes)
    for _ in range(k):
        next(it)
    ret = next(it)
    primes.remove(ret)
    return ret

def setkeys():
    global public_key, private_key, n
    primel = pickrandomprime()
    prime2 = pickrandomprime()
    n = primel * prime2
    fi = (primel - 1) * (prime2 - 1)
    e = 2
    while True:
        if math.gcd(e, fi) == 1:
            break
        e += 1
    public_key = e
    d = 2
    while True:
        if (d * e) % fi == 1:
            break
        d += 1
    private_key = d

# To encrypt the given number
def encrypt(message):
    global public_key, n
    e = public_key
    encrypted_text = 1
    while e > 0:
        encrypted_text *= message
        encrypted_text %= n
        e -= 1
    return encrypted_text

# To decrypt the given number
def decrypt(encrypted_text):
    global private_key, n
    d = private_key
    decrypted = 1
    while d > 0:
        decrypted = (decrypted * encrypted_text) % n
        d -= 1
    return decrypted

# First converting each character to its ASCII value and then encoding it, then decoding the number to get the ASCII and converting it to a character
def encoder(message):
    encoded = []
    for letter in message:
        encoded.append(encrypt(ord(letter)))  # Corrected the missing closing parenthesis here
    return encoded

def decoder(encoded):
    s = ""
    for num in encoded:
        s += chr(decrypt(num))
    return s

if __name__ == '__main__': 
    primefiller()
    setkeys()
    message = "Vikhyat Rai 121A3042"
    coded = encoder(message)
    print("Initial message:")
    print(message)
    print("\n\nThe encoded message (encrypted by public key)\n")
    print(" ".join(str(p) for p in coded))
    print("\n\nThe decoded message (decrypted by private key)\n")
    print(decoder(coded))