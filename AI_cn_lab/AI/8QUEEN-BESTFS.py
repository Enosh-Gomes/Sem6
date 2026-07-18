import heapq
def heuristic(board):
    return sum(1 for i in range(8) for j in range(i + 1, 8)
               if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]))

def show_board(board):
    for row in range(8):
        line = ["_"] * 8
        col = board[row] - 1
        line[col] = "Q"
        print(" ".join(line))
    print()

def get_neighbors(board):
    neighbors = []
    for row in range(8):
        for col in range(1, 9):
            if col != board[row]:
                new_board = board[:]
                new_board[row] = col
                neighbors.append(new_board)
    return neighbors

def best_first_search(initial_board):
    open_list = []
    visited = set()
    h = heuristic(initial_board)
    heapq.heappush(open_list, (h, initial_board))
    steps = 0
    while open_list:
        h, current = heapq.heappop(open_list)
        steps += 1
        board_tuple = tuple(current)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        print(f"Step {steps} - Heuristic: {h}")
        show_board(current)
        if h == 0:
            print("Solution Found!")
            return
        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited:
                heapq.heappush(open_list, (heuristic(neighbor), neighbor))
    print("No solution found.")
initial_board = [int(input(f"Column for row {i+1} (1-8): ")) for i in range(8)]
best_first_search(initial_board)
