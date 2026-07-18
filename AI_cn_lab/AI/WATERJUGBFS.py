from collections import deque
def water_jug_problem_all_solutions_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()
    solutions = []
    queue.append(((0, 0), [(0, 0)], []))
    print("\nStarting Water Jug Problem with BFS...")
    print("Initial state: (0, 0)")
    while queue:
        (jug1, jug2), path, operations = queue.popleft()
        if jug1 == target or jug2 == target:
            solutions.append((path, operations))
            continue
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        next_states = [
            ((jug1_capacity, jug2), "Fill Jug1"),
            ((jug1, jug2_capacity), "Fill Jug2"),
            ((0, jug2), "Empty Jug1"),
            ((jug1, 0), "Empty Jug2"),
            ((jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)), "Pour Jug1 -> Jug2"),
            ((jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)), "Pour Jug2 -> Jug1")
        ]
        for state, operation in next_states:
            if state not in visited:
                queue.append((state, path + [state], operations + [operation]))
    return solutions

jug1_capacity = int(input("Enter the capacity of Jug 1: "))
jug2_capacity = int(input("Enter the capacity of Jug 2: "))
target = int(input("Enter the target amount: "))
solutions = water_jug_problem_all_solutions_bfs(jug1_capacity, jug2_capacity, target)
if solutions:
    print(f"\nFound {len(solutions)} solution(s):")
    for i, (path, operations) in enumerate(solutions, start=1):
        print(f"\nSolution {i}:")
        print(f"States: {path}")
        print(f"Path: {operations}")
else:
    print("\nNo solution found!")
