from collections import deque

def bfs(graph,start,goal):
    queue=deque([[start]])
    while queue:
        path=queue.popleft()
        node=path[-1]
        
        if node==goal:
            return path
        
        for neighbour in graph.get(node,[]):
            if neighbour not in path:
                new_path=list(path)
                new_path.append(neighbour)
                queue.append(new_path)
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

solution=bfs(graph,start,goal)
if solution:
        print("->".join(solution))
else:
    print("nahi hua")


