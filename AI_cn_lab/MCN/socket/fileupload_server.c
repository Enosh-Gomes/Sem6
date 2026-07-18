#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 9006
#define BUF_SIZE 1024

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server = {AF_INET, htons(PORT), INADDR_ANY};

    char buffer[BUF_SIZE];
    int bytes_received;

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    bind(server_fd, (struct sockaddr*)&server, sizeof(server));
    listen(server_fd, 1);

    printf("File Server listening on port %d...\n", PORT);
    client_fd = accept(server_fd, NULL, NULL);
    printf("Client connected.\n");

    FILE *fp = fopen("uploaded_file.txt", "wb");
    if (fp == NULL) {
        perror("File open failed");
        return 1;
    }

    while ((bytes_received = read(client_fd, buffer, BUF_SIZE)) > 0) {
        fwrite(buffer, 1, bytes_received, fp);
        if (bytes_received < BUF_SIZE) break; // end of file
    }

    printf("File received and saved as 'uploaded_file.txt'.\n");

    fclose(fp);
    close(client_fd);
    close(server_fd);
    return 0;
}
