from collections import deque
n = int(input("Enter number of nodes: "))
graph = {}
for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors
start = input("Enter start node: ")
goal = input("Enter goal node: ")

def dfs(graph, start, goal):
    visited = set()
    traversal = []
    goal_path = []

    def dfs_util(node, path):
        nonlocal goal_path
        visited.add(node)
        traversal.append(node)
        path.append(node)
        if node == goal and not goal_path:
            goal_path = list(path)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_util(neighbor, path)
        path.pop()  # backtrack
    dfs_util(start, [])
    print("DFS Traversal Order:", traversal)
    if goal_path:
        print("Path from", start, "to", goal, ":", " -> ".join(goal_path))
    else:
        print("No path found from", start, "to", goal)

dfs(graph, start, goal)

