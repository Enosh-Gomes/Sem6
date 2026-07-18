#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define max 100


void transmitter(){
    char data[max];
    int n,len;
    printf("Data: ");
    scanf("%s",data);
    printf("frame size: ");
    scanf("%d",&n);

    len=strlen(data);
    for(int i=0;i<len;i+=n-1){
        int c=(i+n-1<=len)?n-1:len-i;
        printf("%d",c+1);
        for(int k=0;k<c;k++) 
        printf("%c",data[i+k]);
    }
    printf("\n");
}

void receiver(){
    char input[max],result[max];
    int i=0,j=0;
    printf("Framed input: "); scanf("%s", input);
    while(input[i]){
        int c=input[i++]-'0';
        for(int k=1;k<c && input[i];k++){
            result[j++]=input[i++];
        }
    }
    result[j]='\0';
     printf(" %s ",result);
}



int main() {
    int ch;
    while (1) {
        printf("\n1.Transmitter 2.Receiver 3.Exit: ");
        scanf("%d", &ch);
        if (ch == 1) transmitter();
        else if (ch == 2) receiver();
        else if (ch == 3) break;
    }
    return 0;
}