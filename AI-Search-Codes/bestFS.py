import heapq

def bestfs(graph,heuristics,start,goal):
    visited=set()
    queue=[(heuristics[start],[start])]
    
    while queue:
        h,path=heapq.heappop(queue)
        node=path[-1]
        
        if node==goal:
            return path
        
        if node in visited:
            continue
        
        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                new_path=list(path)
                new_path.append(neighbour)
                heapq.heappush(queue,(heuristics[neighbour],new_path))
                
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

path=bestfs(graph,heuristics,start,goal)
if path:
    print(path)
else:
    print("nothing")