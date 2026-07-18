

def is_valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c)

def get_next_states(m, c, b):
    next_state = []
    moves = [(1,1), (1,0), (0,1), (2,0), (0,2)]
    
    for dm, dc in moves:
        if b == 'left':
            new_m = m - dm
            new_c = c - dc
            if is_valid(new_m, new_c) and is_valid(3 - new_m, 3 - new_c):
                next_state.append((new_m, new_c, 'right'))
        else:
            new_m = m + dm
            new_c = c + dc
            if is_valid(new_m, new_c) and is_valid(3 - new_m, 3 - new_c):
                next_state.append((new_m, new_c, 'left'))
                
    return next_state

def dfs():
    start = (3, 3, 'left')
    goal = (0, 0, 'right')
    
    visited = set()
    stack = [[start]]
    
    while stack:
        path = stack.pop()
        state = path[-1]
        
        if state == goal:
            return path
        
        if state not in visited:
            visited.add(state)
        
        m, c, b = state
        
        for next_state in get_next_states(m, c, b):
            if next_state not in visited:
                new_path = list(path)
                new_path.append(next_state)
                stack.append(new_path)
    return None

solution = dfs()

if solution:
    for step in solution:
        print(step)
else:
    print("nahi")
