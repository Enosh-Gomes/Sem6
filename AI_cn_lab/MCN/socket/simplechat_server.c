#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define PORT 9007
#define BUF_SIZE 1024

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server = {AF_INET, htons(PORT), INADDR_ANY};
    char buffer[BUF_SIZE];

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    bind(server_fd, (struct sockaddr*)&server, sizeof(server));
    listen(server_fd, 1);

    printf("Chat server listening on port %d...\n", PORT);
    client_fd = accept(server_fd, NULL, NULL);
    printf("Client connected.\n");

    while (1) {
        // Receive message
        memset(buffer, 0, BUF_SIZE);
        read(client_fd, buffer, BUF_SIZE);
        if (strcmp(buffer, "exit\n") == 0) break;
        printf("Client: %s", buffer);

        // Send reply
        printf("Server: ");
        fgets(buffer, BUF_SIZE, stdin);
        write(client_fd, buffer, strlen(buffer));
        if (strcmp(buffer, "exit\n") == 0) break;
    }

    close(client_fd);
    close(server_fd);
    return 0;
}
