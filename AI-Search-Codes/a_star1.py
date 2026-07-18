
def a_star(graph, heuristics, start, goal):
    queue=[(heuristics[start],0,[start])]
    visited=set()
    while queue:
        queue.sort()
        f,g,path=queue.pop(0)
        node=path[-1]
        
        if node==goal:
            return path
        
        if node not in visited:
            visited.add(node)
            
        for neighbour,cost in graph.get(node,[]):
            if neighbour not in visited:
                new_g=g+cost
                f=new_g+heuristics[neighbour]
                new_path=list(path)
                new_path.append(neighbour)
                queue.append((f,new_g,new_path))
    return None
       

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G',1)],
    'F': [],
    'G': []
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0  # goal
}


start = 'A'
goal = 'G'

path = a_star(graph, heuristics, start, goal)

if path:
    print("A* Path:", " -> ".join(path))
else:
    print("No path found.")
