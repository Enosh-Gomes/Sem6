#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define SIZE 10

void sortArray(int arr[]) {
    for (int i = 0; i < SIZE - 1; i++)
        for (int j = i + 1; j < SIZE; j++)
            if (arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
}

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server = {AF_INET, htons(9004), INADDR_ANY};

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    bind(server_fd, (struct sockaddr*)&server, sizeof(server));
    listen(server_fd, 1);

    printf("Sort Server listening on port 9004...\n");
    client_fd = accept(server_fd, NULL, NULL);
    printf("Client connected.\n");

    int arr[SIZE];
    read(client_fd, arr, sizeof(arr));

    sortArray(arr);

    write(client_fd, arr, sizeof(arr));

    close(client_fd);
    close(server_fd);
    return 0;
}
