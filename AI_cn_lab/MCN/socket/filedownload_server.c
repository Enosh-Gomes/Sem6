#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <stdlib.h>

#define PORT 9005
#define BUF_SIZE 1024

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server = {AF_INET, htons(PORT), INADDR_ANY};

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    bind(server_fd, (struct sockaddr*)&server, sizeof(server));
    listen(server_fd, 1);

    printf("File Server listening on port %d...\n", PORT);
    client_fd = accept(server_fd, NULL, NULL);
    printf("Client connected.\n");

    char filename[100], buffer[BUF_SIZE];
    int bytes_read;

    read(client_fd, filename, sizeof(filename));
    FILE *fp = fopen(filename, "rb");
    if (fp == NULL) {
        strcpy(buffer, "ERROR: File not found");
        write(client_fd, buffer, strlen(buffer));
    } else {
        while ((bytes_read = fread(buffer, 1, BUF_SIZE, fp)) > 0) {
            write(client_fd, buffer, bytes_read);
        }
        printf("File sent successfully.\n");
        fclose(fp);
    }

    close(client_fd);
    close(server_fd);
    return 0;
}
