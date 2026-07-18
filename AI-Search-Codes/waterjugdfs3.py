

def is_goal(state,target):
    x,y=state
    return x==target or y==target

def next_states(m,n,x,y):
    return set([
        (x,0),(0,y),(m,y),(x,n)
        ,(x-min(x,n-y),y+min(x,n-y)),
        (x+min(m-x,y),y-min(m-x,y))
    ])
    
def dfs(m,n,target,depth):
    start=(0,0)
    stack=[[start]]
    all_paths=[]
    while stack:
        path=stack.pop()
        state=path[-1]
        
        if len(path)>depth:
            continue
        
        
        if is_goal(state,target):
            all_paths.append(path)
            continue
        
        x,y=state
        
        for neighbour in next_states(m,n,x,y):
            if neighbour not in path:
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
    print()
else:
  print("no soln")

                
                
    
