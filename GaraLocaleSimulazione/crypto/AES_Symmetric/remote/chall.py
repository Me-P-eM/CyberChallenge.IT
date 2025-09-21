from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import getStrongPrime, isPrime, bytes_to_long
from random import randint
from os import urandom
import signal
import os

signal.alarm(300)

MAX_REQUESTS = 40
FLAG = os.environ.get("FLAG", "flag{redacted}").encode()
KEY = urandom(16)

def generate_pub_key(bits=1024):
    p = getStrongPrime(bits)
    delta = randint(2**12, 2**32)
    q = p + delta
    while not isPrime(q):
        q += 1
    N = p * q
    return (N, 65537)

N, e = generate_pub_key()
aes = AES.new(KEY, AES.MODE_ECB)

FLAG_CT = []
for b in FLAG:
    enc_block = aes.encrypt(pad(bytes([b]), AES.block_size))
    ct = pow(bytes_to_long(enc_block), e, N)
    FLAG_CT.append(hex(ct))

print("[*] Welcome to AES-Symmetric Cryptography!")
print(f"N = {N}")
print(f"e = {e}")
print("FLAG_CT = [")
for block in FLAG_CT:
    print(f"  {block},")
print("]")
print(f"You have {MAX_REQUESTS} attempts to encrypt a single byte (printable only).")

for i in range(MAX_REQUESTS):
    try:
        inp = input(f"[{i+1}/{MAX_REQUESTS}] Enter a text to encrypt: ").strip()
        b = inp.encode()
        enc_block = aes.encrypt(pad(b, AES.block_size))
        ct = pow(bytes_to_long(enc_block), e, N)
        print(f"Encrypted: {hex(ct)}")
    except Exception as ex:
        print("Error:", ex)
        break

print("No more requests. Bye!")

