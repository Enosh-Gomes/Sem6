#include <stdio.h>
#include <string.h>
#define max 100

void bitStuffing(){
    char data[max],stuffed[max];
    int i,j=0,count=0;
    
    printf("Enter the message: ");
    scanf("%s", data);

    for(int i=0;i<strlen(data);i++){
        stuffed[j++]=data[i];
        if(data[i]=='1'){
            count++;
            if(count==5){
                stuffed[j++]='0';
                count=0;
            }
        }
        else{
            count=0;
        }
    }
    stuffed[j]='\0';

printf("Stuffed message: %s\n", stuffed);
}

void bitDestuffing(){
   char input[max],destuffed[max];
   int i,j=0,count=0;
    printf("Enter the message: ");
    scanf("%s", input);

   for(int i=0;i<strlen(input);i++){
        destuffed[j++]=input[i];
        if(input[i]=='1'){
            count++;
            if(count==5 && input[i+1]=='0'){
                i++;
                count=0;
            }
        }
        else{
            count=0;
        }
    }
    destuffed[j]='\0';

printf("Stuffed message: %s\n", destuffed);

}

int main() {
    int choice;
    while (1) {
        printf("\nBit Stuffing\n1. Transmitter\n2. Receiver\n3. Exit\nChoice: ");
        scanf("%d", &choice);

        if (choice == 1) bitStuffing();
       else if (choice == 2) bitDestuffing();
        else if (choice == 3) break;
        else printf("Invalid choice! Try again.\n");
    }
    return 0;
}