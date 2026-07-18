#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define MAX 100

int main() {
    int sockfd;
    struct sockaddr_in server = {AF_INET, htons(9003)};
    inet_pton(AF_INET, "127.0.0.1", &server.sin_addr);

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    connect(sockfd, (struct sockaddr*)&server, sizeof(server));

    int arr[MAX], n, key;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d integers:\n", n);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    printf("Enter number to search: ");
    scanf("%d", &key);

    write(sockfd, &n, sizeof(n));
    write(sockfd, arr, sizeof(int) * n);
    write(sockfd, &key, sizeof(key));

    int found, pos;
    read(sockfd, &found, sizeof(found));
    read(sockfd, &pos, sizeof(pos));

    if (found)
        printf("Item found at position: %d\n", pos);
    else
        printf("Item not found in the array.\n");

    close(sockfd);
    return 0;
}
