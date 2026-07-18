

def dfs(graph,start,goal):
    stack=[[start]]
    while stack:
        path=stack.pop()
        node=path[-1]
        
        if node==goal:
            return path
        
        for neighbour in graph.get(node,[]):
            if neighbour not in path:
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
print()

start=input("enter the start node:")
goal=input("enter the goal node:")

solution=dfs(graph,start,goal)
if solution:
        print("->".join(solution))
else:
    print("nahi hua")


