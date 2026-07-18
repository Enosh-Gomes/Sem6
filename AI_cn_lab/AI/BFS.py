from collections import deque
n = int(input("Enter number of nodes: "))
graph = {}
for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors
start = input("Enter start node: ")
goal = input("Enter goal node: ")

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    traversal = []
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            if node == goal:
                print("BFS Traversal Order:", traversal)
                print("Path from", start, "to", goal, ":", " -> ".join(path))
                return
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    print("No path found from", start, "to", goal)
bfs(graph, start, goal)
