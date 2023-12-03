import tkinter as tk
import numpy as np

def is_safe_placement(row, col, board):
    n = len(board)

    # Check if there are queens in the same row
    for i in range(n):
        if board[i][col] == 1:
            return False

    # Check if there are queens in the same column
    for i in range(n):
        if board[row][i] == 1:
            return False

    # Check if there are queens in the diagonals
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    i = row
    j = col
    while i < n and j < n:
        if board[i][j] == 1:
            return False
        i += 1
        j += 1

    return True

def solve_n_queens(n, max_depth=None):
    if max_depth is None:
        max_depth = n

    queens_positions = []

    board = np.zeros((n, n), dtype=int)

    def place_queen(row):
        if row == n:
            queens_positions.append(board.copy())
            return

        for col in range(n):
            if is_safe_placement(row, col, board):
                board[row][col] = 1

                place_queen(row + 1)

                board[row][col] = 0

    place_queen(0)

    if not queens_positions:
        print("No solutions found for n =", n)

    return queens_positions


def draw_board(canvas, board):
    n = len(board)

    # Unicode chess symbols for white and black queens
    white_queen = '\u2655'
    black_queen = '\u265B'

    # Calculate cell size based on board size
    cell_size = 600 // n

    # Draw the chessboard
    for row in range(n):
        for col in range(n):
            if (row + col) % 2 == 0:
                color = "white"
            else:
                color = "black"
            canvas.create_rectangle(
                (col * cell_size, row * cell_size, (col + 1) * cell_size, (row + 1) * cell_size),
                fill=color
            )

    # Draw the queens using chess symbols
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                # Calculate the actual position of the queen
                x_pos = col * cell_size + cell_size // 2
                y_pos = row * cell_size + cell_size // 2

                # Draw the queen using chess symbol
                chess_symbol = white_queen if (row + col) % 2 == 0 else black_queen
                canvas.create_text((x_pos, y_pos), text=chess_symbol, font=("Arial", cell_size // 2), fill="red")


# ... (rest of the code remains the same)

def solve_button_click():
    try:
        n = int(n_entry.get())
    except ValueError:
        print("Please enter a valid integer for the number of queens.")
        return

    queens_positions = solve_n_queens(n)

    # Clear previous solutions
    canvas.delete("all")

    # Draw all possible solutions
    for i, board in enumerate(queens_positions):
        draw_board(canvas, board)
        canvas.create_text((300, 30 * (i + 1)),font=("Arial", 12))

window = tk.Tk()
window.title("N-N-Queens Problem")

n_label = tk.Label(window, text="Enter number of queens:")
n_label.grid(row=0, column=0)

n_entry = tk.Entry(window, width=10)
n_entry.grid(row=0, column=1)

solve_button = tk.Button(window, text="Solve", command=solve_button_click)
solve_button.grid(row=1, column=0, columnspan=2)

canvas = tk.Canvas(window, width=600, height=600)
canvas.grid(row=2, columnspan=2)

window.mainloop()
