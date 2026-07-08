import heapq

def dijkstra(graph, start):
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()
    print("---------------------")
    print("Initial Routing Table")
    print("---------------------")
    for node in distances:
        print(f"Router {node} --> {distances[node]}")
    while priority_queue:
        current_distance, current_router = heapq.heappop(priority_queue)
        if current_router in visited:
            continue
        visited.add(current_router)
        print("-------------------")
        print(f"Processing Router {current_router}")
        print("-------------------")
        for neighbor, weight in graph[current_router]:
            print(f"Checking Path:")
            print(f"{current_router} --> {neighbor}")
            print(f"Link Cost = {weight}")
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                old_distance = distances[neighbor]
                distances[neighbor] = new_distance
                print(f"Updating Router {neighbor}")
                print(f"Old Distance = {old_distance}")
                print(f"New Distance = {new_distance}")
                heapq.heappush(priority_queue, (new_distance, neighbor))
            else:
                print("No Update Required")
            print()
        print("------------------------------")
        print("Routing Table After Processing")
        print("------------------------------")
        for node in distances:
            print(f"Router {node} --> {distances[node]}")
    print("\nFinal Routing Table")
    print("------------------------------------------")
    print("Destination Router\tShortest Distance")
    print("------------------------------------------")
    for node in distances:
        print(f"{node}\t\t\t{distances[node]}")
    print("------------------------------------------")

if __name__ == "__main__":
    graph = {}
    n = int(input("Enter the number of routers: "))
    print("\nEnter neighbors and costs in the format:")
    print("neighbor cost")
    print("Enter -1 -1 to stop entering neighbors for a router.")
    for router in range(n):
        graph[router] = []
        print(f"\nRouter {router}:")
        while True:
            neighbor, cost = map(int, input("Enter neighbor and cost: ").split())
            if neighbor == -1 and cost == -1:
                break
            graph[router].append((neighbor, cost))
    start = int(input("\nEnter the starting router: "))
    dijkstra(graph, start)

'''
6
1 4
2 2
-1 -1
0 4
2 1
3 5
-1 -1
0 2
1 1
3 8
4 10
-1 -1
1 5
2 8
4 2
5 6
-1 -1
2 10
3 2
5 3
-1 -1
3 6
4 3
-1 -1
0
'''