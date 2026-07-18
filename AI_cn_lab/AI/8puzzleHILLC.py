def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def heuristic(state, goal):
    distance = 0
    for num in range(1, 9):
        i = state.index(num)
        j = goal.index(num)
        xi, yi = i // 3, i % 3
        xj, yj = j // 3, j % 3
        distance += abs(xi - xj) + abs(yi - yj)
    return distance


def move(state, direction):
    i = state.index(0)
    new_state = list(state)
    if direction == 'up' and i > 2:
        new_state[i], new_state[i-3] = new_state[i-3], new_state[i]
    elif direction == 'down' and i < 6:
        new_state[i], new_state[i+3] = new_state[i+3], new_state[i]
    elif direction == 'left' and i % 3 != 0:
        new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
    elif direction == 'right' and i % 3 != 2:
        new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
    else:
        return None
    return tuple(new_state)

def get_neighbors(state):
    return [move(state, d) for d in ['up', 'down', 'left', 'right'] if move(state, d)]

def hill_climbing(start, goal):
    current = start
    h = heuristic(current, goal)
    steps = 0
    print("Initial State:")
    print_state(current)
    print("Heuristic:", h, "\n")

    while h > 0:
        neighbors = get_neighbors(current)
        best = current
        best_h = h

        for n in neighbors:
            nh = heuristic(n, goal)
            if nh < best_h:
                best = n
                best_h = nh

        if best == current:
            print("Stuck at local minimum. No solution found.")
            return

        current = best
        h = best_h
        steps += 1
        print(f"Step {steps}:")
        print_state(current)
        print("Heuristic:", h, "\n")

    print("Goal reached in", steps, "steps!")

start = tuple(map(int, input("Enter initial state (space-separated 0-8): ").split()))
goal = tuple(map(int, input("Enter goal state (space-separated 0-8): ").split()))

hill_climbing(start, goal)
