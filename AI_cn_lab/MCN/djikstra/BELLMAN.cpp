#include <iostream>
using namespace std;
#define MAX 101
#define INF 99999

struct Edge {
    int u, v, w;
};

Edge edges[MAX * MAX];
int dist[MAX], parent[MAX];
void printPath(int node) {
    if (node == -1) return;
    printPath(parent[node]);
    cout << node << " ";
}
int main() {
    int n, m, u, v, w, start, end;
    cout << "Enter number of nodes and edges: ";
    cin >> n >> m;
    int minNode = INF, maxNode = -1;
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> w;
        edges[i] = {u, v, w};
        if (u < minNode) minNode = u;
        if (v < minNode) minNode = v;
        if (u > maxNode) maxNode = u;
        if (v > maxNode) maxNode = v;
    }
    cout << "Enter start and end node: ";
    cin >> start >> end;
    for (int i = 0; i < MAX; i++) {
        dist[i] = INF;
        parent[i] = -1;
    }
    dist[start] = 0;
    int indexStart = minNode;
    int indexEnd = maxNode;
    for (int i = indexStart; i <= indexEnd - 1; i++) {
        for (int j = 0; j < m; j++) {
            u = edges[j].u;
            v = edges[j].v;
            w = edges[j].w;
            if (dist[u] != INF && dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                parent[v] = u;
            }
        }
    }
    for (int j = 0; j < m; j++) {
        u = edges[j].u;
        v = edges[j].v;
        w = edges[j].w;
        if (dist[u] != INF && dist[v] > dist[u] + w) {
            cout << "Negative weight cycle detected!\n";
            return 0;
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
