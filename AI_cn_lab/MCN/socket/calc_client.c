#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

int main() {
    int sockfd;
    struct sockaddr_in server = {AF_INET, htons(9002)};
    inet_pton(AF_INET, "127.0.0.1", &server.sin_addr);

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    connect(sockfd, (struct sockaddr*)&server, sizeof(server));

    int a, b, result;
    char op;
    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter operator (+ - * /): ");
    scanf(" %c", &op); // space before %c to consume newline
    printf("Enter second number: ");
    scanf("%d", &b);

    write(sockfd, &a, sizeof(a));
    write(sockfd, &b, sizeof(b));
    write(sockfd, &op, sizeof(op));

    read(sockfd, &result, sizeof(result));
    printf("Result: %d\n", result);

    close(sockfd);
    return 0;
}
