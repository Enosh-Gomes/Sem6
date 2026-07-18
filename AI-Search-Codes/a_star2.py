def a_star(graph,heuristics,start,goal):
    queue=[(heuristics[start],0,[start])]
    while queue:
        queue.sort()
        f,g,path=queue.pop(0)
        node=path[-1]
        
        if node==goal:
            return path
        
        for neighbour,cost in graph.get(node,[]):
            if neighbour not in path:
                g_new=g+cost
                f_new=g+heuristics[neighbour]
                new_path=list(path)
                new_path.append(neighbour)
                queue.append((f_new,g_new,new_path))
    return None




graph={}
h={}
n=int(input("enter n:"))
for i in range(n):
    node=input("enter the node:")
    neighbours=input("enter the neighbours with cost(B:2 C:3):").split()
    graph[node]=[]
    for entry in neighbours:
        dest,cost=entry.split(":")
        graph[node].append((dest,int(cost))) # put tuple and make cost int
    
print()
    
for i in range(n):
    node=input("enter the node:")
    value=int(input("enter heuristic:"))
    h[node]=value
    
start=input("enter start state:")
goal=input("enter end state:")

solution=a_star(graph,h,start,goal)
if solution:
    print("-> " .join(solution))
else:
    print("No path found.")
            
