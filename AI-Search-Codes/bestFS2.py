def bestFS(graph, heuristic, start, goal):
    visited = set()
    queue = [(heuristic[start], [start])]  # (heuristic value, path)

    while queue:
        queue.sort()  # Sort by heuristic (ascending)
        h, path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((heuristic[neighbor], new_path))

    return None

# -----------------------------
# Step 1: User Input for Graph
# -----------------------------
def input_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node name: ").strip()
        neighbors = input(f"Enter neighbors of {node} : ").split(" ")
        graph[node] = neighbors
    return graph

# -----------------------------
# Step 2: User Input for Heuristics
# -----------------------------
def input_heuristics():
    heuristic = {}
    n = int(input("Enter number of heuristic values: "))
    for _ in range(n):
        node = input("Enter node name for heuristic: ").strip()
        value = int(input(f"Enter heuristic value for {node}: "))
        heuristic[node] = value
    return heuristic

# -----------------------------
# Step 3: Start, Goal and Execution
# -----------------------------
graph = input_graph()
heuristic = input_heuristics()
start = input("Enter start node: ").strip()
goal = input("Enter goal node: ").strip()

path = bestFS(graph, heuristic, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found.")
