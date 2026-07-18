#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server = {AF_INET, htons(9002), INADDR_ANY};

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    bind(server_fd, (struct sockaddr*)&server, sizeof(server));
    listen(server_fd, 1);

    printf("Calculator Server listening on port 9002...\n");
    client_fd = accept(server_fd, NULL, NULL);
    printf("Client connected.\n");

    int a, b, result;
    char op;

    read(client_fd, &a, sizeof(a));
    read(client_fd, &b, sizeof(b));
    read(client_fd, &op, sizeof(op));

    switch (op) {
        case '+': result = a + b; break;
        case '-': result = a - b; break;
        case '*': result = a * b; break;
        case '/': result = (b != 0) ? a / b : 0; break;
        default:  result = 0;
    }

    write(client_fd, &result, sizeof(result));
    close(client_fd); close(server_fd);
    return 0;
}
