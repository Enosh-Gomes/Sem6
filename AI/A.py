goal = ""
graph = {}
heuristics = {}
Nil = None

def Head(list):
    return list[0] if list else None

def Tail(list):
    return list[1:] if list else []

def Cons(item, list):
    return [item] + list

def Append(list1, list2):
    return list1 + list2

def GoalTest(node):
    return node == goal

def MoveGen(node):
    return graph.get(node, [])

def h(node):
    return heuristics.get(node, 99)

def FindNode(list, node):
    return next((item for item in list if item[0] == node), Nil)

def RemoveNode(list, node):
    return [item for item in list if item[0] != node]

def ReplaceNode(list, node, new_node):
    return [new_node if item[0] == node else item for item in list]

def Sort_f(list):
    return sorted(list, key=lambda x: (x[4], x[3], x[0]))

def ReconstructPath(nodepair, closed):
    path = [nodepair[0]]
    parent = nodepair[1]

    while parent is not Nil:
        path.append(parent)
        node = next((item for item in closed if item[0] == parent), Nil)
        parent = node[1] if node else Nil

    path.reverse()
    return path

def PropagateImprovement(nodepair, open, closed):
    neighbours = MoveGen(nodepair[0])

    for child, cost in neighbours:
        open_child = FindNode(open, child)
        closed_child = FindNode(closed, child)
        child_node = open_child if open_child is not Nil else closed_child

        if child_node is not Nil and child_node[1] == nodepair[0]:
            new_g = nodepair[2] + cost

            if new_g < child_node[2]:
                new_h = h(child)
                updated_child = (child, nodepair[0], new_g, new_h, new_g + new_h)

                if open_child is not Nil:
                    open = ReplaceNode(open, child, updated_child)
                else:
                    closed = ReplaceNode(closed, child, updated_child)
                    open, closed = PropagateImprovement(updated_child, open, closed)

    return open, closed

def A_star_search(start):
    start_h = h(start)
    open = [(start, Nil, 0, start_h, start_h)]
    closed = []
    iteration = 1
    
    print(f"\n{'-' * 152}")
    print(f"{'iteration':<9} | {'OPEN':<69} | {'CLOSED'}")

    while open:
        open = Sort_f(open)
        nodepair = Head(open)
        node = nodepair[0]

        print("-" * 152)

        open_str = ", ".join(str(x).replace("None", "Nil") for x in open)
        closed_str = ", ".join(str(x).replace("None", "Nil") for x in closed)

        # split long text manually
        max_width = 69

        open_lines = [open_str[i:i+max_width] for i in range(0, len(open_str), max_width)]
        closed_lines = [closed_str[i:i+max_width] for i in range(0, len(closed_str), max_width)]

        rows = max(len(open_lines), len(closed_lines))

        for i in range(rows):
            iter_col = str(iteration) if i == 0 else ""

            open_col = open_lines[i] if i < len(open_lines) else ""
            closed_col = closed_lines[i] if i < len(closed_lines) else ""

            print(f"{'     ' + iter_col:<9} | {open_col:<69} | {closed_col}")

        if GoalTest(node):
            print("-" * 152)
            print(f"{'     ' + str(iteration + 1):<9} | {'Goal Found':<69} |")
            print("-" * 152)
            return ReconstructPath(nodepair, closed)

        open = Tail(open)
        closed = Cons(nodepair, closed)
        neighbours = MoveGen(node)

        for child, cost in neighbours:
            new_g = nodepair[2] + cost
            new_h = h(child)
            new_f = new_g + new_h
            new_node = (child, node, new_g, new_h, new_f)

            open_child = FindNode(open, child)
            closed_child = FindNode(closed, child)

            if open_child is Nil and closed_child is Nil:
                open = Append(open, [new_node])

            elif open_child is not Nil:
                if new_g < open_child[2]:
                    open = ReplaceNode(open, child, new_node)

            else:
                if new_g < closed_child[2]:
                    closed = ReplaceNode(closed, child, new_node)
                    open, closed = PropagateImprovement(new_node, open, closed)

        iteration += 1

    return None

def get_input():
    global start, goal, graph, heuristics
    n = int(input("Enter the number of nodes: "))

    for _ in range(n):
        name = input("\nNode: ")
        val = int(input("h(Node): "))
        children = input("Neighbors: ").split()

        weighted_children = []
        for child in children:
            cost = int(input(f"cost({name}->{child}): "))
            weighted_children.append((child, cost))

        heuristics[name] = val
        graph[name] = weighted_children

    start = input("\nEnter start node: ")
    goal = input("Enter goal node: ")

if __name__ == "__main__":
    get_input()
    path = A_star_search(start)

    if path:
        print(f"\nPath: {' -> '.join(path)}")
    else:
        print("\nNo path found.")

'''
8
S
17
A B C
6
5
10
A
10
E
6
B
13
E D
6
7
C
4
D
6
D
2
F
6
E
4
F
4
F
1
G
3
G
0

S
G
'''