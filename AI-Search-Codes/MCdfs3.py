

def is_valid(m,c):
    return 0<=m<=3 and (m==0 or m>=c) and 0<=c<=3

def get_neighbours(m,c,b):
    neighbours=[]
    moves=[(1,0),(0,1),(1,1),(2,0),(0,2)]
    next_state=None
    for dm,dc in moves:
        if b=='left':
           new_m=m-dm
           new_c=c-dc
           if is_valid(new_m,new_c) and is_valid(3-new_m,3-new_c):
            next_state=(new_m,new_c,'right')
            neighbours.append(next_state)
            
        else:
           new_m=m+dm
           new_c=c+dc
           if is_valid(new_m,new_c) and is_valid(3-new_m,3-new_c):
            next_state=(new_m,new_c,'left')
            neighbours.append(next_state)
            
    return neighbours

def dfs():
    start=(3,3,'left')
    goal=(0,0,'right')
    all_paths=[]
    
    stack=[[start]]
    while stack:
        path=stack.pop()
        node=path[-1]
        
        if node==goal:
            all_paths.append(path)
            continue
        
        m,c,b=node
        
        for neighbour in get_neighbours(m,c,b):
            if neighbour not in path:
                new_path=list(path)
                new_path.append(neighbour)
                stack.append(new_path)
    return all_paths

solution=dfs()

if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
    print()
    
else:
    print("nahi hua")
    
            
         
        