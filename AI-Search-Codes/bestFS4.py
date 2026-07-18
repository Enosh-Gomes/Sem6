

def bestfs(graph,heuristic,start,goal):
    queue=[(heuristic[start],[start])] # dont forget this [ ]
    while queue:
        queue.sort()
        h,path=queue.pop(0)
        node=path[-1]
        
        if node==goal:
            return path
        
        for neighbour in graph.get(node,[]):
            if neighbour not in path:
                new_path=list(path)
                new_path.append(neighbour)
                queue.append((heuristic[neighbour],new_path))
    return None

'''graph={}
heuristic={}
n=int(input("enter n:"))
for i in range(n):
    node=input("enter the node:")
    neighbours=input("enter the neighbours:").split()
    graph[node]=neighbours
print()

for i in range(n):
    node=input("enter the node:")
    value=int(input("enter the heurisctic:"))
    heuristic[node]=value

start=input("enter the start node:")
goal=input("enter the goal node:")

solution=bestfs(graph,heuristic,start,goal)
if solution:
        print("->".join(solution))
else:
    print("nahi hua") '''
    
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


