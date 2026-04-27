'''
import random

def hill_climbing(objective_function, initial_solution, neighbors_func, max_iterations=100):
    current_solution = initial_solution
    current_value = objective_function(current_solution)
    
    for iteration in range(max_iterations):
        neighbors = neighbors_func(current_solution)
        
        best_neighbor = None
        best_neighbor_value = current_value
        
        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor)

            if neighbor_value > best_neighbor_value:
                best_neighbor = neighbor
                best_neighbor_value = neighbor_value
        
        iteration += 1
        
        if best_neighbor is None:
            break
        
        current_solution = best_neighbor
        current_value = best_neighbor_value
    
    return current_solution, current_value

if __name__ == "__main__":
    def objective(x):
        return -(x - 5)**2 + 25
    
    def neighbors(x):
        return [x + 1, x - 1]
    
    initial = random.uniform(0, 10)
    solution, value = hill_climbing(objective, initial, neighbors)
    
    print(f"Best solution: {solution}")
    print(f"Best value: {value}")
'''

'''
def Hill_Climbing(graph, start, goal, heuristic):
    current = start
    while current != goal:
        print(f"Current node: {current}, Heuristic: {heuristic[current]}")
        neighbors = graph[current]
        best_neighbor = None
        best_heuristic = float('inf')
        
        for neighbor in neighbors:
            if heuristic[neighbor] < best_heuristic:
                best_heuristic = heuristic[neighbor]
                best_neighbor = neighbor
        
        if best_heuristic >= heuristic[current]:
            print("No better neighbor found. Stopping.")
            return None
        
        current = best_neighbor
    
    print(f"Goal reached: {current}")
    return current

n = int(input("Enter number of nodes: "))
nodes = []
graph = {}
heuristic = {}
print("Enter node names:")
for i in range(n):
    node = input()
    nodes.append(node)
    graph[node] = []
print("\nEnter adjacency list for each node")
for node in nodes:
    adj = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = adj
print("\nEnter heuristic values")
for node in nodes:
    h = int(input(f"Heuristic value of {node}: "))
    heuristic[node] = h
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

Hill_Climbing(graph, start, goal, heuristic)
'''


def hill_climbing(graph, heuristic, start):
    node = start
    path = [node]

    while True:
        neighbors = graph.get(node, [])

        if not neighbors:
            print("No neighbors found. Stopping.")
            return node, path

        sorted_neighbors = sorted(neighbors, key=lambda x: heuristic[x])

        newnode = sorted_neighbors[0]

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
    
    print("\nPath followed:", " -> ".join(path))
    print("Final node (local optimum):", result)
    print("Heuristic value:", heuristic[result])