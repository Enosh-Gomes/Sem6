import heapq
def bestfs(start, goal, graph, heuristic):
    visited = []
    parent = {start: None}
    queue = [(heuristic[start], start, parent[start])]
    OPEN = f"({start.upper()}, {parent[start]}, {heuristic[start]})"
    CLOSED = ""
    print(f"\n{'OPEN':<{75}} | {'CLOSED'}")
    print("-" * (150))
    print(f"{OPEN:<75} | {CLOSED:<75}")
    while queue:
        h, node, par = heapq.heappop(queue)
        if node not in visited:
            visited.append(node)
            if node != goal and node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        if neighbor not in parent:
                            parent[neighbor] = node
                        heapq.heappush(queue, (heuristic[neighbor], neighbor, parent[neighbor]))
            if node == goal:
                print("Goal Found!")
                break
            OPEN = ", ".join([f"({n.upper()}, {p}, {abs(h)})" for h, n, p in sorted(queue)])
            CLOSED = ", ".join([f"({n.upper()}, {parent[n]}, {abs(heuristic[n])})" for n in reversed(visited)])
            print(f"{OPEN:<{75}} | {CLOSED:<{75}}")
    path = []
    current = goal
    if current in visited:
        while current is not None:
            path.append(current)
            current = parent.get(current)
        path.reverse()
        return " -> ".join([p.upper() for p in path])
    else:
        return "Goal not reachable"
if __name__ == "__main__":
    graph = {}
    heuristics = {}
    print("Enter Node, Heuristic and Neighbours. Press Enter twice when done:")
    while True:
        line = input()
        if not line.strip():
            break
        parts = line.split()
        node = parts[0]
        heuristics[node] = int(parts[1])
        graph[node] = parts[2:]
    start_node = input("Enter the starting node: ")
    goal_node = input("Enter the goal node: ")
    if heuristics[start_node] < heuristics[goal_node]:
        for node in heuristics:
            heuristics[node] = -heuristics[node]
    final_path = bestfs(start_node, goal_node, graph, heuristics)
    print(f"\nPath: {final_path}")


'''
S 17 A B C
A 10 E S
B 13 E D S
C 4 D S
D 2 F B C
E 4 A B F
F 1 E D G
G 0

S
G

'''