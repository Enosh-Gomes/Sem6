#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 9006
#define BUF_SIZE 1024

int main() {
    int sockfd;
    struct sockaddr_in server = {AF_INET, htons(PORT)};
    inet_pton(AF_INET, "127.0.0.1", &server.sin_addr);

    char filename[100], buffer[BUF_SIZE];
    int bytes_read;

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    connect(sockfd, (struct sockaddr*)&server, sizeof(server));

    printf("Enter filename to upload: ");
    scanf("%s", filename);

    FILE *fp = fopen(filename, "rb");
    if (fp == NULL) {
        perror("File not found");
        return 1;
    }

    while ((bytes_read = fread(buffer, 1, BUF_SIZE, fp)) > 0) {
        write(sockfd, buffer, bytes_read);
    }

    fclose(fp);
    printf("File '%s' uploaded to server.\n", filename);

    close(sockfd);
    return 0;
}
