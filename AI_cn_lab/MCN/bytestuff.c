#include <stdio.h>
#include <string.h>
#define MAX 100
#define FLAG "flag "
#define ESC "esc "
void byteStuffing(char data[], char stuffed[]) {
    int i = 0, j = 0;
    strcpy(stuffed,FLAG); 
    j += strlen(FLAG);   
    while (data[i] != '\0') {
        if (strncmp(&data[i], FLAG, strlen(FLAG)) == 0) {
            strcpy(&stuffed[j], ESC);
            j += strlen(ESC);
        } else if (strncmp(&data[i], ESC, strlen(ESC)) == 0) {
            strcpy(&stuffed[j], ESC);
            j += strlen(ESC);
        }
        stuffed[j++] = data[i++];
    }    
    strcpy(&stuffed[j], FLAG); 
    j += strlen(FLAG);
    stuffed[j] = '\0'; 
}
void byteUnstuffing(char data[], char unstuffed[]) {
    int i = 0, j = 0;
    int dataLen = strlen(data);
    if (strncmp(&data[i], FLAG, strlen(FLAG)) == 0) {
        i += strlen(FLAG);
    }
    int k;
    int lastFlagIndex = -1;
    for ( k = dataLen - strlen(FLAG); k >= 0; k--) {
        if (strncmp(&data[k], FLAG, strlen(FLAG)) == 0) {
            lastFlagIndex = k;
            break;
        }
    }
	while (i < dataLen) {
        if (i == lastFlagIndex) {
            break;
        }
        if (strncmp(&data[i], ESC, strlen(ESC)) == 0) {
            if (i + strlen(ESC) < dataLen &&
                (strncmp(&data[i + strlen(ESC)], FLAG, strlen(FLAG)) == 0 ||
                 strncmp(&data[i + strlen(ESC)], ESC, strlen(ESC)) == 0)) {
                i += strlen(ESC);
            }
        }        
        unstuffed[j++] = data[i++];
    }    
    unstuffed[j] = '\0'; 
}
void transmitter(char data[]) {
    char stuffed[MAX];
    byteStuffing(data, stuffed);
    printf("Transmitted Data: %s\n", stuffed);
}
void receiver(char data[]) {
    char unstuffed[MAX];
    byteUnstuffing(data, unstuffed);
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
                printf("Enter data: ");
                fgets(data, MAX, stdin);
                data[strcspn(data, "\n")] = 0; 
                transmitter(data);
                break;            
            case 2:
                printf("Enter received data: ");
                fgets(data, MAX, stdin);
                data[strcspn(data, "\n")] = 0;
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

