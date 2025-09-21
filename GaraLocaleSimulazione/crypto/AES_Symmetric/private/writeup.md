# AES Symmetric

## 👁️‍🗨️  Overview

The challenge uses a hybrid cryptosystem: each byte of the flag is encrypted with AES (in ECB mode) and then further encrypted using textbook RSA. The encryption flow is:
```
PT[i] --AES--> --RSA--> CT[i]
```
You are allowed to encrypt arbitrary **printable** characters (one at a time) up to **40 times**, and you are given the list of ciphertexts that correspond to the encrypted flag.

Your task is to reverse the encryption and recover the original flag.

---

## 🔑 Key Observations

- **AES ECB mode**: Since AES is used in ECB mode with a fixed key, encrypting the same padded byte always results in the same ciphertext block.
- **Deterministic mapping**: We can construct a mapping from `AES( pad(b) )` to the final RSA ciphertext using the encryption oracle.
- **RSA textbook (no padding)**: RSA is used without padding, and we are provided with the public modulus `N`, exponent `e`, and the list of encrypted flag blocks.
- **RSA is reversible**: By factoring `N`, we can compute the private exponent `d` and decrypt RSA ciphertexts.

---

## 🧠 Exploit Strategy

1. **Factor N**: Since `p` and `q` are close (by design), we can factor `N` efficiently using Fermat's method.
2. **Recover AES ciphertexts**: For each character in a restricted alphabet (like `a-z0-9{_}`), we encrypt it through the oracle and RSA-decrypt the result to recover the AES ciphertext block.
3. **Build mapping**: Create a dictionary mapping from AES-encrypted block to the character that produced it.
4. **Decrypt the flag**: For each ciphertext block in `FLAG_CT`, decrypt it with the RSA private key to get the AES ciphertext, and use the mapping to recover the original character.

---
