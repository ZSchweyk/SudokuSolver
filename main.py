def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # Step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)
    if row is None:
        return True

    # Step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # Step 3: check if this is a valid guess
        print(f"Checking {guess} at ({row}, {col})")
        if is_valid(puzzle, guess, row, col):
            print("Valid")
            puzzle[row][col] = guess

            # if the rest of the puzzle can be solved with that guess, return True
            # otherwise, reset that guess back to -1
            if solve_sudoku(puzzle):
                print("can solve the rest of the puzzle")
                return True

        puzzle[row][col] = -1

    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(example_board)
    print(solve_sudoku(example_board))
    print(example_board)



