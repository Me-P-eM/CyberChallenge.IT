#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

const char encr[49] = "pxhmh\"lQF:3wcCw\"Tbd)bXa0s#og;Y?nD{utyx)E{q-|z)8~\0";
const char *banner = 
                                                                                                                                           
" @@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@                  @@@  @@@   @@@@@@    @@@@@@   @@@@@@@  @@@   @@@@@@   @@@  @@@   @@@@@@   @@@\n"
"@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@                 @@@@ @@@  @@@@@@@   @@@@@@@@  @@@@@@@  @@@  @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@\n"       
"!@@       @@!       @@!       @@!  @@@                 @@!@!@@@  !@@       @@!  @@@    @@!    @@!  @@!  @@@  @@!@!@@@  @@!  @@@  @@!\n"       
"!@!       !@!       !@!       !@!  @!@                 !@!!@!@!  !@!       !@!  @!@    !@!    !@!  !@!  @!@  !@!!@!@!  !@!  @!@  !@!\n"       
"!!@@!!    @!!!:!    @!!!:!    @!@  !@!                 @!@ !!@!  !!@@!!    @!@!@!@!    @!!    !!@  @!@  !@!  @!@ !!@!  @!@!@!@!  @!!\n"       
" !!@!!!   !!!!!:    !!!!!:    !@!  !!!                 !@!  !!!   !!@!!!   !!!@!!!!    !!!    !!!  !@!  !!!  !@!  !!!  !!!@!!!!  !!!\n"       
"     !:!  !!:       !!:       !!:  !!!                 !!:  !!!       !:!  !!:  !!!    !!:    !!:  !!:  !!!  !!:  !!!  !!:  !!!  !!:\n"       
"    !:!   :!:       :!:       :!:  !:!  :!:  :!:  :!:  :!:  !:!      !:!   :!:  !:!    :!:    :!:  :!:  !:!  :!:  !:!  :!:  !:!   :!:\n"      
":::: ::    :: ::::   :: ::::   :::: ::  :::  :::  :::   ::   ::  :::: ::   ::   :::     ::     ::  ::::: ::   ::   ::  ::   :::   :: ::::\n"  
":: : :    : :: ::   : :: ::   :: :  :   :::  :::  :::  ::    :   :: : :     :   : :     :     :     : :  :   ::    :    :   : :  : :: : :\n";  
                                                                                                                                           

void init(){
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
}

void menu(){
	puts(banner);
	puts("Welcome to our password encryptor service, give us you password to boost its entropy! (its for free, we don't store your password)");
}

long seed(){
	return 0xdeadbeefcafebabe ^ 0x1337133713371337;
}

void encrypt(char buf[]){
	int l;
	l = strlen(buf);
	for(int i=0;i<l;i++){
		buf[i] = (rand()%31) ^ buf[i]; 
	}
	printf("here's your high entropy password: %s\nentropy gained: +%d\n", buf, rand()%31);

}


int main(){
	char buf[48];
	int f;

	init();
	menu();
	srand(seed());
	printf("> ");
	scanf("%48s", buf);
	encrypt(buf);
	f = memcmp(buf, encr, 48);
	if(f==0){
		puts("\nOh wait a moment.. I forgot to remove my old password..\nCongratz this time you won!!");
	}

	return 0;
}
