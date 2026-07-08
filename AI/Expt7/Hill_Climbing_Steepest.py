goal = ""
graph = {}
heuristics = {}
Nil = None
isAscending = False

def GoalTest(node):
    return node == goal

def MoveGen(node):
    return graph.get(node, [])

def h(node):
    return heuristics.get(node, 99)

def Steepest_Descent(start):
    node = start
    path = [node]
    visited = set([node])
    iteration = 1

    print(f"\n{'Iteration':<12} {'Current':<10} {'Neighbors (h)':<35} {'Best Move':<10}")

    while True:
        neighbors = [n for n in MoveGen(node) if n not in visited]

        if not neighbors:
            print(f"{iteration:<12} {node:<10} {'[]':<35} {'STOP'}")
            return path

        neighbor_pairs = [(n, h(n)) for n in neighbors]

        if isAscending:
            best_node, best_h = max(neighbor_pairs, key=lambda x: x[1])
        else:
            best_node, best_h = min(neighbor_pairs, key=lambda x: x[1])

        print(f"{iteration:<12} {node:<10} {str(neighbor_pairs):<35} {best_node}")

        if (isAscending and best_h <= h(node)) or (not isAscending and best_h >= h(node)):
            print("\nNo better neighbor. Local Optimum reached")
            return path

        node = best_node
        path.append(node)
        visited.add(node)

        if GoalTest(node):
            return path

        iteration += 1


def Get_Input():
    global goal, graph, heuristics, isAscending

    n = int(input("Enter the number of nodes: "))

    for _ in range(n):
        name = input("\nNode: ").strip()
        val = int(input("Heuristics: "))
        children = input("Neighbors: ").strip()

        heuristics[name] = val
        graph[name] = [c.strip() for c in children.split()] if children else []

    start = input("\nEnter start node: ").strip()
    goal = input("Enter goal node: ").strip()

    if heuristics[start] < heuristics[goal]:
        isAscending = True
    else:
        isAscending = False

    return start

start = Get_Input()
path = Steepest_Descent(start)

if path:
    print(f"\nPath: {' -> '.join(path)}")
else:
    print("\nNo path found.")
    
'''
8
S
17
A B C
A
10
E
B
13
E D
C
4
D
D
6
F
E
12
F
F
1
G
G
0

S
G
'''