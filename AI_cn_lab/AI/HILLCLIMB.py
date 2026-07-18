def simple_hill_climb(graph, heuristics, start, goal):
    print("\nSimple Hill Climbing Path:")
    current = start
    path = [current]
    while current != goal:
        neighbors = graph.get(current, [])
        next_node = None
        for neighbor in neighbors:
            if heuristics[neighbor] < heuristics[current]:
                next_node = neighbor
                break
        if not next_node:
            print("Stuck at:", current)
            break
        path.append(next_node)
        current = next_node
    print(" -> ".join(path))

def steepest_ascent_hill_climb(graph, heuristics, start, goal):
    print("\nSteepest Ascent Hill Climbing Path:")
    current = start
    path = [current]
    while current != goal:
        neighbors = graph.get(current, [])
        best = None
        for neighbor in neighbors:
            if neighbor != current:
                if best is None or heuristics[neighbor] < heuristics[best]:
                    best = neighbor
        if best is None or heuristics[best] >= heuristics[current]:
            print("Stuck at:", current)
            break
        path.append(best)
        current = best
    print(" -> ".join(path))

graph = {}
heuristics = {}

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    h = int(input(f"Heuristic of {node}: "))
    heuristics[node] = h
    graph[node] = []

e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v = input("Enter edge (from to): ").split()
    graph[u].append(v)
    graph[v].append(u)  # If undirected

start = input("Enter start node: ")
goal = input("Enter goal node: ")

simple_hill_climb(graph, heuristics, start, goal)
steepest_ascent_hill_climb(graph, heuristics, start, goal)
