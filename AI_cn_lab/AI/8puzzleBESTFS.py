import heapq
def manhattan(state, goal):
    distance = 0
    for num in '12345678':
        i = state.index(num)
        j = goal.index(num)
        x1, y1 = i // 3, i % 3
        x2, y2 = j // 3, j % 3
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(state):
    moves = []
    i = state.index('0')
    row, col = i // 3, i % 3
    directions = [(-1,0), (1,0), (0,-1), (0,1)] 

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            j = new_row * 3 + new_col
            lst = list(state)
            lst[i], lst[j] = lst[j], lst[i]
            moves.append(''.join(lst))
    return moves

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

def best_first_search(start, goal):
    queue = []
    heapq.heappush(queue, (manhattan(start, goal), [start]))
    visited = set()
    step = 1
    while queue:
        h, path = heapq.heappop(queue)
        state = path[-1]
        if state in visited:
            continue
        visited.add(state)
        print(f"Step {step} - Heuristic: {h}")
        print_state(state)
        step += 1
        if state == goal:
            print("Goal reached!")
            print("Path to goal:")
            for s in path:
                print_state(s)
            return
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(queue, (manhattan(neighbor, goal), path + [neighbor]))
    print("No solution found.")
start = input("Enter initial state (use 0 for blank, space-separated): ").replace(" ", "")
goal = input("Enter goal state (use 0 for blank, space-separated): ").replace(" ", "")
best_first_search(start, goal)
