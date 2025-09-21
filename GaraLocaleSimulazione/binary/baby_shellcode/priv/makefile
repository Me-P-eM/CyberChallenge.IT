build_chall:
	gcc -o chall chall.c \
  -Wall -Wextra -Werror -O2 -fstack-protector-strong -fPIE -pie -D_FORTIFY_SOURCE=2 \
  -Wl,-z,relro,-z,now,-z,noexecstack

