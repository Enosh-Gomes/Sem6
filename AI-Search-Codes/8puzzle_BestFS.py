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

def find_blank(state):
     for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j
            

def get_neighbours(state):
    neighbours=[]
    x,y=find_blank(state)
    directions=[(-1,0), (1,0), (0,-1), (0,1)]
    
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            new_state=[row[:]  for row in state]
            new_state[x][y],new_state[nx][ny]=new_state[nx][ny],new_state[x][y]
            neighbours.append(new_state)
            
    return neighbours



def best_first(start):
    queue=[(heuristic(start),start,[start])]
    visited=[]
    
    while queue:
        queue.sort()
        h,current,path=queue.pop(0)
        
        if current==goal:
            return path
        
        visited.append(current)
        
        for neighbour in get_neighbours(current):
            if neighbour not in visited:
                queue.append((heuristic(neighbour),neighbour,path + [neighbour]))
        
    return None





# Example usage
start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

solution = best_first(start)

# Show steps
if solution:
    print("Steps to reach goal:")
    for step in solution:
        for row in step:
            print(row)
        print("-----")
else:
    print("No solution found.")


