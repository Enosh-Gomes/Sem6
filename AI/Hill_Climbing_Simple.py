def hill_climbing(graph, heuristic, start):
    node = start
    path = [node]

    while True:
        neighbors = graph.get(node, [])

        if not neighbors:
            print("No neighbors found. Stopping.")
            return node, path

        #sorted_neighbors = sorted(neighbors, key=lambda x: heuristic[x])

        newnode = neighbors[0]

        if heuristic[newnode] < heuristic[node]:
            node = newnode
            path.append(node)
        else:
            return node, path

if __name__ == "__main__":
    n = int(input("Enter number of nodes: "))
    
    nodes = []
    print("Enter node names:")
    for _ in range(n):
        nodes.append(input().strip())
        
    graph = {}
    print("\nEnter adjacency list for each node:")
    for node in nodes:
        neighbors = input(f"Neighbors of {node} (space-separated): ").split()
        graph[node] = neighbors
        
    heuristic = {}
    print("\nEnter heuristic values h(n):")
    for node in nodes:
        h_val = float(input(f"h({node}) = "))
        heuristic[node] = h_val
        
    start = input("\nEnter start node: ")
    
    result, path = hill_climbing(graph, heuristic, start)
    
    if heuristic[result] == 0:
        print("\nGoal node reached!")
    else:
        print("\nLocal optimum reached without finding goal.")
    
    print("\nPath followed:", " -> ".join(path))
    print("Final node:", result)
    print("Heuristic value:", heuristic[result])

'''
8
S
A
B
C
D
E
F
G

A B C
E
E D
D
F
F
G

17
10
13
4
2
4
1
0
S

'''