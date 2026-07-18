def dfs(graph,start,goal):
    visited=set()
    stack=[[start]]
    while stack:
        path=stack.pop()
        node=path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbour in reversed(graph.get(node,[])):
                new_path=list(path)
                new_path.append(neighbour)
                stack.append(new_path)
                
    return None

def get_graph():
    graph={}
    n=int(input("enter no of nodes:"))
    for _ in range(n):
        node=input("enter the node:")
        neighbour=input("enter the neighbours: ").split()
        graph[node]=neighbour
        
    return graph 


if __name__=="__main__":
    print("define graph")
    graph=get_graph()
    start=input("enter the start:")
    goal=input("enter goal node:")
    path = dfs(graph, start, goal)
    if path:
      print("Path found using DFS:", "->".join(path))
    else:
      print("No path found:")
