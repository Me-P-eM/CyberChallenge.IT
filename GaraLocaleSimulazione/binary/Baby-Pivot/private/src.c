#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

void init(){
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
}

void challenge(){
	void *ptr;
	char buf[80];
	int l;

	ptr = malloc(0x100);
	printf("After all this could be usefull: %p\n", ptr);
	l = read(0, ptr, 0x100);
	if(l<=120){
		memcpy(buf, ptr, l);
	}else{
		memcpy(buf, ptr, 120);
	}
	return;

}

void free_gadgets(){
	__asm__("pop %rsp\n\t"
		"ret\n\t");
	__asm__("pop %rdi\n\t"
		"ret\n\t");
	__asm__("pop %rax\n\t"
		"pop %rdx\n\t"
		"pop %rsi\n\t"
		"ret");
}


void quit(){
	__asm__("mov $60, %rax\n\t"
		"mov $0, %rdi\n\t"
		"syscall\n\t");
}
int main(){

	init();
	puts("Hi pwners, this time won't be straigthfull as the old days.. or maybe it will"); 
	write(1,"The only thing I'm sure about is that you will never be able to call /bin/sh\0 AHAHAHAAH\n", 89);
	challenge();
	puts("maybe next time");
	quit();
	return 0;
}
