#include <iostream>
using namespace std;
#define MAX 101
#define INF 99999
int graph[MAX][MAX];
int dist[MAX], parent[MAX];
bool visited[MAX];
void printPath(int node) {
    if (node == -1) return;
    printPath(parent[node]);
    cout << node << " ";
}
int main() {
    int n, m, u, v, w, start, end;
    cout << "Enter number of nodes and edges: ";
    cin >> n >> m;
    for (int i = 0; i < MAX; i++)
        for (int j = 0; j < MAX; j++)
            graph[i][j] = INF;
    cout << "Enter edges (source destination cost):\n";
    int minNode = INF, maxNode = -1;
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> w;
        graph[u][v] = w;
        if (u < minNode) minNode = u;
        if (v < minNode) minNode = v;
        if (u > maxNode) maxNode = u;
        if (v > maxNode) maxNode = v;
    }
    cout << "Enter start and end node: ";
    cin >> start >> end;
    for (int i = 0; i < MAX; i++) {
        dist[i] = INF;
        visited[i] = false;
        parent[i] = -1;
    }
    dist[start] = 0;
    int startIdx = minNode;
    int endIdx = maxNode;
    for (int count = startIdx; count <= endIdx; count++) {
        int minDist = INF, u = -1;
        for (int i = startIdx; i <= endIdx; i++) {
            if (!visited[i] && dist[i] < minDist) {
                minDist = dist[i];
                u = i;
            }
        }
        if (u == -1) break;
        visited[u] = true;
        for (int v = startIdx; v <= endIdx; v++) {
            if (!visited[v] && graph[u][v] != INF && dist[v] > dist[u] + graph[u][v]) {
                dist[v] = dist[u] + graph[u][v];
                parent[v] = u;
            }
        }
    }
    if (dist[end] == INF)
        cout << "No path found.\n";
    else {
        cout << "Shortest path cost: " << dist[end] << "\nPath: ";
        printPath(end);
        cout << "\n";
    }
    return 0;
}
