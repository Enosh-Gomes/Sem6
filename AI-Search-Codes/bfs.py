from collections import deque

def bfs(graph,start,goal):
    visited=set()
    queue=deque([[start]])
    while queue:
        path=queue.popleft()
        node=path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbour in graph.get(node,[]):
                new_path=list(path)
                new_path.append(neighbour)
                queue.append(new_path)
    return None
        
def get_graph_from_user():
        graph={}
        n=int(input("enter n:")) 
        for _ in range(n):
            node=input("enter node name:")
            neighbours=input(f"enter neighbours of {node} seperated by space:").split()
            graph[node]=neighbours
        return graph
        
if __name__ == "__main__":
            print("Define the graph")
            graph=get_graph_from_user()
            start=input("enter the start:")
            goal=input("enter goal node:")
            path = bfs(graph, start, goal)

            if path:
              print("Path found using BFS:", " -> ".join(path))
            else:
              print("No path found.")
            