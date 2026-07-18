def dfs(graph,start,goal):
    visited=set()
    stack=[[start]]
    while stack:
        path=stack.pop()
        node=path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbour in reversed(graph.get(node,[])):
                new_path=list(path)
                new_path.append(neighbour)
                stack.append(new_path)
                
    return None

graph={
    "A":["B","C"],
    "B":["D"],
    "C": ["D"],
    "D": []
}

start="A"
goal="D"

path=dfs(graph,start,goal)

if path:
    print("Path found using DFS:", "->".join(path))
else:
    print("No path found:")


        