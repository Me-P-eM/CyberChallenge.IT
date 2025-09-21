import pwn

HOST = ""
PORT = 0

p = pwn.remote(HOST, PORT)
res = p.recvuntil(b"> ").decode()
payload = ""
p.sendline(payload.encode())