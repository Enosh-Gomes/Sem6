def solvable(state):
    puzzle=[x for x in state if x!=0]
    inversions=0
    n=len(puzzle)
    for i in range(n):
        for j in range(i+1,n):
            if puzzle[i]>puzzle[j]:
                inversions+=1
    return inversions % 2==0
            


def heuristic(state,goal):
    n=len(state)
    count=0
    for i in range(n):
        for j in range(n):
            if state[i][j]!=goal[i][j]:
                count+=1
                
    return count


def find_blank(state):
    n=len(state)
    for i in range(n):
        for j in range(n):
            if state[i][j]==0:
                return i,j


def get_neighbours(state):
    neighbours=[]
    x,y=find_blank(state)
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    
    for dx,dy in directions:
        nx=x+dx
        ny=y+dy
        
        if 0<=nx<3 and 0<=ny<3:
            new_state=[row[:] for row in state] # remembee this line
            new_state[x][y],new_state[nx][ny]=new_state[nx][ny],new_state[x][y] #remember to use new state here
            neighbours.append(new_state)
            
    return neighbours

def hill(start,goal):
    current=start
    path=[current]
    h=heuristic(start,goal)
    while True:
        best_h=h
        next_state=None
        neighbours=get_neighbours(current)
        for neigbour in neighbours:
            if best_h> heuristic(neigbour,goal):
                best_h=heuristic(neigbour,goal) #mistake made
                next_state=neigbour
        
        if next_state is None :
            break
        
        current=next_state
        h=best_h
        path.append(current)
        if current == goal:
            return path
        
    return path if current==goal else None

start=[]
goal=[]

start.extend(list(map(int,input("enter start:").strip().split())))
goal.extend(list(map(int,input("enter goal:").strip().split())))

if not solvable(start[:]):
    print(" This puzzle is not solvable.")
    exit()
    
start=[start[i:i+3] for i in range(0,9,3)]
goal=[goal[i:i+3] for i in range(0,9,3)]

solution = hill(start, goal)
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")


