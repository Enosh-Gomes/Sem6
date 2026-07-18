


def is_goal(state,target):
    x,y=state
    return x==target or y==target

def next_states(x,y,max_x,max_y):
    return set([(0,y),(x,0),(max_x,y),(x,max_y),(x-min(x,max_y-y),y+min(x,max_y-y)),(x+min(max_x-x,y),y-min(max_x-x,y))
    ])
    
def dfs(m,n,target):
    start=(0,0)
    visited=set()
    stack=[[start]]
    allpaths=[]
    while stack:
        path=stack.pop()
        state=path[-1]
        
        if is_goal(state,target):
            allpaths.append(list(path))
            continue
        
        if state not in visited:
            visited.add(state)
            
        x,y=state
            
        for next_state in next_states(x,y,m,n):
            if next_state not in visited:
                new_path=list(path)
                new_path.append(next_state)
                stack.append(new_path)
    return allpaths

max_x=4
max_y=3
target=2

path=dfs(max_x,max_y,target)
if path:
    for step in path:
        print(step)
else:
    print("no soln")
    