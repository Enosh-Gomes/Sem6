#include <stdio.h>
#include <string.h>
void manchesterEncoding(const char *input, int output[], int *size) {
    *size = 0;
    int i;
    for (i = 0; input[i] != '\0'; i++) {
        if (input[i] == '0') {
            output[(*size)++] = 1;
            output[(*size)++] = 0;
        } else {
            output[(*size)++] = 0;
            output[(*size)++] = 1;
        }
    }
}
void differentialManchesterEncoding(const char *input, int output[], int *size) {
    *size = 0;
    char lastBit;
	int i;
	lastBit=0;  
    for (i = 0; input[i] != '\0'; i++) {
        if (input[i] == '1') {
            lastBit = (lastBit == 1) ? 0 : 1;
            lastBit = (lastBit == 1) ? 0 : 1;
            output[(*size)++] = lastBit;
            lastBit = (lastBit == 1) ? 0 : 1;
            output[(*size)++] = lastBit;
        } else {
        	lastBit = (lastBit == 1) ? 0 : 1;
            output[(*size)++] = lastBit;
            lastBit = (lastBit == 1) ? 0 : 1;
            output[(*size)++] = lastBit;
        }
    }
}
int main() {
    char input[100],i;
    int manchester[200], differential[200];
    int manchesterSize, differentialSize;    
    printf("Enter binary string: ");
    scanf("%s", input);    
    manchesterEncoding(input, manchester, &manchesterSize);
    differentialManchesterEncoding(input, differential, &differentialSize);    
    printf("Manchester Encoding: ");
    for (i = 0; i < manchesterSize; i += 2) {
        printf("%d%d ", manchester[i], manchester[i + 1]);
    }
    printf("\n");    
    printf("Differential Manchester Encoding: ");
    for (i = 0; i < differentialSize; i += 2) {
        printf("%d%d ", differential[i], differential[i + 1]);
    }
    printf("\n");    
    return 0;
}
