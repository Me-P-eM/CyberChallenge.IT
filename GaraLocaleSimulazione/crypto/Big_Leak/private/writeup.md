# Big Leak

## 👁️‍🗨️  Overview

This challenge hides one of the RSA primes (`p`) within a multiplicative structure involving a factorial. We're given a ciphertext encrypted with RSA and a tuple of values `(Q, P, M, l1, l2)` where:

- `N = p * q` is the RSA modulus (not directly given)
- `l = factorial(k) * p`
- `M = factorial(k) * N - 1`
- `l1 = l^r1 mod M`
- `l2 = l^r2 mod M`
- `Q = r1² + r2²`, `P = r1 * r2`

We must recover the RSA private key by extracting `p`, reconstructing `N`, and computing `φ(N)` to decrypt the flag.

---

## Step-by-step Breakdown

### 🔓 Step 1: Recover `r1` and `r2` from `(Q, P)`

We are given:
- \( Q = r_1^2 + r_2^2 \)
- \( P = r_1 \cdot r_2 \)

This allows us to reconstruct \( r_1 \) and \( r_2 \) as the roots of the quadratic:

\[
x^2 - Sx + P = 0 \quad \text{where } S = r_1 + r_2 = \sqrt{Q + 2P}
\]

From this, we compute:
- \( r_1 = \frac{S + \sqrt{S^2 - 4P}}{2} \)
- \( r_2 = \frac{S - \sqrt{S^2 - 4P}}{2} \)

This works since both `r1` and `r2` are 128-bit primes.

---

### 🔧 Step 2: Combine `l1` and `l2` to recover `l`

We have:
- `l1 = l^r1 mod M`
- `l2 = l^r2 mod M`

Using the Bézout identity:
\[
a \cdot r_1 + b \cdot r_2 = 1
\Rightarrow l^{a r_1 + b r_2} \equiv l \mod M
\]

So we compute:
\[
l = l_1^a \cdot l_2^b \mod M
\]

---

### 🧮 Step 3: Extract `p` from `l = factorial(k) * p`

We brute-force small `k` in the range [128, 4096] and look for the correct one such that:

- `p = l // factorial(k)` is in the correct size range (1024 bits)
- And `N = (M + 1) // factorial(k)` is consistent with RSA modulus construction

Once `p` is found, `q = N // p`.

---

### 🔐 Step 4: Decrypt the flag

Now that we have `p` and `q`, we compute:

- \( \phi(N) = (p-1)(q-1) \)
- \( d = e^{-1} \mod \phi(N) \)
- \( m = c^d \mod N \)

where `c` is the ciphertext.

Finally, we convert the plaintext back to bytes and read the flag.

---

## Conclusion

The trick in this challenge lies in the clever hiding of `p` within a factorial multiple, and in recovering it using RSA structure and basic number theory. The leakage structure `(l1, l2)` is vulnerable to known exponent recombination via Bézout coefficients.

The full exploit script automates the recovery and decryption process in just a few seconds.

---
