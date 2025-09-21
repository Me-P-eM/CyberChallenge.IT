#include <stdio.h>
#include <stdint.h> 
#include <inttypes.h>
#include <stdlib.h> 
#include <unistd.h>
#include <sys/mman.h>
#include <string.h>

static const char* msg = "Give me your shellcode size (max 100): ";
static const uint8_t header[] = {0x48, 0x31, 0xE4, 0x48, 0x31, 0xED , 0x48, 0x31, 0xC0}; 

void init(){
	setvbuf(stdin, NULL, _IOFBF, 1024);   
	setvbuf(stdout, NULL, _IOFBF, 1024); 
	setvbuf(stderr, NULL, _IONBF, 0);   
}

void bye(){
	__asm__ volatile (
		"mov $60, %rax\n\t" 
		"xor %rdi, %rdi\n\t" 
		"syscall\n\t"
	);
}

int read_exactly(uint8_t *buf, uint size){
	puts("Now!!");
	fflush(stdout);

	if (!buf || size == 0) return -1;

	uint8_t bytes_read = 0;
	while (bytes_read < size) {
		int result = read(STDIN_FILENO, &buf[bytes_read], 1);
		if (result < 0) {
	    		perror("Read failed");
	    		exit(1);
		}
		if (result == 0) {
	    		break;
		}
		bytes_read += (int)result;
	}
	return bytes_read;
}


int main(){
	uint8_t size;
	int err;
	uint8_t buf[101];
	void* addr;

	init();
	printf(msg);
	fflush(stdout);

	err = scanf("%hhu", &size);
	
	if(!err){
		puts("Why?");
		fflush(stdout);
        	exit(1);
	}
	
	if(size > 100){
		puts("You found the backdoor!!!");
		fflush(stdout);
		asm volatile("movl $0, 0x1337");
	}

	err = read_exactly(buf, size);
	
	for (uint i = 0; i + 1 < size; i++) {
		if (buf[i] == 0x0F && buf[i+1] == 0x05) {
            		puts("Syscalls are forbidden");
			bye();
        	}
		if (buf[i] == 0xCD && buf[i+1] == 0x80){
			puts("Int 0x80 are forbidden");
			bye();
		}
		if (buf[i] == 0x0F && buf[i+1] == 0x34){
			puts("Not this time");
			bye();
		}
    	}
	
	addr = mmap((void *)0xdeadb000,
		4096,
		PROT_READ | PROT_WRITE, 
		MAP_PRIVATE | MAP_ANONYMOUS | MAP_FIXED,
		-1, 0);

	if (addr == MAP_FAILED) {
        	perror("mmap failed");
        	return 1;
	}

	memcpy(addr, header, sizeof(header));
	memcpy(addr+sizeof(header), buf, size);

	err = mprotect(addr, 4096, PROT_READ | PROT_WRITE | PROT_EXEC);
	if(err){
		perror("mprotect failed");
		return 1;
	}

	puts("Have fun!");
	fflush(stdout);
	asm volatile (
		"xorq %rax, %rax\n\t"
		"xorq %rbx, %rbx\n\t"
		"xorq %rcx, %rcx\n\t"
		"xorq %rdx, %rdx\n\t"
		"xorq %rsi, %rsi\n\t"
		"xorq %rdi, %rdi\n\t"
		"xorq %r8,  %r8\n\t"
		"xorq %r9,  %r9\n\t"
		"xorq %r10, %r10\n\t"
		"xorq %r11, %r11\n\t"
		"xorq %r12, %r12\n\t"
		"xorq %r13, %r13\n\t"
		"xorq %r14, %r14\n\t"
	);

	__asm__  volatile(
		"leaq main(%%rip), %%r15\t\n"
	        ::: "r15" 
	);

	 __asm__ volatile("movq $0xdeadb000, %%rax\n\t"
			  "jmp *%%rax\n\t"
			    :
			    :
			    : "rax"
	);


	return 0;
}
