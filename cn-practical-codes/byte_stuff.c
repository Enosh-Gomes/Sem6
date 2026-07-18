#include <stdio.h>
#include <string.h>
#define MAX 100
#define FLAG "flag"
#define ESC "esc"

void byteStuffing() {
    char word[MAX], stuffed[MAX * 2] = "";  // Start with FLAG
    int n;

    printf("Number of words: ");
    scanf("%d", &n);

    strcat(stuffed, FLAG); strcat(stuffed, " ");

    printf("Enter the words:\n");
    for (int i = 0; i < n; i++) {
        scanf("%s", word);

        if(strcmp(word,FLAG)==0 || strcmp(word,ESC)==0){
        strcat(stuffed,ESC);
        strcat(stuffed, " ");
    }

        strcat(stuffed,word);
        strcat(stuffed, " ");

    }
strcat(stuffed,FLAG);
printf("Stuffed: %s\n", stuffed);
}


void byteDestuffing() {
    char input[MAX * 2], word[MAX], result[MAX * 2] = "";
    int i = 0, esc = 0, flagCount = 0,detectESC=1;

    printf("Enter stuffed input (space separated, ending with 3rd 'flag'):\n");

    while (scanf("%s", word) != EOF) {
     if (strcmp(word, FLAG) == 0) {
            flagCount++;
            if (flagCount == 3) break;
            if(flagCount==1)
            continue;
        }

        if (strcmp(word, ESC) == 0 && detectESC) {
            esc = 1;
            detectESC=0;
            continue;
        }

        

        if (esc) {
    strcat(result, word);  // Append the escaped FLAG or ESC
    strcat(result, " ");
    esc = 0;  // Reset
    detectESC=1;
} else {
    strcat(result, word);
    strcat(result, " ");
}
       
    }
    if (strlen(result) > 0)
        result[strlen(result) - 1] = '\0'; // remove trailing space

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