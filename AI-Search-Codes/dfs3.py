

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

graph={}
n=int(input("enter n:"))
for i in range(n):
    node=input("enter the node:")
    neighbours=input("enter the neighbours:").split()
    graph[node]=neighbours
    
start=input("enter start state:")
goal=input("enter end state:")

solution=dfs(graph,start,goal)
if solution:
    print("-> " .join(solution))
else:
    print("No path found.")
            
