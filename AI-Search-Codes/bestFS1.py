def bestFS(graph,heuristic,start,goal):
    visited=set()
    queue=[(heuristic[start],[start])]
    while queue:
        queue.sort()
        h,path=queue.pop(0)
        node=path[-1]
        
        if node==goal:
            return path
        
        if node not in visited:
            visited.add(node)
            
        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                new_path=list(path)
                new_path.append(neighbour)
                queue.append((heuristic[neighbour],new_path))
    return None

graph={
    "A":["B","C"],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

heuristics={
    'A':6,
    'B':5,
    'C': 4,
    'D': 7,
    'E': 3,
    'F': 5,
    'G': 0  
}

start='A'
goal ='G'

path=bestFS(graph,heuristics,start,goal)
if path:
    print(path)
else:
    print("nothing")