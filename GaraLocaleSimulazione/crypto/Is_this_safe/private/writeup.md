# Is this safe?

## Cipher analilsis
The cipher takes a string and a number between 2 and 8912 as input.
Since the number of keys is small we can try all of them.
The cipher simply multiply the letter of the plaintext by the key.
To decipher the plaintext we divide the character by the key.
Try all the key until you get a plaintext with `flag` at the beginning.
