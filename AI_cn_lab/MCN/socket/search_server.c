#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define MAX 100

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server = {AF_INET, htons(9003), INADDR_ANY};

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    bind(server_fd, (struct sockaddr*)&server, sizeof(server));
    listen(server_fd, 1);

    printf("Search Server listening on port 9003...\n");
    client_fd = accept(server_fd, NULL, NULL);
    printf("Client connected.\n");

    int n, arr[MAX], key, found = 0, pos = -1;

    read(client_fd, &n, sizeof(n));
    read(client_fd, arr, sizeof(int) * n);
    read(client_fd, &key, sizeof(key));

    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            found = 1;
            pos = i;
            break;
        }
    }

    write(client_fd, &found, sizeof(found));
    write(client_fd, &pos, sizeof(pos));

    close(client_fd);
    close(server_fd);
    return 0;
}
