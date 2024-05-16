#!/usr/bin/python3
'''N-Queens Challenge'''

import sys

# Check if the script is executed with the correct number of arguments
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Try to convert the argument to an integer (N)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    # Check if N is at least 4, as the N-Queens problem is not defined for N < 4
    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []  # List to store all solutions
    placed_queens = []  # List to store coordinates of placed queens [row, column]
    stop = False  # Flag to stop iterating
    r = 0  # Initialize row index to 0
    c = 0  # Initialize column index to 0

    # iterate thru rows
    while r < n:
        goback = False  # Flag to indicate if backtracking is needed
        # iterate thru columns
        while c < n:
            # Check if the current column is safe for placing a queen
            safe = True
            for cord in placed_queens:
                col = cord[1]
                if (col == c or col + (r - cord[0]) == c or
                        col - (r - cord[0]) == c):
                    safe = False
                    break

            if not safe:  # If not safe, move to the next column or backtrack
                if c == n - 1:
                    goback = True  # Need to backtrack
                    break
                c += 1
                continue

            # Place queen in the current row and column
            cords = [r, c]
            placed_queens.append(cords)
            # If last row, add solution and reset to the last unfinished row
            # and last safe column in that row
            if r == n - 1:
                solutions.append(placed_queens[:])
                for cord in placed_queens:
                    if cord[1] < n - 1:
                        r = cord[0]
                        c = cord[1]
                for i in range(n - r):
                    placed_queens.pop()
                if r == n - 1 and c == n - 1:
                    placed_queens = []
                    stop = True
                r -= 1
                c += 1
            else:
                c = 0  # Move to the first column of the next row
            break
        if stop:  # If all solutions found, exit the loop
            break
        # Backtrack: go back to the previous row and continue from the last safe column + 1
        if goback:
            r -= 1
            while r >= 0:
                c = placed_queens[r][1] + 1
                del placed_queens[r]  # Delete previous queen coordinates
                if c < n:
                    break
                r -= 1
            if r < 0:  # If no more rows to backtrack, exit the loop
                break
            continue
        r += 1  # Move to the next row

    # Print all solutions
    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
