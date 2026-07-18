#include <stdio.h>

#define INF 9999
#define n 3  // number of routers

// Function to print the path from src to dest
void print_path(int via[][n], int src, int dest) {
    if (src == dest) {
        printf("%d", src);
        return;
    }

    if (via[src][dest] == -1) {
        printf("No path");
        return;
    }

    printf("%d", src);
    int next = via[src][dest];
    while (next != dest && next != -1) {
        printf(" -> %d", next);
        next = via[next][dest];
    }
    if (next == -1)
        printf(" -> No path");
    else
        printf(" -> %d", dest);
}

int main() {
    int cost[n][n], dist[n][n], via[n][n];

    printf("Enter the cost matrix (%d for no link):\n", INF);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &cost[i][j]);
            dist[i][j] = cost[i][j];

            if (i == j || cost[i][j] == INF)
                via[i][j] = -1;
            else
                via[i][j] = j;
        }
    }

    // Distance Vector update logic
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (dist[i][k] != INF && dist[k][j] != INF &&
                    dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    via[i][j] = via[i][k];
                }
            }
        }
    }

    // Show final routing table and paths
    for (int i = 0; i < n; i++) {
        printf("\nRouting table for Router %d:\n", i);
        printf("Dest\tNextHop\tCost\tPath\n");
        for (int j = 0; j < n; j++) {
            printf("%d\t", j);
            if (via[i][j] == -1)
                printf("-\t");
            else
                printf("%d\t", via[i][j]);

            if (dist[i][j] == INF)
                printf("-\t");
            else
                printf("%d\t", dist[i][j]);

            print_path(via, i, j);
            printf("\n");
        }
    }

    return 0;
}
