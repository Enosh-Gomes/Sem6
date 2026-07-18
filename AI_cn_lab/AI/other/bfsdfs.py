from collections import deque

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
                print("\nBFS Traversal Order:", traversal)
                print("Path from", start, "to", goal, ":", " -> ".join(path))
                return
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    print("No path found from", start, "to", goal)

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
    print("\nDFS Traversal Order:", traversal)
    if goal_path:
        print("Path from", start, "to", goal, ":", " -> ".join(goal_path))
    else:
        print("No path found from", start, "to", goal)

def main():
    print("Graph Traversal using BFS and DFS\n")
    n = int(input("Enter number of nodes: "))
    graph = {}
    for i in range(n):
        node = input(f"Enter name of node {i+1}: ")
        neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
        graph[node] = neighbors
    start = input("\nEnter start node: ")
    goal = input("Enter goal node: ")
    print("\nChoose Traversal Algorithm:")
    print("1. BFS")
    print("2. DFS")
    choice = input("Enter choice (1 or 2): ")
    if choice == '1':
        bfs(graph, start, goal)
    elif choice == '2':
        dfs(graph, start, goal)
    else:
        print("Invalid choice.")
main()
