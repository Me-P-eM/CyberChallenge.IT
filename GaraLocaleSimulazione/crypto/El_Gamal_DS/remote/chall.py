from hashlib import sha256
from Crypto.Util.number import getPrime, inverse, bytes_to_long, GCD
from sys import exit
import os
import signal

signal.alarm(300)

FLAG = os.environ.get("FLAG", "flag{redacted}").encode()

def gen_keys():
    p = getPrime(512)
    g = 2
    x = int.from_bytes(os.urandom(32), 'big') % (p - 1)
    y = pow(g, x, p)
    while True:
        k = int.from_bytes(os.urandom(32), 'big') % (p - 1)
        if 1 < k < p - 1 and GCD(k, p - 1) == 1:
            break
    return p, g, x, y, k

def mac(key: bytes, msg: bytes) -> int:
    return bytes_to_long(sha256(key + msg).digest())

def sign_msg(mac: int, p: int, g: int, x: int, k: int):
    try:
        r = pow(g, k, p)
        k_inv = inverse(k, p - 1)
        s = (k_inv * (mac - x * r)) % (p - 1)
        return r, s
    except ValueError:
        pass

def verify_sig(mac: int, r: int, s: int, p: int, g: int, y: int) -> bool:
    if not (0 < r < p):
        return False
    v1 = pow(y, r, p) * pow(r, s, p) % p
    v2 = pow(g, mac, p)
    return v1 == v2

# Keys and Secret
key_hex = os.environ.get("KEY", "ff"*16)
key = bytes.fromhex(key_hex)
p, g, x, y, k = gen_keys()

# Initial Known Msg and Signature
known_msg = b"u never get the flag"
known_mac = mac(key, known_msg)
known_r, known_s = sign_msg(known_mac, p, g, x, k)

print("[*] Welcome to ElGamal-DS based on MAC")
print(f"Known message: {known_msg.decode()}")
print(f"MAC: {known_mac}")
print(f"Signature: (r={known_r}, s={known_s})")
print(f"Public params:")
print(f"{p=}")
print(f"{g=}")
print(f"{y=}")
print("Note: You can ask for (MAC, SIGN) of any msg except ones containing 'give me the flag'")
print("Messages must be given as HEX strings.")

while True:
    print("\nOptions:")
    print("1. Sign a message")
    print("2. Submit a message and signature")
    print("3. Quit")
    opt = input("> ").strip()

    if opt == '1':
        msg_hex = input("Enter message to sign (hex): ").strip()
        try:
            msg = bytes.fromhex(msg_hex)
        except ValueError:
            print("Invalid hex input.")
            continue
        if b"give me the flag" in msg:
            print("This message is not allowed!")
            continue
        mac_dig = mac(key, msg)
        r, s = sign_msg(mac_dig, p, g, x, k)
        print(f"MAC: {mac_dig}")
        print(f"Signature: (r={r}, s={s})")

    elif opt == '2':
        msg_hex = input("Enter message (hex): ").strip()
        try:
            msg = bytes.fromhex(msg_hex)
        except ValueError:
            print("Invalid hex input.")
            continue
        try:
            r = int(input("Enter r: ").strip())
            s = int(input("Enter s: ").strip())
        except:
            print("Invalid input.")
            continue
        mac_dig = mac(key, msg)
        if verify_sig(mac_dig, r, s, p, g, y):
            if b"give me the flag" in msg:
                print(f"Correct signature! Here's the flag: {FLAG.decode()}")
            else:
                print("Valid signature, but not the right message.")
        else:
            print("Invalid signature.")

    elif opt == '3':
        print("Bye!")
        exit()
        break
        
    else:
        print("Invalid option.")

