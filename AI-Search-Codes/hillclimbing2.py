def simple_hill(graph, heuristics, start, goal):
    current=start
    path=[current]
    h=heuristics[current]
    
    while True:
        found=False
        best_h=h
        for neighbour in graph.get(current,[]):
            if best_h>heuristics[neighbour]:
                best_h=heuristics[neighbour]
                current=neighbour
                path.append(current)
                h=best_h
                found=True
                break
            
        if found==False:
            break
        
        if current==goal:
            return path
        
    return path if current==goal else None
                
            
            
def steep_hill(graph, heuristics, start, goal):
    current=start
    path=[current]
    h=heuristics[current]
   
    while True:
        neighbours=graph.get(current,[])
        next_state=None
        best_h=h
       
        for neighbour in neighbours:
           if best_h>heuristics[neighbour]:
               best_h=heuristics[neighbour]
               next_state=neighbour
        
        if next_state is None:
            break
        
        current=next_state
        path.append(current)
        h=best_h
        
        if current==goal:
            return path
        
    return path if current==goal else None
       
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

heuristics = {
    'A': 10,
    'B': 8,
    'C': 9,
    'D': 7,
    'E': 5,
    'F': 6,
    'G': 0
}
 
start = 'A'
goal = 'G'

path1 = simple_hill(graph, heuristics, start, goal)
print("Simple Hill Climbing Path:", " -> ".join(path1) if path1 else "Failed")

path2 = steep_hill(graph, heuristics, start, goal)
print("Steepest Ascent Path:", " -> ".join(path2) if path2 else "Failed")
