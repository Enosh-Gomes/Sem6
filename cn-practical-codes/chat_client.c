#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>
#include <arpa/inet.h>

#define PORT 8090

void *receive(void *sock) {
    int fd = *(int*)sock;
    char msg[100];
    while (1) {
        read(fd, msg, sizeof(msg));
        printf("\nServer: %s\n", msg);
    }
    return NULL;
}

int main() {
    int sockfd;
    struct sockaddr_in servaddr;
    char msg[100];
    pthread_t recv_thread;

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);
    servaddr.sin_addr.s_addr = INADDR_ANY;

    connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr));

    pthread_create(&recv_thread, NULL, receive, &sockfd);

    while (1) {
        printf("You: ");
        fgets(msg, sizeof(msg), stdin);
        write(sockfd, msg, strlen(msg));
    }

    close(sockfd);
    return 0;
}