#include <stdio.h>

unsigned char computeChecksum(char * data, int len){
    int sum=0;
     for (int i = 0; i < len; i++) {
        sum+= data[i]; 
    }

     while(sum >> 8)
         sum=(sum & 0xFF) + (sum >> 8);


return 0xFF-sum;
}


int main(){
    char data[]="MCN";
    int len=sizeof(data)-1;
    unsigned char checksum = computeChecksum(data, len);
    printf("Sender:\n");
    printf("Data: %s\n", data);
    printf("Checksum: 0x%X\n\n", checksum);

    // Receiver side
    char receivedData[100];
    unsigned char receivedChecksum;

    //data[0]='a';

    // Simulate receiving data and checksum
    for (int i = 0; i < len; i++) {
        receivedData[i] = data[i]; 
    }
    receivedChecksum = checksum;

     // Compute total sum at receiver (including checksum)
    int totalSum = 0;
    for (int i = 0; i < len; i++) {
        totalSum += receivedData[i];
    }
    totalSum += receivedChecksum;

    while(totalSum >> 8)
    totalSum=(totalSum & 0xFF) + (totalSum >> 8);

    printf("Receiver:\n");
    printf("Received Data: %s\n", receivedData);
    printf("Received Checksum: 0x%X\n", receivedChecksum);
    printf("Sum + Checksum: 0x%X\n", totalSum);

    if (totalSum == 0xFF)
        printf(" Data received correctly. No error.\n");
    else
        printf("Data corrupted! Error detected.\n");

    return 0;
}