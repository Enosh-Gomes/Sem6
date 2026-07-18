from collections import deque
def bfs(graph,start,goal):
    visited=set()
    queue=deque([[start]])
    while queue:
        path=queue.popleft()
        node=path[-1]
        
        if node==goal:
            return path
        
        if node not in visited:
            visited.add(node)
            
        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                new_path=list(path)
                new_path.append(neighbour)
                queue.append(new_path)
    return None
    

graph={
    "A":["B","C"],
    "B":["D"],
    "C":["D"],
    "D":['E'],
    'E': []
}

start="A"
goal="E"

path=bfs(graph,start,goal)

if path:
    print(path)
else:
    print("NAHI HAI PATH")