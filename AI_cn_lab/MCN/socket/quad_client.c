#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int sockfd;
    struct sockaddr_in server = {AF_INET, htons(9001)};
    inet_pton(AF_INET, "127.0.0.1", &server.sin_addr);

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    connect(sockfd, (struct sockaddr*)&server, sizeof(server));

    float a, b, c;
    printf("Enter coefficients a, b, c: ");
    scanf("%f %f %f", &a, &b, &c);

    write(sockfd, &a, sizeof(a));
    write(sockfd, &b, sizeof(b));
    write(sockfd, &c, sizeof(c));

    char result[100];
    read(sockfd, result, sizeof(result));
    printf("Server response: %s\n", result);

    close(sockfd);
    return 0;
}
