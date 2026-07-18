#include <stdio.h>
#include <string.h>
#define MAX 100
void bitStuffing(char data[], char stuffed[]) {
    int i, j = 0, count = 0;
    for (i = 0; data[i] != '\0'; i++) {
        stuffed[j++] = data[i];
        if (data[i] == '1') {
            count++;
            if (count == 5) {
                stuffed[j++] = '0';
                count = 0;
            }
        } else {
            count = 0;
        }
    }
    stuffed[j] = '\0';
}
void bitUnstuffing(char data[], char unstuffed[]) {
    int i, j = 0, count = 0;
    for (i = 0; data[i] != '\0'; i++) {
        if (data[i] == '1') {
            count++;
        } else {
            count = 0;
        }
        unstuffed[j++] = data[i];
        if (count == 5 && data[i + 1] == '0') {
            i++; // Skip stuffed bit
            count = 0;
        }
    }
    unstuffed[j] = '\0';
}
void transmitter(char data[]) {
    char stuffed[MAX];
    bitStuffing(data, stuffed);
    printf("Transmitted Data: %s\n", stuffed);
}
void receiver(char data[]) {
    char unstuffed[MAX];
    bitUnstuffing(data, unstuffed);
    printf("Received Data: %s\n", unstuffed);
}
int main() {
    int choice;
    char data[MAX];
    do {
        printf("\nMenu:\n1. Transmitter\n2. Receiver\n3. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        getchar();        
        switch (choice) {
            case 1:
                printf("Enter binary data: ");
                scanf("%s", data);
                transmitter(data);
                break;            
            case 2:
                printf("Enter received data: ");
                scanf("%s", data);
                receiver(data);
                break;            
            case 3:
                printf("Exiting...\n");
                break;            
            default:
                printf("Invalid choice! Try again.\n");
        }
    } while (choice != 3);    
    return 0;
}

