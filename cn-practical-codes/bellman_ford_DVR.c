#include <stdio.h>

#define INF 9999
#define N 3  // number of routers

int main() {
    int cost[N][N], dist[N][N], via[N][N];

    printf("Enter the cost matrix (%d for no link):\n", INF);
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            scanf("%d", &cost[i][j]);
            dist[i][j] = cost[i][j];
            via[i][j] = j;
        }

    // Distance Vector update (Bellman-Ford logic)
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                if (dist[i][j] > cost[i][k] + dist[k][j]) {
                    dist[i][j] = cost[i][k] + dist[k][j];
                    via[i][j] = k;
                }
            }
        }
    }

    // Show final table for each router
    for (int i = 0; i < N; i++) {
        printf("\nRouting table for Router %d:\n", i);
        printf("Dest\tNextHop\tCost\n");
        for (int j = 0; j < N; j++) {
            printf("%d\t%d\t%d\n", j, via[i][j], dist[i][j]);
        }
    }

    return 0;
}
