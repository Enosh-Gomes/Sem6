#include <stdio.h>

int main() {
    int data[7], r[3];

    printf("Enter 4 data bits (d3 d5 d6 d7): ");
    scanf("%d%d%d%d", &data[2], &data[4], &data[5], &data[6]);

    // Parity bits
    data[0] = data[2] ^ data[4] ^ data[6]; // r1
    data[1] = data[2] ^ data[5] ^ data[6]; // r2
    data[3] = data[4] ^ data[5] ^ data[6]; // r4

    printf("Hamming Code: ");
    for (int i = 0; i < 7; i++) printf("%d ", data[i]);
    printf("\n");

    // Simulate error
    printf("Enter received bits: ");
    for (int i = 0; i < 7; i++) scanf("%d", &data[i]);

    r[0] = data[0] ^ data[2] ^ data[4] ^ data[6];
    r[1] = data[1] ^ data[2] ^ data[5] ^ data[6];
    r[2] = data[3] ^ data[4] ^ data[5] ^ data[6];

    int error_pos = r[0] + r[1]*2 + r[2]*4;

    if (error_pos == 0)
        printf("No error\n");
    else {
        printf("Error at position: %d\n", error_pos);
        data[error_pos - 1] ^= 1; // Correct the error
        printf("Corrected code: ");
        for (int i = 0; i < 7; i++) printf("%d ", data[i]);
        printf("\n");
    }

    return 0;
}
