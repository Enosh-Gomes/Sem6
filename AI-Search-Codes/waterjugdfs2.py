

def is_goal(state,goal):
    x,y=state
    return x==goal or y==goal

def next_states(x,y,max_x,max_y):
    return set([
        (x,0),(0,y),(max_x,y),(x,max_y),
        (x-min(x,max_y-y),y+min(x,max_y-y)),
        (x+min(max_x-x,y),y-min(max_x-x,y))
    ])
    
def dfs(m,n,target,depth):
    start=(0,0)
    stack=[[start]]
    visited=set()
    all_paths=[]
    while stack:
        path=stack.pop()
        node=path[-1]
        
        if len(path)>depth+1:
            continue
        
        if is_goal(node,target):
            all_paths.append(path)
            continue
        
        
        if node not in visited:
            visited.add(node)
            
        x,y=node
            
        for neighbour in next_states(x,y,m,n):
            if neighbour not in visited:
                new_path=list(path)
                new_path.append(neighbour)
                stack.append(new_path)
    return all_paths if all_paths else None

m=int(input("enter m:"))
n=int(input("enter n:"))
target=int(input("enter target:"))

depth=int(input("enter depth:"))


solution=dfs(m,n,target,depth)

if solution:
    for step in solution:
        print(step)
else:
  print("no soln")



            