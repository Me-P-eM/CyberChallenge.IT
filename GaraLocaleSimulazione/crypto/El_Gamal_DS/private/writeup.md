# ElGamal-DS

## 🛠  Description

This exploit targets a vulnerable ElGamal digital signature system that signs a SHA256-based MAC. The system is flawed in **two independent ways**:

1. **Insecure MAC Construction**:
   The MAC is defined as `SHA256(key || msg)` — a classic mistake. Since the hash is prepended with the key (instead of using HMAC), it becomes vulnerable to **length extension attacks**.

2. **Nonce Reuse**:
   The ElGamal signing process reuses the same ephemeral `k` value across signatures. This allows recovery of the signing key `x` with two valid signatures.

## 🚩 Goal

Forge a valid signature for the forbidden message:
**`"give me the flag"`**, which the server refuses to sign.

---

## 🧠 Exploit Strategy

1. **Use `hash_extender`**:
   - Craft a message `m2` such that `SHA256(key || m2) = SHA256(key || m1 || padding || extra)`.
   - This works due to the insecure `key || msg` MAC construction.
   - Obtain a new message+tag pair that reuses a known tag but appends arbitrary content.

2. **Collect two signatures**:
   - One from the known message (`m1`), already signed by the server.
   - One from a custom message (`m3`), submitted to the server for signing.

3. **Exploit nonce reuse**:
   - Both signatures reuse the same nonce `k`.
   - Recover `k` algebraically using the two signature equations.

4. **Recover the private key `x`**:
   - Once `k` is known, derive `x` from the known signature.

5. **Forge the final signature**:
   - Sign the extended forbidden message using the recovered key.

6. **Submit and win**:
   - Send the forged signature for `"give me the flag"` and receive the flag.

---

## Conclusion

Combining a **MAC collision** (via hash length extension) with a **signature forgery** (via nonce reuse), the exploit bypasses server restrictions and successfully retrieves the flag.

---
