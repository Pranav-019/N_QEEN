**N-Queens Problem Solver GUI**

**Description:**

This Python project provides a graphical user interface (GUI) for solving and visualizing solutions to the classic N-Queens problem. The N-Queens problem involves placing N queens on an N×N chessboard in such a way that no two queens threaten each other. The solution utilizes the backtracking algorithm to explore different configurations of queen placements.

**Features:**

1. **User-Friendly GUI:**
   - The program offers a simple and intuitive interface using the tkinter library for GUI development.
   - Users can input the number of queens through an Entry widget and click the "Solve" button to find solutions.

2. **Backtracking Algorithm:**
   - The core algorithm employs backtracking to systematically explore possible queen placements on the chessboard.
   - The `is_safe_placement` function ensures that queens do not threaten each other horizontally, vertically, or diagonally.

3. **Chessboard Visualization:**
   - Solutions are visualized on a graphical chessboard using Unicode chess symbols.
   - The `draw_board` function utilizes tkinter's canvas to draw the chessboard and queens.

4. **Multiple Solutions:**
   - The program identifies and displays all possible solutions to the N-Queens problem for a given input.

**How to Use:**

1. Run the Python script (`main.py`).
2. Enter the number of queens in the provided input field.
3. Click the "Solve" button to find and visualize solutions.
4. Multiple solutions are displayed on the canvas, and solution numbers are labeled.

**Dependencies:**

- Python 3.x
- tkinter library (usually included with Python installations)
- numpy library

**Files:**

- `main.py`: The main Python script containing the GUI code, backtracking algorithm, and visualization functions.
- `README.md`: This file providing information about the project.

**Notes:**

- Ensure that Python and the required libraries are installed before running the script.
- This project serves as an educational tool for understanding the N-Queens problem and backtracking algorithm.

Feel free to explore, modify, and share this project. If you encounter any issues or have suggestions for improvements, please reach out to the project contributors.

**Contributors:**
- Pranav Hare
