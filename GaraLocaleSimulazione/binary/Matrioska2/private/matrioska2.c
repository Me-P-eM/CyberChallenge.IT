#include <stdio.h>
#include <string.h>

#define FLAG_SIZE 54

unsigned char vrfy_53(char * p) {
    return *p == '}' && *(p + 1) == '\0';
}

unsigned char vrfy_52(char * p) {
    return *p == 'C' && vrfy_53(p + 1);
}

unsigned char vrfy_51(char * p) {
    return *p == 'C' && vrfy_52(p + 1);
}

unsigned char vrfy_50(char * p) {
    return *p == '4' && vrfy_51(p + 1);
}

unsigned char vrfy_49(char * p) {
    return *p == '2' && vrfy_50(p + 1);
}

unsigned char vrfy_48(char * p) {
    return *p == '0' && vrfy_49(p + 1);
}

unsigned char vrfy_47(char * p) {
    return *p == '2' && vrfy_48(p + 1);
}

unsigned char vrfy_46(char * p) {
    return *p == '_' && vrfy_47(p + 1);
}

unsigned char vrfy_45(char * p) {
    return *p == '3' && vrfy_46(p + 1);
}

unsigned char vrfy_44(char * p) {
    return *p == 'm' && vrfy_45(p + 1);
}

unsigned char vrfy_43(char * p) {
    return *p == '_' && vrfy_44(p + 1);
}

unsigned char vrfy_42(char * p) {
    return *p == 'n' && vrfy_43(p + 1);
}

unsigned char vrfy_41(char * p) {
    return *p == '0' && vrfy_42(p + 1);
}

unsigned char vrfy_40(char * p) {
    return *p == 'w' && vrfy_41(p + 1);
}

unsigned char vrfy_39(char * p) {
    return *p == '_' && vrfy_40(p + 1);
}

unsigned char vrfy_38(char * p) {
    return *p == 'h' && vrfy_39(p + 1);
}

unsigned char vrfy_37(char * p) {
    return *p == 'c' && vrfy_38(p + 1);
}

unsigned char vrfy_36(char * p) {
    return *p == '1' && vrfy_37(p + 1);
}

unsigned char vrfy_35(char * p) {
    return *p == 'h' && vrfy_36(p + 1);
}

unsigned char vrfy_34(char * p) {
    return *p == 'w' && vrfy_35(p + 1);
}

unsigned char vrfy_33(char * p) {
    return *p == '_' && vrfy_34(p + 1);
}

unsigned char vrfy_32(char * p) {
    return *p == '3' && vrfy_33(p + 1);
}

unsigned char vrfy_31(char * p) {
    return *p == 'g' && vrfy_32(p + 1);
}

unsigned char vrfy_30(char * p) {
    return *p == 'n' && vrfy_31(p + 1);
}

unsigned char vrfy_29(char * p) {
    return *p == '3' && vrfy_30(p + 1);
}

unsigned char vrfy_28(char * p) {
    return *p == '1' && vrfy_29(p + 1);
}

unsigned char vrfy_27(char * p) {
    return *p == 'l' && vrfy_28(p + 1);
}

unsigned char vrfy_26(char * p) {
    return *p == '4' && vrfy_27(p + 1);
}

unsigned char vrfy_25(char * p) {
    return *p == 'h' && vrfy_26(p + 1);
}

unsigned char vrfy_24(char * p) {
    return *p == 'C' && vrfy_25(p + 1);
}

unsigned char vrfy_23(char * p) {
    return *p == '_' && vrfy_24(p + 1);
}

unsigned char vrfy_22(char * p) {
    return *p == '3' && vrfy_23(p + 1);
}

unsigned char vrfy_21(char * p) {
    return *p == 'h' && vrfy_22(p + 1);
}

unsigned char vrfy_20(char * p) {
    return *p == 't' && vrfy_21(p + 1);
}

unsigned char vrfy_19(char * p) {
    return *p == '_' && vrfy_20(p + 1);
}

unsigned char vrfy_18(char * p) {
    return *p == 's' && vrfy_19(p + 1);
}

unsigned char vrfy_17(char * p) {
    return *p == '4' && vrfy_18(p + 1);
}

unsigned char vrfy_16(char * p) {
    return *p == 'w' && vrfy_17(p + 1);
}

unsigned char vrfy_15(char * p) {
    return *p == '_' && vrfy_16(p + 1);
}

unsigned char vrfy_14(char * p) {
    return *p == 'a' && vrfy_15(p + 1);
}

unsigned char vrfy_13(char * p) {
    return *p == 'k' && vrfy_14(p + 1);
}

unsigned char vrfy_12(char * p) {
    return *p == 's' && vrfy_13(p + 1);
}

unsigned char vrfy_11(char * p) {
    return *p == 'o' && vrfy_12(p + 1);
}

unsigned char vrfy_10(char * p) {
    return *p == 'i' && vrfy_11(p + 1);
}

unsigned char vrfy_9(char * p) {
    return *p == 'r' && vrfy_10(p + 1);
}

unsigned char vrfy_8(char * p) {
    return *p == 't' && vrfy_9(p + 1);
}

unsigned char vrfy_7(char * p) {
    return *p == 'a' && vrfy_8(p + 1);
}

unsigned char vrfy_6(char * p) {
    return *p == 'M' && vrfy_7(p + 1);
}

unsigned char vrfy_5(char * p) {
    return *p == '{' && vrfy_6(p + 1);
}

unsigned char vrfy_4(char * p) {
    return *p == 'g' && vrfy_5(p + 1);
}

unsigned char vrfy_3(char * p) {
    return *p == 'a' && vrfy_4(p + 1);
}

unsigned char vrfy_2(char * p) {
    return *p == 'l' && vrfy_3(p + 1);
}

unsigned char vrfy_1(char * p) {
    return *p == 'f' && vrfy_2(p + 1);
}

unsigned char vrfy(const char *input)
{
    return vrfy_1((char*)input);
}

int main(int argc, char const *argv[])
{
    size_t len;
    if (argc != 2) {
        printf("Usage: %s <flag>\n", argv[0]);
        return 1;
    }
    len = strlen(argv[1]);
    if (len > FLAG_SIZE-1) {
        printf("Invalid flag size\n");
        return 1;
    }
    if (argv[1][len] != '\0') {
        printf("Invalid flag format\n");
        return 1;
    }
    if (vrfy((const char *)argv[1])) {
        printf("Correct flag!\n");
    } else {
        printf("Incorrect flag\n");
    }
    return 0;
}
