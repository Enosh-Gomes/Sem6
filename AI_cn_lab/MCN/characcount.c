#include <stdio.h>
#include <string.h>
#define MAX 100
void transmitter(char data[], int frame_size) {
    int len = strlen(data);
    int i, j;
    printf("Transmitted Frames:\n");
    for (i = 0; i < len;) {
        int count = (i + frame_size - 1 < len) ? frame_size : (len - i + 1);
        printf("%d", count);
        for (j = 0; j < count - 1 && i < len; j++, i++) 
		{
            printf("%c", data[i]);
        }
    }
}
void receiver(char data[]) {
    printf("Received Data: ");
    int i = 0,j;
    while (i < strlen(data)) {
        int count = data[i] - '0'; 
        if (count <= 0 || count > 9 || i + count > strlen(data)) {
            printf("Wrong data received\n");
            return;
        }
        for ( j = 1; j < count; j++) {
            printf("%c", data[i + j]);
        }
        i += count;
    }
    printf("\n");
}
int main() {
    int choice;
    char data[MAX];
    int frame_size;
    do {
        printf("\nMenu:\n1. Transmitter\n2. Receiver\n3. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        getchar(); 
        switch (choice) {
            case 1:
                printf("Enter data: ");
                scanf("%s", data);
                printf("Enter frame size: ");
                scanf("%d", &frame_size);
                transmitter(data, frame_size);
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

