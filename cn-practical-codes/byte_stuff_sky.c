#include <stdio.h>
#include <string.h>
#define MAX 100
#define FLAG "flag"
#define ESC "esc"

void byteStuffing() {
    char word[MAX], stuffed[MAX * 2] = "";
    int n;

    printf("Number of words: ");
    scanf("%d", &n);

    strcat(stuffed, FLAG);
    strcat(stuffed, " ");

    printf("Enter the words:\n");
    for (int i = 0; i < n; i++) {
        scanf("%s", word);
        
        // If word is FLAG or ESC, add escape sequence
        if (strcmp(word, FLAG) == 0 || strcmp(word, ESC) == 0) {
            strcat(stuffed, ESC);
            strcat(stuffed, " ");
        }
        
        strcat(stuffed, word);
        strcat(stuffed, " ");
    }
    
    strcat(stuffed, FLAG);
    printf("Stuffed: %s\n", stuffed);
}

void byteDestuffing() {
    char word[MAX], result[MAX * 2] = "";
    int flagCount = 0, escapeNext = 0;

    printf("Enter stuffed input (space separated):\n");

    while (scanf("%s", word) == 1) {
         if (strcmp(word, ESC) == 0 && !escapeNext) {
            escapeNext = 1; // Next word is escaped
            continue;
        }
        
        if (strcmp(word, FLAG) == 0 && !escapeNext) {
            flagCount++;
            if (flagCount == 1) continue; // Skip first flag
            if (flagCount == 2) break; // Stop at second flag
        }
        
       
        // Add word to result
        if (strlen(result) > 0) strcat(result, " ");
        strcat(result, word);
        
        escapeNext = 0;
    }
    
    printf("Destuffed: %s\n", result);
}


int main() {
    int choice;
    while (1) {
        printf("\nByte Stuffing\nMenu:\n1. Transmitter\n2. Receiver\n3. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        getchar(); // consume leftover newline

        switch (choice) {
            case 1: byteStuffing(); break;
           case 2: byteDestuffing(); break;
            case 3: return 0;
            default: printf("Invalid choice! Try again.\n");
        }
    }
}