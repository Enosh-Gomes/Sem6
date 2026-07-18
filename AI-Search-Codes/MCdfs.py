def is_valid(m,c):
    return (m==0 or m>=c) and 0<=m<=3 and 0<=c<=3

def next_states(m,c,boat):
    moves=[(1,0),(0,1),(1,1),(2,0),(0,2)]
    next_state=[]
    
    for dm,dc in moves:
        if boat=='left':
            new_m=m-dm
            new_c=c-dc
            if is_valid(new_m,new_c) and is_valid(3-new_m,3-new_c):
              next_state.append((new_m,new_c,'right'))
        else:
            new_m=m+dm
            new_c=c+dc
            if is_valid(new_m,new_c) and is_valid(3-new_m,3-new_c):
              next_state.append((new_m,new_c,'left'))
    return next_state

def dfs():
    start=(3,3,'left')
    goal=(0,0,'right')
    visited=set()
    stack=[[start]]
    
    while stack:
        path=stack.pop()
        node=path[-1]
        
        if node==goal:
            return path
        
        if node in visited:
            continue
        
        visited.add(node)
        m,c,boat=node
        
        for next_state in next_states(m,c,boat):
            if next_state not in visited:
                new_path=list(path)
                new_path.append(next_state)
                stack.append(new_path)
    return None

solution=dfs()
if solution:
    for step in solution:
        print(step)
        
else:
    print("nahi")
                
               
        