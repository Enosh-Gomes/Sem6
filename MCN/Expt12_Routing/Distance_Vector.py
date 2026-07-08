def bellman_ford(graph, vertices, source):
    distance = [float('inf')] * vertices
    distance[source] = 0
    print("\n---------------------")
    print("Initial Routing Table")
    print("---------------------")
    for i in range(vertices):
        print(f"Router {i} --> {distance[i]}")
    for iteration in range(vertices - 1):
        print("\n-----------")
        print(f"Iteration {iteration + 1}")
        print("-----------\n")
        updated = False
        for u, v, w in graph:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                old_distance = distance[v]
                distance[v] = distance[u] + w
                updated = True
                print(f"Updating Router {v}")
                print(f"Path: Router {u} --> Router {v}")
                print(f"Edge Cost = {w}")
                print(f"Old Distance = {old_distance}")
                print(f"New Distance = {distance[v]}\n")
        print("-----------------------------")
        print("Routing Table After Iteration")
        print("-----------------------------\n")
        for i in range(vertices):
            print(f"Router {i} --> {distance[i]}")
        if not updated:
            print("\nNo further updates possible.")
            print("Shortest paths already found.")
            break
    print("\nFinal Routing Table")
    print("----------------------------------------")
    print("Destination Router\tMinimum Distance")
    print("----------------------------------------")
    for i in range(vertices):
        print(f"{i}\t\t\t{distance[i]}")
    print("----------------------------------------")

if __name__ == "__main__":
    graph = []
    vertices = int(input("Enter the number of routers: "))
    print("\nEnter edges in the format:")
    print("source destination cost")
    print("Enter -1 -1 -1 to stop entering edges.\n")
    while True:
        src, dest, cost = map(int, input("Enter source, destination and cost: ").split())
        if src == -1 and dest == -1 and cost == -1:
            break
        graph.append((src, dest, cost))
    source = int(input("\nEnter the source router: "))
    bellman_ford(graph, vertices, source)

'''
7
0 1 6
0 2 5
0 3 5
1 4 -1
2 1 -2
2 4 1
3 2 -2
3 5 -1
4 6 3
5 6 3
-1 -1 -1
0
'''