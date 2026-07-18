import random
    
def print_board(state):
    n=len(state)
    for r in range(n):
        row=['.']*n
        row[state[r]]='Q'
        print(" ".join(row))
    print()
    
    
def count_conflicts(state,row,col):
        n=len(state)
        count=0
        for r in range(n):
            if r==row:
                continue
            c=state[r]
            
            if c==col or abs(row-r)==abs(col-c):
                count+=1
                
        return count
    
    
    
def min_conflicts(state,min_steps=1000):
    n=len(state)
    
    for _ in range(min_steps):
        conflicted=[r for r in range(n) if count_conflicts(state,r,state[r])>0]
        if not conflicted:
            return state
        
        row=random.choice(conflicted) #dont forget
        
        min_c=len(state)
        best_cols=[]
        
        for col in range(n):
            c=count_conflicts(state,row,col)
            
            if c<min_c:
                min_c=c
                best_cols=[col]
            elif min_c==c:
                best_cols.append(col)
                
        state[row]=random.choice(best_cols) #dont forget
    
    return None
    
user_input = input("Enter initial positions (space-separated columns for each row): ")
positions=list(map(int,user_input.strip().split()))


solution = min_conflicts(positions)

if solution:
    print(" Solution found:")
    print_board(solution)
else:
    print(" No solution found.")