#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define port 7070

int main(){
    int server_fd,client_fd;
    struct sockaddr_in servaddr;
    server_fd=socket(AF_INET,SOCK_STREAM,0);
    servaddr.sin_family=AF_INET;
    servaddr.sin_port=htons(port);
    servaddr.sin_addr.s_addr=INADDR_ANY;

    bind(server_fd,(struct sockaddr*)&servaddr,sizeof(servaddr));
    listen(server_fd,1);

    client_fd=accept(server_fd,NULL,NULL);

    int a,b;
    char op;
    int result;

    read(client_fd,&a,sizeof(a));
    read(client_fd,&b,sizeof(b));
    read(client_fd,&op,sizeof(op));

    switch(op){
        case '+':result=a+b;
        break;
        case '-':result=a-b;
        break;
        case '*':result=a*b;
        break;
        case '/':result=(b==0)?0:a/b;   
        break;
        default: result=0;
    }

    write(client_fd,&result,sizeof(result));

    close(server_fd);
    close(client_fd);
    return 0;
}