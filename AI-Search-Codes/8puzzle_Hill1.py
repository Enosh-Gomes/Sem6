
goal=[ [1,2,3],
[4,5,6],
[7,8,0]]


def heuristic(state):
    count=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=goal[i][j]:
                count+=1
    return count

def get_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j
            
            
def get_neighbours(state):
    neighbours=[]
    x,y=get_blank(state)
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            new_state=[row[:] for row in state]
            new_state[x][y],new_state[nx][ny]=new_state[nx][ny],new_state[x][y]
            neighbours.append(new_state)
            
    return neighbours


def hill(start):
    path=[start]
    visited=[]
    h=heuristic(start)
    current=start
    
    while True:
     neighbours=get_neighbours(current)
     next_state=None
     best_h=h
     
     for neighbour in neighbours:
         if best_h > heuristic(neighbour):
             best_h=heuristic(neighbour)
             next_state=neighbour
             
     if next_state is None:
             break
         
     current=next_state
     path.append(current)
     h=best_h
         
     if current==goal:
        break
     

    return path
    
# Example usage
start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

solution = hill(start)

if solution[-1] == goal:
     print("Steps to reach goal:")
     for step in solution:
         for row in step:
            print(row)
         print("-----")
else:
    print("No solution found.")
