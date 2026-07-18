#include <stdio.h>
#include <string.h>

// Predefined generator polynomials
#define CRC12_POLY "1100000001111"        // 13 bits
#define CRC16_POLY "11000000000000101"    // 17 bits

void xorOperation(char *rem, const char *key) {
    for (int i = 1; i < strlen(key); i++)
        rem[i] = (rem[i] == key[i]) ? '0' : '1';
}

void computeCRC(char *data, const char *key, char *checksum) {
    int keyLen = strlen(key);
    char temp[128];
    strcpy(temp, data);
    for (int i = 0; i < keyLen - 1; i++)
        strcat(temp, "0");

    char rem[64];
    strncpy(rem, temp, keyLen);
    rem[keyLen] = '\0';

    for (int i = keyLen; i <= strlen(temp); i++) {
        if (rem[0] == '1')
            xorOperation(rem, key);

        memmove(rem, rem + 1, keyLen - 1);
        rem[keyLen - 1] = temp[i];
    }
    rem[keyLen - 1] = '\0';
    strcpy(checksum, rem);
}

void sender() {
    int crc_choice;
    const char *key;
    char data[100], checksum[64];

    printf("\n[Sender] Choose CRC Type:\n1. CRC-12\n2. CRC-16\nEnter choice: ");
    scanf("%d", &crc_choice);

    key = (crc_choice == 1) ? CRC12_POLY : CRC16_POLY;

    printf("Enter binary data: ");
    scanf("%s", data);

    computeCRC(data, key, checksum);
    strcat(data, checksum);

    printf("CRC Checksum: %s\n", checksum);
    printf("Transmitted Frame: %s\n", data);
}

void receiver() {
    int crc_choice;
    const char *key;
    char frame[130], checksum[64];

    printf("\n[Receiver] Choose CRC Type:\n1. CRC-12\n2. CRC-16\nEnter choice: ");
    scanf("%d", &crc_choice);

    key = (crc_choice == 1) ? CRC12_POLY : CRC16_POLY;

    printf("Enter received frame: ");
    scanf("%s", frame);

    computeCRC(frame, key, checksum);

    if (strspn(checksum, "0") == strlen(checksum))
        printf("✅ Data is correct. No error detected.\n");
    else
        printf("❌ Error detected in received data.\n");
}

int main() {
    int choice;

    while (1) {
        printf("\n=== CRC MENU ===\n");
        printf("1. Sender (Generate CRC)\n2. Receiver (Check CRC)\n3. Exit\nEnter choice: ");
        scanf("%d", &choice);

        if (choice == 1)
            sender();
        else if (choice == 2)
            receiver();
        else if (choice == 3)
            break;
        else
            printf("Invalid option!\n");
    }

    return 0;
}
