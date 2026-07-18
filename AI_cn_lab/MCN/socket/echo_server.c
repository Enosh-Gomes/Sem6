#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 9008
#define BUF_SIZE 1024

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server = {AF_INET, htons(PORT), INADDR_ANY};
    char buffer[BUF_SIZE];

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    bind(server_fd, (struct sockaddr*)&server, sizeof(server));
    listen(server_fd, 1);

    printf("Echo Server listening on port %d...\n", PORT);
    client_fd = accept(server_fd, NULL, NULL);
    printf("Client connected.\n");

    while (1) {
        memset(buffer, 0, BUF_SIZE);
        int bytes = read(client_fd, buffer, BUF_SIZE);
        if (bytes <= 0 || strcmp(buffer, "exit\n") == 0)
            break;

        printf("Received: %s", buffer);
        write(client_fd, buffer, strlen(buffer)); // echo
    }

    close(client_fd);
    close(server_fd);
    return 0;
}
