
def dfs(graph,start,goal):
    visited=set()
    stack=[[start]]
    while stack:
        path=stack.pop()
        node=path[-1]
        
        if node==goal:
            return path
        
        if node not in visited:
            visited.add(node)
            
        for neighbour in reversed(graph.get(node,[])):
            if neighbour not in visited:
                new_path=list(path)
                new_path.append(neighbour)
                stack.append(new_path)
    return None
    

graph={
    "A":["B","C"],
    "B":["K"],
    "C":["D"],
    "D":['E'],
    'E': [],
    'K':[]
}

start="A"
goal="E"

path=dfs(graph,start,goal)

if path:
    print(path)
else:
    print("NAHI HAI PATH")