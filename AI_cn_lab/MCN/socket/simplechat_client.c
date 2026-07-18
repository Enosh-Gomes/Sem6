#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define PORT 9007
#define BUF_SIZE 1024

int main() {
    int sockfd;
    struct sockaddr_in server = {AF_INET, htons(PORT)};
    inet_pton(AF_INET, "127.0.0.1", &server.sin_addr);
    char buffer[BUF_SIZE];

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    connect(sockfd, (struct sockaddr*)&server, sizeof(server));
    printf("Connected to chat server. Type 'exit' to quit.\n");

    while (1) {
        // Send message
        printf("Client: ");
        fgets(buffer, BUF_SIZE, stdin);
        write(sockfd, buffer, strlen(buffer));
        if (strcmp(buffer, "exit\n") == 0) break;

        // Receive reply
        memset(buffer, 0, BUF_SIZE);
        read(sockfd, buffer, BUF_SIZE);
        if (strcmp(buffer, "exit\n") == 0) break;
        printf("Server: %s", buffer);
    }

    close(sockfd);
    return 0;
}
