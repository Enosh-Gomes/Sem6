from collections import deque
def is_valid(state, m, c):
    m1, c1, _ = state
    m2, c2 = m - m1, c - c1
    if m1 < 0 or m2 < 0 or c1 < 0 or c2 < 0:
        return False
    if (m1 and m1 < c1) or (m2 and m2 < c2):
        return False
    return True
def generate_successors(state, m, c, b):
    m1, c1, boat = state
    successors = []
    for ms in range(b + 1):
        for cn in range(b + 1):
            if ms + cn == 0 or ms + cn > b:
                continue
            if boat == 1:
                new_state = (m1 - ms, c1 - cn, 0)
            else:
                new_state = (m1 + ms, c1 + cn, 1)
            if is_valid(new_state, m, c):
                successors.append(new_state)
    return successors
def bfs(m, c, b):
    start_state = (m, c, 1)
    goal_state = (0, 0, 0)
    queue = deque([(start_state, [])])
    visited = set()
    allpaths = []
    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        path = path + [state]
        if state == goal_state:
            allpaths.append(path)
            continue
        visited.add(state)
        for successor in generate_successors(state, m, c, b):
            if successor not in visited:
                queue.append((successor, path))
    return allpaths

m = int(input("Enter number of Missionaries: "))
c = int(input("Enter number of Cannibals: "))
b = int(input("Enter boat capacity: "))

solutions = bfs(m, c, b)
if not solutions:
    print("No solutions found.")
else:
    print(f"Found {len(solutions)} solution(s):")
    for i, path in enumerate(solutions, 1):
        print(f"\nSolution {i}:")
        for state in path:
            print(state)
