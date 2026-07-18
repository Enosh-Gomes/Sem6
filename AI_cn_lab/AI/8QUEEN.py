import random
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
def get_best_neighbor(board):
    min_h = float('inf')
    best_neighbors = []
    for row in range(8):
        for col in range(1, 9):
            if col != board[row]:
                temp = board[:]
                temp[row] = col
                h = heuristic(temp)
                if h < min_h:
                    best_neighbors = [temp]
                    min_h = h
                elif h == min_h:
                    best_neighbors.append(temp)
    if best_neighbors:
        return random.choice(best_neighbors), min_h
    return board, heuristic(board)

def solve_queens(board):
    total_iterations = 0
    while True:
        h = heuristic(board)
        print("Initial Board:")
        show_board(board)
        print("Initial Heuristic:", h, "\n")
        while True:
            next_board, next_h = get_best_neighbor(board)
            total_iterations += 1
            if next_h >= h:
                break
            board, h = next_board, next_h
            print(f"Iteration {total_iterations}:")
            show_board(board)
            print("Current Heuristic:", h, "\n")
        print("Final Board:")
        show_board(board)
        print(f"Final Heuristic: {h}")
        print(f"Total Iterations: {total_iterations}")
        if h == 0:
            print("Solution Found!")
            break
        else:
            print("Stuck in Local Minima. Restarting...\n")
            board = [random.randint(1, 8) for _ in range(8)]
initial_board = [int(input(f"Column for row {i+1} (1-8): ")) for i in range(8)]
solve_queens(initial_board)
