#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define port 7070

int main(){
    int sock_fd;
    struct sockaddr_in servaddr;
    sock_fd=socket(AF_INET,SOCK_STREAM,0);
    servaddr.sin_family=AF_INET;
    servaddr.sin_port=htons(port);
    servaddr.sin_addr.s_addr=inet_addr("127.0.0.1");

    connect(sock_fd,(struct sockaddr*)&servaddr,sizeof(servaddr));


    int a,b;
    char op;
    int result;

   printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    getchar(); // consume leftover newline
    printf("Enter operator (+, -, *, /): ");
    scanf("%c", &op);

    write(sock_fd,&a,sizeof(a));
    write(sock_fd,&b,sizeof(b));
    write(sock_fd,&op,sizeof(op));


    read(sock_fd,&result,sizeof(result));
    printf("result:%d",result);

    close(sock_fd);
    return 0;
}