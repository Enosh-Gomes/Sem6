from collections import deque

def is_goal(state,target):
    x,y=state
    return x==target or y==target

def next_state(x,y,max_x,max_y):
    return set([
        (0,y),(x,0),(max_x,y),(x,max_y),(x-min(x,max_y-y),y+min(x,max_y-y)),(x+min(max_x-x,y),y-min(max_x-x,y))
    ])
    
def bfs(max_x,max_y,target):
    start=(0,0)
    visited=set()
    queue=deque([[start]])
    
    while queue:
        path=queue.popleft()
        node=path[-1]
        
        if is_goal(node,target):
            return path
        
        if node in visited:
            continue
        
        visited.add(node)
        x,y=node
        
        for state in next_state(x,y,max_x,max_y):
            if state not in visited:
                new_path=list(path)
                new_path.append(state)
                queue.append(new_path)
                
    return None

max_x=4
max_y=3
target=2

path=bfs(max_x,max_y,target)
if path:
    for step in path:
        print(step)
else:
    print("no soln")
    