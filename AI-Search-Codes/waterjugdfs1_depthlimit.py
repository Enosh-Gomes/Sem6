def is_goal(state, target):
    x, y = state
    return x == target or y == target

def next_states(x, y, max_x, max_y):
    return set([
        (0, y),  # Empty jug X
        (x, 0),  # Empty jug Y
        (max_x, y),  # Fill jug X
        (x, max_y),  # Fill jug Y
        (x - min(x, max_y - y), y + min(x, max_y - y)),  # Pour X → Y
        (x + min(max_x - x, y), y - min(max_x - x, y))   # Pour Y → X
    ])

def dfs(m, n, target, depth_limit):
    start = (0, 0)
    visited = set()
    stack = [[start]]

    while stack:
        path = stack.pop()
        state = path[-1]

        if len(path) > depth_limit + 1:
            continue

        if is_goal(state, target):
            return path

        if state not in visited:
            visited.add(state)

        x, y = state
        for next_state in next_states(x, y, m, n):
            if next_state not in visited:
                new_path = list(path)
                new_path.append(next_state)
                stack.append(new_path)

    return None

# Example usage
max_x = 4
max_y = 3
target = 2
depth_limit = 6

path = dfs(max_x, max_y, target, depth_limit)
if path:
    for step in path:
        print(step)
else:
    print("no soln")
