def a_star(graph, heuristics, start, goal):
    queue = [(heuristics[start], 0, [start])]  # (f, g, path)
    cost_so_far = {start: 0}

    while queue:
        # Sort by f = g + h
        queue.sort()
        f, g, path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        for neighbour, cost in graph.get(node, []):
            new_g = g + cost
            # Check if this path is better
            if neighbour not in cost_so_far or new_g < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_g
                new_f = new_g + heuristics[neighbour]
                new_path = path + [neighbour]
                queue.append((new_f, new_g, new_path))

    return None

graph = {}
heuristics = {}

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    neighbours = input("Enter neighbours with cost (e.g., B:2 C:3): ").split()
    graph[node] = []
    for item in neighbours:
        neighbor, cost = item.split(":")
        graph[node].append((neighbor, int(cost)))

for _ in range(n):
    node = input("Enter node for heuristic: ")
    h = int(input(f"Heuristic for {node}: "))
    heuristics[node] = h

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = a_star(graph, heuristics, start, goal)

if path:
    print("A* Path:", " -> ".join(path))
else:
    print("No path found.")