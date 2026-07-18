#include <stdio.h>
#include <math.h>
#include <string.h>
int isPowerOfTwo(int x) {
    return (x & (x - 1)) == 0;
}
int main() {
    char data[32];
    printf("Enter binary data: ");
    scanf("%s", data);
    int m = strlen(data);
    int r = 0;
    while ((1 << r) < (m + r + 1)) r++;
    int total = m + r;
    char hamming[64];
    int j = 0, k = 0;
    for (int i = 1; i <= total; i++) {
        if (isPowerOfTwo(i))
            hamming[i - 1] = '0';
        else
            hamming[i - 1] = data[j++];
    }

    for (int i = 0; i < r; i++) {
        int pos = (1 << i);
        int count = 0;
        for (int j = pos; j <= total; j++) {
            if (((j >> i) & 1) && hamming[j - 1] == '1')
                count++;
        }
        hamming[pos - 1] = (count % 2) ? '1' : '0';
    }

    printf("Hamming code: ");
    for (int i = 0; i < total; i++) printf("%c", hamming[i]);
    printf("\n");
    return 0;
}
