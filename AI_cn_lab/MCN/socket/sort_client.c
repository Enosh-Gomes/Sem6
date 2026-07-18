#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define SIZE 10

int main() {
    int sockfd;
    struct sockaddr_in server = {AF_INET, htons(9004)};
    inet_pton(AF_INET, "127.0.0.1", &server.sin_addr);

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    connect(sockfd, (struct sockaddr*)&server, sizeof(server));

    int arr[SIZE];
    printf("Enter 10 integers:\n");
    for (int i = 0; i < SIZE; i++)
        scanf("%d", &arr[i]);

    write(sockfd, arr, sizeof(arr));
    read(sockfd, arr, sizeof(arr));

    printf("Sorted array: ");
    for (int i = 0; i < SIZE; i++)
        printf("%d ", arr[i]);
    printf("\n");

    close(sockfd);
    return 0;
}
