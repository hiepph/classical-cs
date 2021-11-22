# ref: https://youtu.be/Zq4upTEaQyM
#      https://youtu.be/JzONv5kaPJM

# 1. brute force
# + Generate all boards
# + Validate all boards
# + Return a valid board

# 2. backtrack
# choice: place 1-9 in an empty cell
# constraints: placement can't break board
# goal: fill the board
#
# NP-complete
# time: O(n^m), n: number of possibilities (i.e. 9)
#               m: number of spaces that are blank
# space: O(m)
#
import pprint

def is_valid_move(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    topleft_row = row - row % 3
    topleft_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[topleft_row + x][topleft_col + y] == num:
                return False

    return True


def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col]:
        return solve(grid, row, col + 1)

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
        grid[row][col] = None

    return False

if __name__ == '__main__':
    grid = [[2, 5, None, None, 3, None, 9, None, 1],
            [None, 1, None, None, None, 4, None, None, None],
            [4, None, 7, None, None, None, 2, None, 8],
            [None, None, 5, 2, None, None, None, None, None],
            [None, None, None, None, 9, 8, 1, None, None],
            [None, 4, None, None, None, 3, None, None, None],
            [None, None, None, 3, 6, None, None, 7, 2],
            [None, 7, None, None, None, None, None, None, 3],
            [9, None, 3, None, None, None, 6, None, 4]]

    if solve(grid, 0, 0):
        pprint.pprint(grid)
    else:
        print("Can't find any solution")
