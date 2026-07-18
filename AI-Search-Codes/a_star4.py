def a_star(graph,heuristic,start,goal):
    queue=[(heuristic[start],0,[start])]
    cost_so_far={start:0}
    while queue:
        queue.sort()
        f,g,path=queue.pop(0)
        node=path[-1]
        
        if node==goal:
            return path
        
        for neighbour,cost in graph.get(node,[]):
            if neighbour not in path:
                new_g=g+cost
                if neighbour not in cost_so_far or new_g<cost_so_far[neighbour]:
                 cost_so_far[neighbour]=new_g
                 f=new_g+heuristic[neighbour] #use new_g not g
                 new_path=list(path)
                 new_path.append(neighbour)
                 queue.append((f,new_g,new_path))
    return None

graph={}
h={}
n=int(input("enter n:"))
for i in range(n):
    node=input("enter the node:")
    neighbours=input("enter the neighbours with cost:").split()
    graph[node]=[]
    for entity in neighbours:
        dest,cost=entity.split(":")
        graph[node].append((dest,int(cost))) # make cost in
    
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
            
        