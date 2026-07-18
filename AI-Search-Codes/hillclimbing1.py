def simple_hill(graph, heuristics, start, goal):
    current=start
    h=heuristics[current]
    best_h=h
    path=[current]
    while True:
        found=False
        for neighbour in graph.get(current,[]):
            if best_h > heuristics[neighbour]:
                best_h=heuristics[neighbour]
                current=neighbour
                found=True
                path.append(current)
                break
            
        if found ==False:
            break
        
        if current==goal:
            return path
        
    return path if current==goal else None
            
            
def steep_hill(graph, heuristics, start, goal):
    current = start
    path = [current]

    while True:
        neighbours = graph.get(current, [])
        best_h = heuristics[current]
        best_neighbor = None

        # Find the best neighbor (steepest descent)
        for neighbour in neighbours:
            if heuristics[neighbour] < best_h:
                best_h = heuristics[neighbour]
                best_neighbor = neighbour

        # If no better neighbor found, we're at a local maximum
        if best_neighbor is None:
            break

        # Move to the best neighbor
        current = best_neighbor
        path.append(current)

        if current == goal:
            return path

    return path if current == goal else None

        


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

heuristics = {
    'A': 10,
    'B': 8,
    'C': 9,
    'D': 7,
    'E': 5,
    'F': 6,
    'G': 0
}
 
start = 'A'
goal = 'G'

path1 = simple_hill(graph, heuristics, start, goal)
print("Simple Hill Climbing Path:", " -> ".join(path1) if path1 else "Failed")

path2 = steep_hill(graph, heuristics, start, goal)
print("Steepest Ascent Path:", " -> ".join(path2) if path2 else "Failed")
