from Crypto.Util.number import getPrime, bytes_to_long, GCD
from random import randint
from math import factorial
import sys
import os

sys.set_int_max_str_digits(100000)
FLAG = os.environ.get("FLAG", "flag{quad_eq_2_bezout_id_2_leaky_factorial_beat_rsa}").encode()

# PubKey
p = getPrime(1024)
q = getPrime(1024)
N = p * q
e = 65537

# PrivKey
phi_N = (p-1) * (q-1)
d = pow(e, -1, phi_N)

flag_pt = bytes_to_long(FLAG)
flag_ct = pow(flag_pt, e, N)
assert pow(flag_ct, d, N) == flag_pt


k = randint(2**7, 2**12)
l = factorial(k) * p

M = factorial(k) * N - 1
assert GCD(l, M) == 1
r1 = getPrime(128)
l1 = pow(l, r1, M)
r2 = getPrime(128)
l2 = pow(l, r2, M)

Q = r1 ** 2 + r2 ** 2
P = r1 * r2

LEAK = (Q, P, M, l1, l2)
with open('out', 'wb') as f:
    f.write(str(LEAK).encode()+ b'\n')
    f.write(hex(flag_ct).encode() + b'\n')
    f.close()