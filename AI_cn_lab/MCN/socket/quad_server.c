#include <stdio.h>
#include <math.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server = {AF_INET, htons(9001), INADDR_ANY};

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    bind(server_fd, (struct sockaddr*)&server, sizeof(server));
    listen(server_fd, 1);

    printf("Server is listening on port 9001...\n");
    client_fd = accept(server_fd, NULL, NULL);
    printf("Client connected.\n");

    float a, b, c;
    read(client_fd, &a, sizeof(a));
    read(client_fd, &b, sizeof(b));
    read(client_fd, &c, sizeof(c));

    float d = b*b - 4*a*c;
    char result[100];

    if (d < 0)
        strcpy(result, "No real roots");
    else {
        float r1 = (-b + sqrt(d)) / (2*a);
        float r2 = (-b - sqrt(d)) / (2*a);
        snprintf(result, sizeof(result), "Roots: %.2f and %.2f", r1, r2);
    }

    write(client_fd, result, strlen(result));
    close(client_fd); close(server_fd);
    return 0;
}
