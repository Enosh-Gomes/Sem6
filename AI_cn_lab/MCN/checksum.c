#include <stdio.h>
#include <string.h>
#define N 20

void binaryAdd(char a[], char b[], char sum[]) {
    int len = strlen(a), carry = 0;
    for (int i = len - 1; i >= 0; i--) {
        int bit = (a[i] - '0') + (b[i] - '0') + carry;
        sum[i] = (bit % 2) + '0';
        carry = bit / 2;
    }
    sum[len] = '\0';
    if (carry) {
        for (int i = len - 1; i >= 0 && carry; i--) {
            int bit = (sum[i] - '0') + carry;
            sum[i] = (bit % 2) + '0';
            carry = bit / 2;
        }
    }
}

void onesComplement(char in[], char out[]) {
    for (int i = 0; in[i]; i++) out[i] = (in[i] == '0') ? '1' : '0';
    out[strlen(in)] = '\0';
}

int isAllOnes(char s[]) {
    for (int i = 0; s[i]; i++) if (s[i] != '1') return 0;
    return 1;
}

int main() {
    int ch; char a[N], b[N], c[N], chk[N], sum[N];
    while (1) {
        printf("\nChecksum Menu:\n1. Transmitter\n2. Receiver\n3. Exit\nEnter choice: ");
        scanf("%d", &ch);
        if (ch == 3) break;

        printf("Enter first binary number: "); scanf("%s", a);
        printf("Enter second binary number: "); scanf("%s", b);

        if (ch == 1) {
            binaryAdd(a, b, sum);
            onesComplement(sum, chk);
            printf("Sum: %s\nChecksum: %s\nEncoded: %s %s %s\n", sum, chk, a, b, chk);
        } else if (ch == 2) {
            printf("Enter received checksum: "); scanf("%s", c);
            binaryAdd(a, b, sum); binaryAdd(sum, c, sum);
            printf(isAllOnes(sum) ? "No error.\nDecoded: %s %s\n" : "Error detected!\n", a, b);
        } else printf("Invalid choice!\n");
    }
    return 0;
}
