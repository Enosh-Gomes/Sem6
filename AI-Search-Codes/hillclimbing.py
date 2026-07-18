
def simple_hill(graph,heuristics,start,goal):
  current= start
  path=[current]
  
  while True:
      found_better=False
      for neighbour in graph.get(current,[]):
          if heuristics[current] > heuristics[neighbour]:
              current=neighbour
              path.append(current)
              found_better=True
              break
       
      if not found_better or current==goal:
           break
       
  return path if current==goal else None
    
    
def steep_hill(graph,heuristics,start,goal):
  current= start
  path=[current]
  
  while True:
      neighbours=graph.get(current,[])
      if not neighbours:
       break
   
      best=min(neighbours,key=lambda n: heuristics[n])
      if heuristics[best]< heuristics[current]:
          current=best
          path.append(current)
          if current==goal:
              return path
      else:
        break
    
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



          
          
    
    
    
 
 
 
 
 
 
 
 
 
 
    
