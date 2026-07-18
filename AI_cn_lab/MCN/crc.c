#include <stdio.h>
#include <string.h>
void xorCRC(char *div, const char *key) {
    for (int i = 1; i < strlen(key); i++)
        div[i] = (div[i] == key[i]) ? '0' : '1';
}
void mod2div(char *dividend, const char *key, char *rem) {
    int keylen = strlen(key);
    strncpy(rem, dividend, keylen);
    for (int i = keylen; i <= strlen(dividend); i++) {
        if (rem[0] == '1') xorCRC(rem, key);
        memmove(rem, rem + 1, keylen - 1);
        rem[keylen - 1] = dividend[i];
    }
    rem[keylen - 1] = '\0';
}
void crcTransmitter() {
    char data[100], key[30], temp[130], rem[30];
    printf("\n[Transmitter] Enter binary data: "); scanf("%s", data);
    printf("Enter generator key: "); scanf("%s", key);

    strcpy(temp, data);
    for (int i = 0; i < strlen(key) - 1; i++) strcat(temp, "0");

    mod2div(temp, key, rem);
    strcat(data, rem);

    printf("CRC Checksum: %s\nTransmitted Frame: %s\n", rem, data);
}
void crcReceiver() {
    char frame[130], key[30], rem[30];
    printf("\n[Receiver] Enter received frame: "); scanf("%s", frame);
    printf("Enter generator key: "); scanf("%s", key);

    int keylen = strlen(key);
    int datalen = strlen(frame) - keylen + 1;

    mod2div(frame, key, rem);
    rem[keylen - 1] = '\0';

    printf("Received Data (excluding checksum): ");
    for (int i = 0; i < datalen; i++) putchar(frame[i]);
    printf("\n");

    printf(strspn(rem, "0") == strlen(rem) ? "No error. Data is correct.\n"
                                           : "Error detected in received data.\n");
}
int main() {
    int ch;
    while (1) {
        printf("\n=== CRC MENU ===\n1. Transmitter\n2. Receiver\n3. Exit\nEnter choice: ");
        scanf("%d", &ch);
        if (ch == 1) crcTransmitter();
        else if (ch == 2) crcReceiver();
        else if (ch == 3) break;
        else printf("Invalid choice!\n");
    }
    return 0;
}
