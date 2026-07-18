#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <stdlib.h>

#define PORT 9005
#define BUF_SIZE 1024

int main() {
    int sockfd;
    struct sockaddr_in server = {AF_INET, htons(PORT)};
    inet_pton(AF_INET, "127.0.0.1", &server.sin_addr);

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    connect(sockfd, (struct sockaddr*)&server, sizeof(server));

    char filename[100], buffer[BUF_SIZE];
    printf("Enter filename to download: ");
    scanf("%s", filename);

    write(sockfd, filename, strlen(filename) + 1);

    FILE *fp = fopen("downloaded_file.txt", "wb");
    int bytes_read;
    while ((bytes_read = read(sockfd, buffer, BUF_SIZE)) > 0) {
        fwrite(buffer, 1, bytes_read, fp);
        if (bytes_read < BUF_SIZE) break; // end of file
    }

    fclose(fp);
    printf("File downloaded and saved as 'downloaded_file.txt'.\n");

    close(sockfd);
    return 0;
}
