#include <stdio.h>
#include <string.h>
#define max 100
#define FLAG "flag"
#define ESC "esc"

void byteStuffing() {
    char word[max],stuffed[max*2];
    int n;

     printf("Number of words: ");
    scanf("%d",&n);

    strcat(stuffed,FLAG);
    strcat(stuffed," ");

    printf("Enter the words:\n");
    for (int i = 0; i < n; i++) {
        scanf("%s", word);

        if(strcmp(word,FLAG)==0 || strcmp(word,ESC)==0){
            strcat(stuffed,ESC);
    strcat(stuffed," ");
        }

        strcat(stuffed,word);
    strcat(stuffed," ");

    }
    strcat(stuffed,FLAG);
    strcat(stuffed," ");

    printf("stuffed: %s\n", stuffed);
}

void byteDestuffing() {
     char word[max], result[max * 2] = "";
    int flagCount = 0, escapeNext = 0;

    printf("Enter stuffed input (space separated):\n");
    while(scanf("%s",word)==1){
        if(strcmp(word,ESC)==0 && !escapeNext){
            escapeNext=1;
            continue;
        }

        if(strcmp(word,FLAG)==0 && !escapeNext){
            flagCount++;
            if(flagCount==1) continue;
            if(flagCount==2) break;
        }

        if(strlen(result)>0)  strcat(result," ");

        strcat(result, word);
        escapeNext=0;
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