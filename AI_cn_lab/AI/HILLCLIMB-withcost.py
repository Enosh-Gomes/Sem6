def simple_hill_climb(graph, heuristics, start, goal):
    print("\nSimple Hill Climbing Path:")
    current = start
    path = [current]
    total_cost = 0

    while current != goal:
        neighbors = graph.get(current, [])
        next_node = None
        next_cost = None
        for neighbor, cost in neighbors:
            if heuristics[neighbor] < heuristics[current]:
                next_node = neighbor
                next_cost = cost
                break
        if not next_node:
            print("Stuck at:", current)
            break
        total_cost += next_cost
        path.append(next_node)
        current = next_node
    print(" -> ".join(path))
    print("Total Cost:", total_cost)

def steepest_ascent_hill_climb(graph, heuristics, start, goal):
    print("\nSteepest Ascent Hill Climbing Path:")
    current = start
    path = [current]
    total_cost = 0
    while current != goal:
        neighbors = graph.get(current, [])
        best_node = None
        best_cost = None
        for neighbor, cost in neighbors:
            if neighbor != current:
                if best_node is None or heuristics[neighbor] < heuristics[best_node]:
                    best_node = neighbor
                    best_cost = cost
        if best_node is None or heuristics[best_node] >= heuristics[current]:
            print("Stuck at:", current)
            break
        total_cost += best_cost
        path.append(best_node)
        current = best_node
    print(" -> ".join(path))
    print("Total Cost:", total_cost)
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
    u, v, c = input("Enter edge (from to cost): ").split()
    c = int(c)
    graph[u].append((v, c))
    graph[v].append((u, c))  # If undirected
start = input("Enter start node: ")
goal = input("Enter goal node: ")
simple_hill_climb(graph, heuristics, start, goal)
steepest_ascent_hill_climb(graph, heuristics, start, goal)
