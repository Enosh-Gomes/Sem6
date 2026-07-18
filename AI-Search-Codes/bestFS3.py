def bestfs(graph,h,start,goal):
    visited=set()
    queue=[(h[start],[start])]#start is in a [] and whole tuple is in a []
    while queue:
        queue.sort()
        heuristic,path=queue.pop(0)
        node=path[-1]
        
        if node==goal:
            return path
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                new_path=list(path)
                new_path.append(neighbour)
                queue.append((h[neighbour],new_path)) #dont forget abt tuple type in queue for this
    return None



graph={}
h={}
n=int(input("enter n:"))
for i in range(n):
    node=input("enter the node:")
    neighbours=input("enter the neighbours:").split()
    graph[node]=neighbours
    
for i in range(n):
    node=input("enter the node:")
    value=int(input("enter heuristic:"))
    h[node]=value
    
start=input("enter start state:")
goal=input("enter end state:")

solution=bestfs(graph,h,start,goal)
if solution:
    print("-> " .join(solution))
else:
    print("No path found.")
            
